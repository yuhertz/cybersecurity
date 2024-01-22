import requests
import time

# Assuming color_code is a dictionary mapping status codes to color codes
color_code = {200: "\033[92m", 404: "\033[91m", 500: "\033[91m"}

def display_status(response):
    status = f"{color_code.get(response.status_code, '')}Status: [{response.status_code}]\033[0m"
    print(status)

def get_website_status(url):
    try:
        for _ in range(40):  # Adjust the range for the desired number of iterations
            response = requests.get(url)
            display_status(response)
            time.sleep(0.002)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Take the website domain as input
website_input = input("Enter Website URL or Domain Name: ")

# Check if the input contains 'https://', if not, add it
if not website_input.startswith("http://") and not website_input.startswith("https://"):
    url = f"https://{website_input}"
else:
    url = website_input

get_website_status(url)
