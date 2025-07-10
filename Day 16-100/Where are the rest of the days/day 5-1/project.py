this is my code
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "bhavishya.texas@gmail.com"
TWITTER_PASSWORD = "Narr@2810"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path=None):
        self.driver = webdriver.Chrome(driver_path) if driver_path else webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        # Accept cookie banner if present
        try:
            consent_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
            consent_button.click()
            time.sleep(2)
        except:
            pass

        # Click GO button
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()

        # Wait for test to finish (adjust if needed)
        time.sleep(60)

        # Get download and upload speeds by class names
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

        print(f"Download speed: {self.down} Mbps")
        print(f"Upload speed: {self.up} Mbps")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(5)

        # Twitter login - update if layout changes
        email = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input'
        )
        password = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input'
        )

        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        # Wait for tweet box to load
        time.sleep(5)

        tweet = (
            f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up "
            f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        )

        tweet_compose = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
        )
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]'
        )
        tweet_button.click()

        print("Tweet posted successfully!")

        time.sleep(3)
        self.driver.quit()


# Run the bot
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()


