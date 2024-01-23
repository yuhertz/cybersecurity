import requests
import time

def scan_website():
    url = input("Enter Website URL or Domain Name: ")
    if not url.startswith("https://"):
        url = "https://" + url
    print("Scanning...")

    # Loading animation
    animation = "|/-\\"
    idx = 0

    while True:
        print("Scanning... " + animation[idx % len(animation)], end="\r")
        idx += 1
        time.sleep(0.1)

        response = requests.get(url)

        if response.status_code == 200:
            # Analyze the response content for potential bugs
            # You can use regular expressions or specific patterns to identify vulnerabilities

            # Example: Look for SQL injection vulnerabilities
            if 'error' in response.text:
                print("Potential SQL injection vulnerability found!")

            # Example: Check for cross-site scripting (XSS) vulnerabilities
            if '<script>' in response.text:
                print("Potential XSS vulnerability found!")

            break

    print("Scan complete!")

# Usage example:
scan_website()
