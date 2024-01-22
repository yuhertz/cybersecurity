import requests

def view_website_source(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Raise an HTTPError for bad responses (4xx and 5xx status codes)
        response.raise_for_status()

        # Print the HTML source code
        print(response.text)
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    finally:
        # Always close the response object to release resources
        if 'response' in locals():
            response.close()

# Prompt the user to enter the domain name
website_url = input("Enter Website Domain Name: ")

# Ensure the URL starts with 'http://' or 'https://'
if not website_url.startswith('http://') and not website_url.startswith('https://'):
    website_url = 'http://' + website_url

view_website_source(website_url)
