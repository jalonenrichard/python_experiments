from bs4 import BeautifulSoup

with open('delfi.html','r') as f:
    html_string = f.read()

def is_not_blank(s):
    return bool(s and s.strip())

soup = BeautifulSoup(html_string, 'html.parser')
for headline in soup.find_all('a'):
    if is_not_blank(headline.get_text()):
        print(headline.get_text())

