from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Initialize Chrome WebDriver
# Replace with your Chrome WebDriver path
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Instagram login function


def instagram_login(username, password):
    driver.get("https://www.instagram.com/")
    time.sleep(3)

    # Enter username
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys(username)
    time.sleep(1)

    # Enter password
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(password)
    time.sleep(1)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)


# Example usage
instagram_login("your_username", "your_password")

# Function to like posts by hashtag


def like_posts_by_hashtag(hashtag, max_likes=10):
    driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
    time.sleep(3)

    # Click on the first post
    driver.find_element(By.CLASS_NAME, "_9AhH0").click()
    time.sleep(2)

    for i in range(max_likes):
        try:
            # Click the 'like' button
            like_button = driver.find_element(
                By.XPATH, '//button[@class="wpO6b "]/*[name()="svg" and @aria-label="Like"]')
            like_button.click()
            time.sleep(2)

            # Move to the next post
            next_button = driver.find_element(
                By.XPATH, '//a[contains(@class, "_65Bje")]')
            next_button.click()
            time.sleep(2 + i % 3)  # Random delay for human-like behavior
        except Exception as e:
            print(f"Error occurred: {e}")
            break


# Use the function to start liking posts
like_posts_by_hashtag("pythonprogramming")
