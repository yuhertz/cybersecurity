import requests
import socket

def scan_website():
    # Prompt the user to enter a website URL or domain name
    url = input("Enter Website URL or Domain Name: ")
    
    # Check if the URL does not start with "https://"
    if not url.startswith("https://"):
        # If not, prepend "https://" to the URL
        url = "https://" + url
    
    # Print a message indicating the scanning process has begun
    print("Scanning...")

    # Extract the domain name from the URL
    domain_name = url.split("/")[2]

    # Define a function to scan a specific port
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

    # Obtain the target IP address from the domain name
    target_ip = socket.gethostbyname(domain_name)

    # A list of common ports to check
    common_ports = [80, 443, 8080, 8443]

    # Check each port in the list
    for port in common_ports:
        # Call the scan_port function to check if the port is open
        if scan_port(port):
            print(f"Port {port} is open, there is a higher risk of DDoS attack!")

    try:
        # Check for rate limits by sending an HTTP GET request to the website
        response = requests.get(url)
        rate_limit_status = False
        
        # Check if the response status code indicates a rate limit
        if response.status_code >= 429:
            print(f"Website {url} has a rate limit! Current status code: {response.status_code}")
            rate_limit_status = True
        # Check if rate limit headers are present in the response
        elif response.headers.get("X-RateLimit-Limit"):
            print(f"Website {url} has a rate limit of {response.headers['X-RateLimit-Limit']} requests per {response.headers['X-RateLimit-Interval']} seconds")
            rate_limit_status = True
        # If no rate limit information is found in the response headers
        else:
            print("Website does not have a rate limit, higher risk of DDoS attack")
    # Handle any potential exceptions that occur during the request
    except requests.RequestException as e:
        print(f"An error occurred while attempting to fetch {url}: {e}")
        rate_limit_status = False

    # Print a message indicating that the scan has finished
    print("Scan finished.")

# Call the scan_website function to start the scanning process
scan_website()
