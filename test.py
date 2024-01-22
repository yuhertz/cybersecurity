from selenium import webdriver

def test_website(url):
    # Create a new instance of the Firefox driver (you can use other browsers as well)
    driver = webdriver.Firefox()

    try:
        # Open the website
        driver.get(url)

        # Example: Check if the title of the webpage is as expected
        expected_title = "Your Expected Title"
        actual_title = driver.title

        assert expected_title in actual_title, f"Title mismatch! Expected: {expected_title}, Actual: {actual_title}"

        # Example: Check if a specific element is present on the webpage
        # Replace 'your_element_locator' with the actual locator of the element you want to check
        # You can inspect elements in your browser to find their locators
        assert driver.find_element_by_css_selector('your_element_locator').is_displayed(), "Element not found!"

        # You can add more tests based on your requirements

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser window
        driver.quit()

# Take user input for the website domain name
website_domain = input("Enter Website Domain Name: ")

# Construct the complete URL
url = f"https://{website_domain}"

# Call the test_website function with the provided URL
test_website(url)
