import requests
from bs4 import BeautifulSoup
import json
from setupLog import setupLog
import logging
import re

setupLog()
logger = logging.getLogger('study.webScrapping')

# # Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
# url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# # Send a GET request to the URL
# logger.info(f"Invoke web request for url = {url}")
# response = requests.get(url)

# match response.status_code:
#     case 200:
#         logger.info(f"Status Code = 200")

#         # Parse HTML content
#         soup = BeautifulSoup(response.content, 'html.parser')
#         data = {}

#         # Find all div tag having class = facts-wrapper
#         div = soup.find_all('div', {'class':'facts-wrapper'})
#         for d in div:
#             # For each div tag find all li tags with class list-item
#             lis = d.find_all('li', {'class':'list-item'})
#             dataChild = {}

#             # From the li populate child data dictionary.
#             for li in lis:
#                 dataChild[li.p.text] = li.span.text
            
#             # Populate final data dictionary
#             data[d.h5.text] = dataChild

#         # Write data in json file
#         logger.info(f"Opening json file in write mode.")
#         with open("./data/boston-university-facts-stats.json", 'wt', encoding='utf-8') as file:
#             logger.info(f"Dumping data in json file.")
#             json.dump(data, file, indent=4)
#             logger.info(f"Data writing to json file successfully.")

#         # Read data from json file and write into logs.
#         with open("./data/boston-university-facts-stats.json", 'r') as file:
#             logger.info(f"Data => \n{file.read()}")
#     case 404:
#         logger.info(f"Status Code = 404")

# Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

res = requests.get(url)

match res.status_code:
    case 200:
        # Parse HTML content
        soup = BeautifulSoup(res.content, 'html.parser')

        # get table from the HTML page
        table = soup.find('table')
        pdata = []

        # find all rows of the table and iterate from 2nd row. First row is header.
        for tr in table.find_all('tr')[1:]:
            td = tr.find_all('td')              # find all columns
            pimg = td[0].find('img')['src']     # Get image
            pname = td[1].get_text(strip=True)  # Get Name
            pterm = td[2].get_text(strip=True)  # Get Term
            pparty = td[4].get_text(strip=True) # Get Party
            pelec = td[5].get_text(strip=True)  # Get Election
            pvp = td[6].get_text(strip=True)    # get Vice Precident

            pt = re.findall(r'\b\w+\b', pname)
            pname = " ".join(pt[:2])            # Previously pname has name and bday. Get only name
            pdb = "-".join(pt[2:4])             # Get bday and dday.
            pt = re.findall(r'\d{4}',pelec)     # format election years
            pelec = "-".join(pt)
            pt = re.findall(r'\b\w+\b', pvp)    # format VP name.
            pvp = " ".join(pt[:-1])
            pdata.append({                      # Add the data in pdata
                "Name" : pname,
                "Birth-Death": pdb,
                "Term": pterm,
                "Party": pparty,
                "Election": pelec,
                "VP": pvp,
                "Image": pimg
                })

        # Create president data json file.
        with open('./data/president_data.json', 'wt') as file:
            json.dump(pdata, file, indent=4)
    case 404:
        logger.info("Page Not Found.")