import requests

def view_website_source(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the HTML source code
            print(response.text)
        else:
            print(f"Failed to retrieve the website. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user to enter the domain name
website_url = input("Enter Website Domain Name: ")

# Ensure the URL starts with 'http://' or 'https://'
if not website_url.startswith('http://') and not website_url.startswith('https://'):
    website_url = 'http://' + website_url

view_website_source(website_url)
