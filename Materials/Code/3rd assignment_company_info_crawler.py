from bs4 import BeautifulSoup
import urllib.request


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


if __name__ == '__main__':
    company_info_url = 'http://www.jobkorea.co.kr/Company/1845948/?C_IDX=5871'
    company_info_soup = get_soup_by_page(company_info_url)
    lable_value_dict = get_lables_and_values(company_info_soup)
    company_name = get_company_name(company_info_soup)

    print(company_name)
    print(lable_value_dict)
