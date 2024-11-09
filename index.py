import time
import random
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import gspread
from google.oauth2.service_account import Credentials

# set up selenium

driver = webdriver.Chrome()
# Set up Google Sheets API credentials
SCOPES = ['https://www.googleapis.com/auth/documents',
          'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file(
    "path_to_your_service_account.json", scopes=SCOPES)
gc = gspread.authorize(creds)

# Document ID for your Google Doc
DOCUMENT_ID = "1TIhk0WLWEgb0nIfxvSLRi5yeKDIj7YHKTL6lwnth75I"

# Function to log into Instagram


def instagram_login(username, Mandem123):
    driver.get("https://www.instagram.com/")
    time.sleep(3)

    # Enter username
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys(workstudyple)
    time.sleep(1)

    # Enter password
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(Mandem123)
    time.sleep(1)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

# Function to like posts by hashtag and collect usernames


def like_posts_by_hashtag(hashtag, max_likes=10):
    driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
    time.sleep(3)

    driver.find_element(By.CLASS_NAME, "_9AhH0").click()
    time.sleep(2)
    liked_users = []

    for i in range(max_likes):
        try:
            # Like post
            like_button = driver.find_element(
                By.XPATH, '//button[@class="wpO6b "]/*[name()="svg" and @aria-label="Like"]')
            like_button.click()
            time.sleep(2)

            # Get username
            username = driver.find_element(
                By.XPATH, "//a[contains(@class, 'FPmhX')]").text
            liked_users.append(username)

            # Move to the next post
            next_button = driver.find_element(
                By.XPATH, '//a[contains(@class, "_65Bje")]')
            next_button.click()
            # Random delay for human-like behavior
            time.sleep(2 + random.randint(1, 3))

        except Exception as e:
            print(f"Error: {e}")
            break
    return liked_users

# Function to add liked usernames to Google Doc


def update_google_doc(usernames):
    document = gc.open_by_key(DOCUMENT_ID)
    doc_content = document.get_all_records()

    # Append date and usernames to the document
    date_str = datetime.now().strftime("%Y-%m-%d")
    for username in usernames:
        doc_content.append([date_str, username])

    # Save updates to the document
    document.update(doc_content)


# Run bot and update Google Doc
instagram_login("your_username", "your_password")
liked_usernames = like_posts_by_hashtag("pythonprogramming", max_likes=5)
update_google_doc(liked_usernames)

# Close the browser when done
driver.quit()
