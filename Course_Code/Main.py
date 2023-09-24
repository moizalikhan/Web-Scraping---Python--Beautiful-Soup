import requests
from bs4 import BeautifulSoup

url = "https://venturebeat.com/ai/how-much-energy-does-ai-use-compared-to-humans-surprising-study-ignites-controversy/"

# request to the server
request_to_server= requests.get(url)
html_Content = request_to_server.content

# parsing
parsed_content = BeautifulSoup(html_Content,'html.parser')
# .prettify for better alignment

# extracting title as bs4.element.tag object
page_tile = parsed_content.title
# extracting comment as bs4.element.comment object
# for string it gives us bs4.element.naigablestring object

# all Paragraphs
all_page_paragraphs = parsed_content.find_all('p')

# first paragraph
first_paragraph = parsed_content.find('p')

# all paragraphs that has lead class
all_paragraphs_class = parsed_content.find_all('p', class_='lead')

# texts from the first paragraph
# .stripped strings
first_page_paragraph_text = parsed_content.find('p').get_text()

#  texts from the all paragraph
all_page_paragraphs_text = parsed_content.find_all('p').get_text()

# all links on the page
# for not repetition of links made a set
links_on_page = parsed_content.find_all('a')

# .children vs .contents
# contents --> tag's children as a list(in memory)
# children --> tag's children as a generator

# for css selectors --> #