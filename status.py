import requests

# Assuming color_code is a dictionary mapping status codes to color codes
color_code = {200: "\033[92m", 404: "\033[91m", 500: "\033[91m"}

def display_status(response):
    status = (
        f"{color_code.get(response.status_code, '')}Status: [{response.status_code}]\033[0m"
    )
    print(status)

def get_website_status(url):
    try:
        response = requests.get(url)
        display_status(response)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Take the website domain as input
website_domain = input("Enter Website Domain Name: ")
url = f"http://{website_domain}"  # Assuming http:// for simplicity, adjust as needed
get_website_status(url)
