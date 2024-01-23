import socket

def scan_port(port):
    # Create a new socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a timeout value to avoid hanging on unresponsive ports
    sock.settimeout(1)
    
    # Attempt to connect to the specified port
    result = sock.connect_ex((target_ip, port))
    
    # Close the socket
    sock.close()
    
    # Return the result (0 if the port is open, otherwise an error code)
    return result == 0

# Get the user input for the website URL or domain name
url = input("Enter Website URL or Domain Name: ")

# Remove "https:" from the input if it exists
if url.startswith("https:"):
    url = url[8:]

# Resolve the hostname or domain name to an IP address
target_ip = socket.gethostbyname(url)

# A list of common ports to check
common_ports = [80, 443, 8080, 8443]

# Check each port in the list
for port in common_ports:
    if scan_port(port):
        print(f"Port {port} is open, there is a higher risk of DDoS attack.")
