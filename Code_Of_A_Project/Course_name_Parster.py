# Import the necessary libraries
import requests
from bs4 import BeautifulSoup

# Define the URL to parse
url = "https://uok.edu.pk/faculties/computerscience/bs.php"

# Make a request to the server
request_to_server = requests.get(url)

# Get the content of the response
Content = request_to_server.content

# Create a BeautifulSoup object from the content
Alligned_Content = BeautifulSoup(Content, 'html.parser')

# Find all rows in the table
rows = Alligned_Content.find_all('tr')

# Create a list to store the course titles
course_titles = []

# Iterate over the rows and extract the course titles
for row in rows:
    # Find all columns in the row
    columns = row.find_all('td')

    # Check if the row has at least 4 columns
    if len(columns) >= 4:
        # Extract the course title from the second column
        course_title = columns[1].text.strip()

        # Add the course title to the list
        course_titles.append(course_title)

# Define the name of the output file
output_file_name = "course_titles.txt"

# Open the file in write mode and write the course titles
with open(output_file_name, 'w', encoding='utf-8') as output_file:
    for title in course_titles:
        output_file.write(title + '\n')

print(f"Course titles saved to {output_file_name}")