import requests
from bs4 import BeautifulSoup as BS

# For regex matching
import re

# For downloading mp4
from urllib.request import urlretrieve

# URL for a TED talk
url = "https://www.ted.com/talks/ashley_m_grice_the_power_of_purpose_in_business"

# sending a GET request and storing the response received
r = requests.get(url)

# Semantic helper for user to inform about the download
print("Starting download of the requested video...")

soup = BS(r.content, features="html.parser")

for val in soup.findAll("script"):
    if re.search("id=\"__NEXT_DATA__\"", str(val)):
        result = str(val)

result_mp4 = re.search(r'(https://[\d\w./-]+.mp4)', result).group()

file_name = url[26:] + ".mp4"
print("\nDownload URL: " + result_mp4)

# Downloading the file
urlretrieve(result_mp4, filename=file_name)

print("\nDownload finished!")