from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USER_EMAIL = "bhavishyanarravula@gmail.com"
USER_PASSWORD = "Narr@2810"
USER_PHONE = "7780737243"

JOB_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer"

def cancel_application():
    try:
        close_modal = browser.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_modal.click()
        time.sleep(2)
        discard_buttons = browser.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
        if discard_buttons:
            discard_buttons[-1].click()
        print(" Skipped a multi-step application.")
    except Exception as error:
        print(f"Error while canceling application: {error}")

def wait_for_easy_apply_modal_to_close():
    try:
        WebDriverWait(browser, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div[data-test-modal-id="easy-apply-modal"]'))
        )
        print(" Easy Apply modal closed.")
    except:
        print("Timeout waiting for Easy Apply modal to close.")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.get(JOB_URL)

time.sleep(3)

try:
    overlay = browser.find_element(By.CLASS_NAME, "modal__overlay--visible")
    browser.execute_script("arguments[0].style.display = 'none';", overlay)
    print(" Overlay hidden successfully.")
except:
    print("No blocking overlay detected.")

login_link = browser.find_element(By.LINK_TEXT, "Sign in")
login_link.click()

time.sleep(3)
email_box = browser.find_element(By.ID, "username")
email_box.send_keys(USER_EMAIL)
password_box = browser.find_element(By.ID, "password")
password_box.send_keys(USER_PASSWORD)
password_box.send_keys(Keys.ENTER)

input(" Please complete any CAPTCHA if prompted, then press Enter to continue...")

time.sleep(5)
job_cards = browser.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
print(f"Found {len(job_cards)} job postings.")

for job_num, job_card in enumerate(job_cards):

    try:
        easy_apply_modal = browser.find_element(By.CSS_SELECTOR, 'div[data-test-modal-id="easy-apply-modal"]')
        if easy_apply_modal.is_displayed():
            close_btn = easy_apply_modal.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_btn.click()
            wait_for_easy_apply_modal_to_close()
            print("Closed leftover Easy Apply modal before continuing.")
    except:
        pass

    print(f"\nOpening job #{job_num + 1}")
    job_card.click()
    time.sleep(2)

    try:
        apply_btn = browser.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_btn.click()
        time.sleep(3)
        phone_box = browser.find_element(By.CSS_SELECTOR, "input[id*=phoneNumber]")
        if phone_box.get_attribute("value") == "":
            phone_box.send_keys(USER_PHONE)
        next_btn = browser.find_element(By.CSS_SELECTOR, "footer button")
        if next_btn.get_attribute("data-control-name") == "continue_unify":
            cancel_application()
            continue
        else:
            print(" Sending application...")
            next_btn.click()
        time.sleep(2)
        close_btn = browser.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_btn.click()
        wait_for_easy_apply_modal_to_close()
    except NoSuchElementException:
        print("Could not apply to this job. Skipping.")
        continue

time.sleep(5)
print(" Finished processing all jobs. Closing browser.")
browser.quit()
