from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
import csv

def scrape_data(link, driver):
    driver.get(link)
    data = {}

    try:
        dd_element_1 = driver.find_element(By.CSS_SELECTOR, "#__next > main > section > article > article > div.css-1iz9gs3.ee4wkaf4 > div.css-1gc7po1.ee4wkaf5 > div.css-nyzrx4.ee4wkaf21 > dl:nth-child(1) > dd")
        data['dd_1'] = dd_element_1.text.strip()
    except:
        data['dd_1'] = "Not Found"

    try:
        dd_element_2 = driver.find_element(By.CSS_SELECTOR, "#__next > main > section > article > article > div.css-1iz9gs3.ee4wkaf4 > div.css-1gc7po1.ee4wkaf5 > div.css-nyzrx4.ee4wkaf21 > dl:nth-child(2) > dd")
        data['dd_2'] = dd_element_2.text.strip()
    except:
        data['dd_2'] = "Not Found"

    return data

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

with open("program_movie_links.txt", "r", encoding="utf-8") as file:
    links = [line.strip() for line in file.readlines()]

with open("specific_cast_data_movie.csv", "w", encoding="utf-8", newline="") as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(["Content ID", "감독", "출연"])

    for link in links:
        try:
            content_id = re.search(r"contents/([^/]+)", link)
            content_id = content_id.group(1) if content_id else "Unknown ID"
            print(f"Scraping: {link} (ID: {content_id})")
            data = scrape_data(link, driver)
            csv_writer.writerow([content_id, data['dd_1'], data['dd_2']])
        except Exception as e:
            print(f"Error scraping {link}: {e}")
            continue

driver.quit()
print("Scraped specific data saved to 'specific_cast_data.csv'.")
