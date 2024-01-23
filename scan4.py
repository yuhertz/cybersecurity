import requests
import time

# Prompt the user to a website URL or name
url = input("Enter Website URL or Domain Name: ")

# Add 'http://' to the beginning of the URL if it's not already there
if not url.lower().startswith('http'):
    url = 'http://' + url

# The number of requests to send
num_requests = 10

# The time interval between requests (in seconds)
time_interval = 0.1

# Send the requests and measure the time between the responses
start_time = time.time()
for i in range(num_requests):
    response = requests.get(url)
    elapsed_time = time.time() - start_time
    print(f"Request {i+1} took {elapsed_time} seconds")
    time.sleep(time_interval)

# Calculate the average time between requests
average_time = (time.time() - start_time) / num_requests
print(f"Average time between requests: {average_time} seconds")

# Check if the average time between requests is greater than the time interval
if average_time > time_interval:
    print("The website may have rate limiting in place.")
else:
    print("The website does not appear to have rate limiting in place.")
