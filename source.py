import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urlparse

# Prompt the user to enter the website URL
url = input('Enter website URL or Domain Name: ')

# Parse the URL to get the domain name and the full URL
parsed_url = urlparse(url)
domain_name = parsed_url.netloc
full_url = parsed_url.geturl()

if not url.startswith('http'):
  url = 'https://' + url

# Make a request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links that end with '.html', '.css', or '.txt'
text_files = soup.find_all('a', href=re.compile(r'\.(html|css|txt)$'))

# Print the links and ask the user to choose a file
for i, text_file in enumerate(text_files):
    print(f'{i+1}. {text_file["href"]}')


file_num = int(input('Enter the number of the file you want to access: '))


# Construct the file URL
file_url = url + text_files[file_num-1]['href']

# Make a request to the file URL
file_response = requests.get(file_url)

# Check if the file is a text file
if file_url.endswith(('.html', '.css', '.txt')):
    # Print the file content to the terminal
    print(file_response.text)
else:
    print('The chosen file is not a text file.')
