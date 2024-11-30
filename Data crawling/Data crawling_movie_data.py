import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re

# Scrape specific information from a single link
def scrape_data(link, driver):
    driver.get(link)
    data = {}
    try:
        img_element = driver.find_element(By.CSS_SELECTOR, "#__next > main > section > article > article > div.css-1iz9gs3.ee4wkaf4 > div.css-eabzdp.ee4wkaf12 > picture > img")
        data['image'] = img_element.get_attribute("src")
        data['title'] = img_element.get_attribute("alt")
    except:
        data['image'] = data['title'] = "null"

    try:
        div_element = driver.find_element(By.CSS_SELECTOR, "#__next > main > section > article > article > div.css-1iz9gs3.ee4wkaf4 > div.css-1gc7po1.ee4wkaf5 > div.css-220vpb.ee4wkaf16 > div")
        contents_info = div_element.text.strip().split("\n")
        data['date'] = contents_info[0] if len(contents_info) > 0 else ""
        data['category'] = contents_info[1] if len(contents_info) > 1 else ""
        data['blank'] = contents_info[2] if len(contents_info) > 2 else ""
        data['network'] = contents_info[3] if len(contents_info) > 3 else ""
    except:
        data['date'] = data['category'] = data['network'] = data['blank'] = "null"

    try:
        age_element = driver.find_element(By.CSS_SELECTOR, "#__next > main > section > article > article > div.css-1iz9gs3.ee4wkaf4 > div.css-1gc7po1.ee4wkaf5 > div.css-220vpb.ee4wkaf16 > div > div.tag.tag-age")
        age_class = age_element.get_attribute("class")
        match = re.search(r"tag-age-cmmg-([a-z]+)", age_class)
        data['age_restriction'] = match.group(1).capitalize() if match else ""
    except:
        data['age_restriction'] = "null"

    try:
        p_element = driver.find_element(By.CSS_SELECTOR, "#__next > main > section > article > article > div.css-1iz9gs3.ee4wkaf4 > div.css-1gc7po1.ee4wkaf5 > p")
        data['paragraph'] = p_element.text.strip()
    except:
        data['paragraph'] = "null"

    return data

# Start Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Read links from 'program_links.txt'
with open("program_movie_links.txt", "r", encoding="utf-8") as file:
    links = [line.strip() for line in file.readlines()]

# Open files to save scraped data
with open("specific_movie_data.csv", "w", newline="", encoding="utf-8") as csv_file, \
     open("specific_movie_data.txt", "w", encoding="utf-8") as text_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["content_id", "content_name", "img_url", "limit_age", "company_name", "production_date", "url", "Category", "introduction"])

    for link in links:
        try:
            content_id = re.search(r"contents/([^/]+)", link)
            content_id = content_id.group(1) if content_id else ""

            print(f"Scraping: {link} (ID: {content_id})")
            data = scrape_data(link, driver)

            # Write to CSV
            csv_writer.writerow([
                content_id,
                data['title'],
                data['image'],
                data['age_restriction'],
                data['blank'],
                data['network'],
                data['date'],
                link,
                data['category'],
                data['paragraph']
            ])

            # Write to text file
            text_file.write(f"Content ID: {content_id}\n")
            text_file.write(f"Content Name: {data['title']}\n")
            text_file.write(f"Image URL: {data['image']}\n")
            text_file.write(f"Age Restriction: {data['age_restriction']}\n")
            text_file.write(f"blank: {data['blank']}\n")
            text_file.write(f"Company Name: {data['network']}\n")
            text_file.write(f"Production Date: {data['date']}\n")
            text_file.write(f"URL: {link}\n")
            text_file.write(f"Category: {data['category']}\n")
            text_file.write(f"Introduction: {data['paragraph']}\n")
            text_file.write("\n" + "="*50 + "\n\n")
        except Exception as e:
            print(f"Error scraping {link}: {e}")
            continue

# Close the driver
driver.quit()
print("Scraped specific data saved to 'specific_movie_data.csv' and 'specific_movie_data.txt'.")
