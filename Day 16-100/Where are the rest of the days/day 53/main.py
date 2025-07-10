from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


#url = "https://appbrewery.github.io/Zillow-Clone/"
url = "https://www.zillow.com/east-lansing-mi/rentals/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A42.81951950807953%2C%22south%22%3A42.67833577160073%2C%22east%22%3A-84.32833865771484%2C%22west%22%3A-84.59819034228515%7D%2C%22mapZoom%22%3A12%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3Anull%2C%22max%22%3A970669%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A5000%7D%2C%22beds%22%3A%7B%22min%22%3A3%7D%2C%22baths%22%3A%7B%22min%22%3A2%7D%7D%2C%22isListVisible%22%3Atrue%2C%22usersSearchTerm%22%3A%22East%20Lansing%20MI%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A38289%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D"
response = requests.get(url, headers=headers)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_link_elements]
print(f"There are {len(all_links)} links to individual listings:\n")
print(all_links)

all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]
print(f"\nCleaned {len(all_addresses)} addresses:\n")
print(all_addresses)

all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
print(f"\nCleaned {len(all_prices)} prices:\n")
print(all_prices)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdX8BhgaIF0dnNR6ZZWIPieixaTELeWXeSsmXBiXYSFJ45k4w/viewform?usp=header")
    time.sleep(2)

    address_field = driver.find_element(By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field = driver.find_element(By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field = driver.find_element(By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address_field.send_keys(all_addresses[n])
    price_field.send_keys(all_prices[n])
    link_field.send_keys(all_links[n])
    submit_button.click()

    time.sleep(2)
