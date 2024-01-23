import requests
import time

def check_website_security():
    url = input("Enter Website URL or Domain Name: ")
    
    # Add 'https://' if it's missing
    if not url.startswith("https://") and not url.startswith("http://"):
        url = "https://" + url

    # Check if the website is using HTTPS
    if not url.startswith("https://"):
        print("Warning: The website is not using HTTPS. Consider enabling SSL/TLS.")

    # Check for HTTP security headers
    response = requests.head(url)
    headers = response.headers

    # Scanning animation
    print("Scanning", end="")
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

    # Check for Content Security Policy (CSP) header
    if "Content-Security-Policy" not in headers:
        print("Warning: Content-Security-Policy header is missing. Consider implementing a CSP.")

    # Check for X-Content-Type-Options header
    if "X-Content-Type-Options" not in headers:
        print("Warning: X-Content-Type-Options header is missing. Consider enabling it.")

    # Check for X-Frame-Options header
    if "X-Frame-Options" not in headers:
        print("Warning: X-Frame-Options header is missing. Consider enabling it.")

    # Check for X-XSS-Protection header
    if "X-XSS-Protection" not in headers:
        print("Warning: X-XSS-Protection header is missing. Consider enabling it.")

    # Check for Strict Transport Security (HSTS) header
    if "Strict-Transport-Security" not in headers:
        print("Warning: Strict-Transport-Security header is missing. Consider enabling it.")

    # You can add more security checks as per your requirements

# Example usage
check_website_security()
