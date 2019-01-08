from bs4 import BeautifulSoup
import urllib.request
import csv


def get_soup(page):
    soup = BeautifulSoup(page, "lxml")
    return soup

def get_page(url):
    response = urllib.request.urlopen(url)
    page = response.read().decode(response.headers.get_content_charset())
    return page

def get_soup_by_page(url):
    page = get_page(url)
    company_info_soup = get_soup(page)
    return company_info_soup

def get_company_name(company_info_soup):
    name_container = company_info_soup.find("div", class_="company-header-branding-body")
    company_name = name_container.find("div", class_="name").get_text()
    return company_name

def get_information_container(company_info_soup):
    info = company_info_soup.find("div", class_="table-basic-infomation-primary")
    return info

def get_company_info_lables(info):
    lables = info.find_all("div", class_="field-label")
    print(lables[0].get_text())
    lable_list = []
    return lable_list

def get_company_info_values(info):
    values = info.find_all("div", class_="value")
    value_list = []
    return value_list

def get_lables_and_values(company_info_soup):
    info = get_information_container(company_info_soup)
    lable_list = get_company_info_lables(info)
    value_list = get_company_info_values(info)
    lable_value_dict = {}
    return lable_value_dict

def get_spec(spec_info_soup):
    speclist = spec_info_soup.find('div', class_='specListWrap')
    specitems = speclist.find_all('div', class_='item')
    for spec in specitems:
        item = spec.find('strong', class_='tit').get_text().split("   ")
        item_name = item[0].strip()
        item_percent = item[-1].replace(" 보유\n", " ").strip()
        average_item_score = spec.find('span', class_='score').get_text().strip()
        print(item_name, item_percent, average_item_score)
    return

def save(dict):
    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})


if __name__ == '__main__':
    company_info_basis = 'http://www.jobkorea.co.kr/Company/'
    company_number = '1845948/'
    target_company_url = company_info_basis + company_number
    company_info_soup = get_soup_by_page(target_company_url)
    lable_value_dict = get_lables_and_values(company_info_soup)
    company_name = get_company_name(company_info_soup)

    spec_info_url = f'{target_company_url}PassAvgSpec'

    spec_info_soup = get_soup_by_page(spec_info_url)
    get_spec(spec_info_soup)
    save(lable_value_dict)
