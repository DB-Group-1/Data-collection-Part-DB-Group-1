from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Start Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the webpage: url by category
driver.get("https://www.tving.com/more/band/HM159988")

# Simulate scrolling to load content
for _ in range(5):  # Adjust number of scrolls depending on how much content you need to load
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for content to load after each scroll

# Open a file to write the program links
with open("program_links.txt", "w", encoding="utf-8") as file:
    # Iterate through 1 to 250 for div:nth-child(X)
    for i in range(1, 251):  # Adjust the range as needed
        selector = f"#__next > main > section > div:nth-child(2) > section > div > div:nth-child({i}) > a"
        try:
            link_element = driver.find_element(By.CSS_SELECTOR, selector)
            href = link_element.get_attribute("href")  # Extract the 'href' attribute
            if href:  # Check if href exists
                file.write(href + "\n")  # Write each link to the file, with a newline
        except Exception as e:
            # Skip if no element is found for the selector
            continue

# Close the driver after scraping
driver.quit()

print("Program links saved to 'movie_links.txt'.")
