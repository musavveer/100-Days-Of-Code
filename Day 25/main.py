import requests
import bs4

def get_html_data(url):
    data = requests.get(url)
    return data

def get_corona_details():
    url = "https://www.mohfw.gov.in/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div",class_ = "col-xs-8 site-stats-count").find("ul").find_all("li")

    for item in info_div:
        text = item.find("strong").get_text()
        count = item.find("span").get_text()
        print(text, " : ", count)

get_corona_details() 