import requests
import time
import socket

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

# Extract the domain name from the URL
domain_name = url.split("/")[2]

def scan_port(port):
    # Create a new socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set a timeout value to avoid hanging on unresponsive ports
    sock.settimeout(1)

    # Attempt to connect to the specified port
    result = sock.connect_ex((domain_name, port))

    # Close the socket
    sock.close()

    # Return the result (0 if the port is open, otherwise an error code)
    return result == 0

target_ip = socket.gethostbyname(domain_name)

# A list of common ports to check
common_ports = [80, 443, 8080, 8443]

# Check each port in the list
for port in common_ports:
    if scan_port(port):
        print(f"Port {port} is open, there is a higher risk of DDoS attack.")

print("Scan complete!")
