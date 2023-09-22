import requests
from bs4 import BeautifulSoup

# Define the URL to parse
url = "https://uok.edu.pk/faculties/computerscience/bsseout.php"

# Make a request to the server
response = requests.get(url)

# Get the HTML content of the page
html = response.text

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all <p> elements containing course information
course_elements = soup.find_all('p')

# Define the name of the output file
output_file_name = "course_information.txt"

# Open the file in write mode and write the course information
with open(output_file_name, 'w', encoding='utf-8') as output_file:
    for element in course_elements:
        output_file.write(element.text + '\n')

print(f"Course information saved to {output_file_name}")

