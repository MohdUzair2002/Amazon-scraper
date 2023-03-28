import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
url='https://www.amazon.com/dp/B08FCGH2RL?ref_=cm_sw_r_cp_ud_dp_PR2VH0HS473CK253J7E0'
webpage=requests.get(url,headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")

# Outer Tag Object
title = soup.find("span", attrs={"id":'productTitle'})

# Inner NavigableString Object
title_value = title.string

# Title as a string value
title_string = title_value.strip()

# Printing types of values for efficient understanding
print(type(title))
print(type(title_value))
print(type(title_string))
print()

# Printing Product Title
print("Product Title = ", title_string)


price = soup.find("span", attrs={'class':'a-offscreen'}).string.strip()

print(price)
