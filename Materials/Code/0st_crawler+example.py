import os.path
import time
import json
from bs4 import BeautifulSoup
import netnew_excel as nn
from collections import OrderedDict, defaultdict
import numpy as np
import pandas as pd
import collections
import datetime
import os

from selenium import webdriver
from selenium.webdriver.ie.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys

class JsonDump:
    def __init__(self):
        dir = os.path.dirname(os.path.abspath(__file__))
        jsonfile = dir + r'\\asset\\static\\login_infomation.json'
        with open(jsonfile) as f:
            login_data = json.load(f)
        self.login_data = login_data

    def get_login_info(self):
        self.id = self.login_data['ID']
        self.password = self.login_data['Password']

    def get_MU_info(self):
        muinfo = {'MU' : self.login_data['MU'],
                  'Countrycode' : self.login_data['Countrycode'],
                  'inumber' : self.login_data['inumber']}
        return muinfo

class SelDriver(JsonDump):
    def __init__(self):
        super(SelDriver, self).__init__()
        opts = Options()
        opts.ignore_protected_mode_settings = True
        opts.ignore_zoom_level = True
        dir = os.path.dirname(os.path.abspath(__file__))
        # path = dir + r'\\asset\\selenium\\IEDriverServer.exe'
        # self.driver = webdriver.Ie(executable_path=path, ie_options=opts)

        path = dir + r'\\asset\\selenium\\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=path, chrome_options=opts)
        self.access()
        self.login()

    def control(self):
        return self.driver

    def access(self):
        pageurl = input("pageurl")
        self.driver.get(pageurl)

    def put_id(self):
        self.driver.find_element_by_name('lgnuid').click()
        self.driver.find_element_by_name('lgnuid').send_keys(self.id)

    def put_password(self):
        self.driver.find_element_by_class_name('pwType').click()
        self.driver.find_element_by_class_name('pwType').send_keys(self.password)

    def login(self):
        self.get_login_info()
        try:
            try:
                self.driver.find_element_by_class_name('btn_ico_close').click()
            except:
                pass
            print('****LOGIN****')
            self.put_id()

            self.put_password()
            self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div/fieldset/a').click()
        except Exception as e:
            print(e)
            try:
                time.sleep(1)
                self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div/fieldset/a').click()
            except:
                print('Please check Log-in Status')
                input("Looks like already Logged in, or please Log-in my yourself, then press any key")

class SearchAndFind:
    def __init__(self, driver, search_object):
        self.driver = driver
        if type(search_object) == list:
            self.search_term = search_object[0]
            self.orgid = search_object[1]
        else:
            self.search_term = search_object
            self.orgid = np.nan
        original_search_term = self.search_term

        self.put_searchterm_and_get_search_page()
        last = self.is_there_company()
        if last == 0:
            self.search_term = 'Fail|' + str(original_search_term)


    def get_soup(self, page_source):
        return BeautifulSoup(page_source, "lxml")

    def put_searchterm(self):
        self.driver.find_element_by_id('q').clear()
        self.driver.find_element_by_id('q').send_keys(self.search_term)
        self.driver.find_element_by_id('searchView').click()
        self.search_page = self.driver.page_source

    def put_searchterm_and_get_search_page(self):
        try:
            self.put_searchterm()
        except:
            try:
                time.sleep(1)
                self.search_term = input("You typed Wrong Search Term! Please input other Search Term twice!   ")
                time.sleep(2)
                self.search_term = input("Once more! This gonna search!!   ")
                self.put_searchterm()
            except:
                print("bye")


    def is_there_company(self):
        soup = self.get_soup(self.search_page)
        table = soup.find(id="eprTable")
        search_row = table.find_all('tr')
        length = len(search_row)
        if (length == 2):
            a = table.find_all("tr", class_="last")
            if len(a) != 0:
                print("Only 1 Company Found. Coutinue to process")
                self.driver.find_element_by_id('eprTable').find_elements_by_name('overViewOpen')[0].click()
                return
            else:
                try:
                    print("NOTTING.")
                    a = input("Please check your SEARCHTERM, If you want to leave it blank, Press 0")
                    b = input("Then, Press any key >>>>>        ")
                    if a == '0' or b == '0':
                        return 0
                except:
                    try:
                        return 0
                    except:
                        raise
        else:
            try:
                a = input("More than 1 Companies found. Please check & open Overview page, and Press any key       :")
                a = input("Please Press any key once more, for prevent error!     :")
            except:
                try:
                    return 0
                except:
                    raise

class GiveMeInfo(SearchAndFind):
    def __init__(self, driver, search_object):
        super().__init__(driver, search_object)

    def instant_ramen(self):
        self.get_overview_info()

    def japan_ramen(self):
        if self.search_term[0:5] != 'Fail|':
            self.get_overview_info()
            self.driver.find_element_by_class_name("lnb").find_elements_by_tag_name("ul")[1].click()
            self.driver.find_element_by_class_name("lnb").find_elements_by_tag_name("ul")[1].click()
            self.kor_page_source = self.driver.page_source
            self.driver.find_element_by_id("langTsm").click()  # 영어페이지 클릭
            self.eng_page_source = self.driver.page_source
            self.get_info_from_both_page()
        else:
            self.assign_empty()

    def solo(self):
        self.japan_ramen()
        return self

    def juju_club(self):
        self.japan_ramen()
        self.click_grouptab()
        self.analysis_group_table()
        return self


    def assign_empty(self):
        self.company_name_eng = np.nan
        self.company_name_kor = np.nan
        self.kor_group_main_company = np.nan
        self.groupname_eng = np.nan
        self.companytype = np.nan
        self.address_kor = np.nan
        self.eng_add_1 = np.nan
        self.eng_add_2 = np.nan
        self.eng_add_3 = np.nan
        self.youngnam = np.nan
        self.postcode = np.nan
        self.phonenumber = np.nan
        self.fax_number = np.nan
        self.homepage = np.nan
        self.taxnumber = np.nan
        self.kscode = np.nan
        self.kscode_kor = np.nan
        self.kscode_eng = np.nan
        self.moneydict = {2016 : np.nan, 2017 : np.nan}
        self.number_of_employee = np.nan
        self.year_of_employee = np.nan
        self.ceo_name_eng_last = np.nan
        self.ceo_name_eng_first = np.nan
        self.ceo_name_kor = np.nan
        self.companystatus = np.nan
        return


    def get_overview_info(self):
        self.overview_page = self.driver.page_source
        soup = self.get_soup(self.overview_page)
        # 첫번째 테이블 선택
        basic_info_table = soup.find_all("tbody")[0]
        basic_info_table_row = basic_info_table.find_all("tr")

        # KISCODE Handle
        self.kiscode = basic_info_table_row[0].find("td").get_text().split(")", -1)[-2].split("(", -1)[-1]

        #이름 Handle
        self.company_name_kor = basic_info_table_row[0].find("td").get_text().rsplit("(", 1)[0].strip()

        #사업자등록번호 Handle
        taxnumber = basic_info_table_row[3].find('td').get_text().strip()
        if taxnumber == "-":
            self.taxnumber = "N/A"
        else:
            self.taxnumber = int(taxnumber.replace("-", "").strip())

        #기업 형태 Handle
        self.companytype = basic_info_table_row[5].find('td').get_text().strip()

        #KSCODE Handle
        row_kscode = basic_info_table_row[6].find('td').get_text().strip().split(")")
        self.kscode = row_kscode[0].replace("(", "").strip()
        self.kscode_kor = row_kscode[1].strip()
        peopleinfo = basic_info_table_row[8].get_text().strip().split("(")
        
        try:
            if ("-" in peopleinfo) or (len(peopleinfo) == 0):
                raise
            else:
                self.number_of_employee = int(peopleinfo[0].split("\n")[1].strip().split("명")[0].strip())
                self.year_of_employee = int(peopleinfo[1].strip().split("년")[0])
        except:
            self.number_of_employee = "N/A"
            self.year_of_employee = "N/A"

        #휴폐업상태 Handle
        if "폐업" in self.companytype:
            self.companystatus = "Inactive"
        elif "피흡수합병" in self.companytype:
            self.companystatus = "Inactive - 피흡수"
        else:
            self.companystatus = "Active"

        # 전화번호 Handle
        try:
            phonenumber = basic_info_table_row[11].find('td').get_text().strip()
            if len(phonenumber) == 0:
                raise
            elif phonenumber == '-':
                raise
            elif phonenumber == 'NULL':
                raise
            else:
                self.phonenumber = phonenumber
        except:
            self.phonenumber = "N/A"


        address_row = basic_info_table_row[12].find('td').get_text()
        # 우편번호 Handle
        self.postcode = address_row.strip().split("\n")[0].replace("(", "").replace(")", "").zfill(5)

        #주소 Handle
        self.address_kor = address_row.strip().split("\n")[1].strip()

        turnovertable = soup.find_all("tbody")[1]  # 매출액테이블 선택
        moneydict = self.get_moneydict(turnovertable)
        if moneydict == "N/A":
            moneydict = {}
            moneydict[2016], moneydict[2017] = "N/A", "N/A"
        else:
            moneydictyears = sorted(list(moneydict.keys()))
            lastyear = moneydictyears[-1]

            if (2017 in moneydictyears) & (2016 in moneydictyears):
                pass
            elif (2017 in moneydictyears) & (2016 not in moneydictyears):
                moneydict[2016] = "N/A"
            elif (2017 not in moneydictyears) & (2016 in moneydictyears):
                moneydict[2017] = "N/A"
            else:
                moneydict[2016] = str(lastyear) + "년   " + str(moneydict[lastyear])
                moneydict[2017] = "N/A"
        self.moneydict = moneydict

    def get_moneydict(self, turnovertable):
        turnover_row = turnovertable.find_all("tr")
        moneydict = OrderedDict()
        number = 0
        firstyear = turnover_row[0].find_all("td")[0].get_text()[0:4]
        if firstyear == "조회된 ":
            moneydict = "N/A"
        else:
            for i in turnover_row:
                year = int(i.find_all("td")[0].get_text()[0:4])
                try:
                    moneyofyear = int(i.find_all("td")[4].get_text().replace(",", "")) * 1000
                except:
                    moneyofyear = "N/A"
                    print(year + "의 매출액이 없습니다")
                moneydict[year] = moneyofyear
                number = number + 1
        return moneydict

    def get_info_from_both_page(self):
        kor_soup = self.get_soup(self.kor_page_source)
        kor_table = kor_soup.find_all("tbody")
        basic_info = kor_table[0].find_all("tr")

        eng_soup = self.get_soup(self.eng_page_source)
        eng_table = eng_soup.find("tbody")
        eng_basic_info = eng_table.find_all("tr")

        self.company_name_eng = eng_basic_info[0].get_text().strip().split("\n")[-1].strip()


        company_group = basic_info[5].get_text().strip().split("\n")

        if company_group[1] != '-':
            self.kor_group_main_company = company_group[-1].split(")", 1)[-1]
            self.groupname_eng = eng_basic_info[13].get_text().strip().split("\n")[-1].split(")", 1)[-1]
        else:
            self.kor_group_main_company = "N/A"
            self.groupname_eng = "N/A"


        address_eng = eng_basic_info[5].get_text().replace("MAP Land-lot Num.", "").strip().split("\n")[-1].split(" ")

        lastadd = "".join(address_eng[-1])
        try:
            if lastadd in ["Busan", "Seoul", "Ulsan", "Incheon", "Daegu", "Daejeon", "Gwangju", 'Sejong']:
                self.eng_add_1 = " ".join(address_eng)
                self.eng_add_2 = "".join(address_eng[-1])
                self.eng_add_3 = "".join(address_eng[-1])
            else:
                self.eng_add_1 = " ".join(address_eng)
                self.eng_add_2 = "".join(address_eng[-2])
                self.eng_add_3 = "".join(address_eng[-1])

            if lastadd in ["Gyeongbuk", "Busan", "Daegu", "Ulsan", "Gyeongnam"]:
                self.youngnam = "Young Nam"
            else:
                self.youngnam = np.nan
        except:
            print("Someting is wrong with address. Please check it later")
            pass

        faxnumber = eng_basic_info[6].get_text().split("\n")[1].split(":")[2].strip()
        try:
            if len(faxnumber) == 0:
                raise
            else:
                self.fax_number = faxnumber
        except:
            self.fax_number = "N/A"


        homepage = basic_info[15].get_text().split("홈페이지")[-1].strip()
        if homepage == '-' or homepage == 'http://':
            self.homepage = "N/A"
        else:
            self.homepage = homepage

        self.ceo_name_kor = basic_info[1].get_text().strip().split("\n ")[1].strip()
        ceo_name_eng = eng_basic_info[1].get_text().strip().split("\n")[1].split("/")[0]
        if "," in ceo_name_eng:  # 한국인인경우
            self.ceo_name_eng_last = ceo_name_eng.split(",")[0].strip()
            self.ceo_name_eng_first = ceo_name_eng.split(",")[1].strip()
        else:  # 외국인인경우
            self.ceo_name_eng_last = ceo_name_eng.split(" ")[-1].strip()
            self.ceo_name_eng_first = " ".join(ceo_name_eng.split(" ")[0:-1]).strip()

        self.kscode_eng = eng_basic_info[11].get_text().split("\n")[-2].split(")")[-1]

    def click_grouptab(self):
        firstclick = self.driver.find_element_by_class_name("lnb").find_elements_by_tag_name("ul")[2]
        firstclick.click()
        firstclick.find_element_by_tag_name("ul").find_elements_by_tag_name("li")[1].click()

    def analysis_group_table(self):
        group_page = self.driver.page_source
        group_soup = self.get_soup(group_page)
        thead = group_soup.find("thead").find_all("tr")[0].find("th").get_text().strip()

        if thead == "주주명":
            tabletype = 6
        else:
            tabletype = 8

        table = group_soup.find("tbody")
        rowlist = table.find_all("tr")
        temp_list = []

        if tabletype == 8:
            for rows in range(3):
                groupdict = {}
                try:
                    findtd = rowlist[rows * 2].find_all("td")
                    groupdict["name"] = findtd[2].get_text().strip()
                    groupdict["status"] = findtd[6].get_text().strip()
                    groupdict["portion"] = float(findtd[5].get_text().replace("%", "").strip())
                    temp_list.append(groupdict)
                except:
                    groupdict["name"], groupdict["portion"], groupdict["status"] = np.nan, np.nan, np.nan
                    temp_list.append(groupdict)

        elif tabletype == 6:
            for rows in range(3):
                groupdict = {}
                try:
                    findtd = rowlist[rows * 2].find_all("td")
                    groupdict["name"] = findtd[0].get_text().strip()
                    groupdict["status"] = findtd[1].get_text().strip()
                    groupdict["portion"] = float(findtd[6].get_text().replace("%", "").strip())
                    temp_list.append(groupdict)
                except:
                    groupdict["name"], groupdict["portion"], groupdict["status"] = np.nan, np.nan, np.nan
                    temp_list.append(groupdict)
        self.juju = temp_list




class DataFrameOperator:
    def __init__(self, muinfo):
        self.dir = os.path.dirname(os.path.abspath(__file__))
        self.prepare_tax_excel()
        self.check_path()
        self.get_today()
        self.make_dataframe()
        self.mu = muinfo['MU']
        self.countrycode = muinfo['Countrycode']
        self.inumber = muinfo['inumber']

    def prepare_tax_excel(self):
        path = self.dir + r'\\asset\\static\\tax_finder.xlsx'
        taxfile = pd.read_excel(path)
        taxfile["Tax Number"] = taxfile["Tax Number"].apply(lambda x: str(x))
        self.taxfile = taxfile

    def compare_tax(self, taxnumber):
        taxdict = self.taxfile[self.taxfile["Tax Number"] == f'{taxnumber}'].reset_index().T.to_dict()
        try:
            taxlist = []
            for i in range(len(taxdict)):
                print(f"동일한 사업자번호를 가진 BP#  {taxdict[i]['Business Partner']} | {taxdict[i]['Eng_name']} | {taxdict[i]['korea_name']} 가 발견되었습니다.")
                taxlist.append(taxdict[i]['Business Partner'])
            return taxlist

        except:
            pass

    def make_dataframe(self):
        self.maindataframe = pd.DataFrame()

    def concat(self):
        self.maindataframe = pd.concat([self.maindataframe, self.adddataframe])

    def get_today(self):
        self.today = str(datetime.date.today())

    def check_path(self):
        try:
            if not (os.path.isdir("EXCEL")):
                os.makedirs(os.path.join("EXCEL"))
        except OSError as e:
            if e.errno != errno.EEXIST:
                print("Failed to create directory!")
            raise

    def plush_to_excel(self, mode=0):
        now = datetime.datetime.today()
        if mode == 0:
            filename = str(now)[:16].replace(":", "") + ".xlsx"
        elif mode == 1:
            filename = str(now)[:16].replace(":", "") + "_autosave.xlsx"
        filenamewithPath = ".\\EXCEL\\" + filename
        print("File is created at EXCEL folder as " + filename)
        self.maindataframe.to_excel(filenamewithPath, index=False)

    def make_infomation(self, information):
        basic_form = collections.OrderedDict({
            'State of BP# Request': 'In Progress',
            'Campaign Name': information.search_term,
            'Requested Person': np.nan,
            'Request Receive Date\ndd/mm/yyyy': self.today,
            "BP Creation Requested Date\ndd/mm/yyyy": np.nan,
            "BP Creation Completed Date\ndd/mm/yyyy": np.nan,
            'MU': self.mu,
            'BP #\n(Account ID)': information.orgid,
            'Organisation Name - full legal version, no abbreviations or marketing or brand names\n(35 characters)': information.company_name_eng,
            'Organisation Name 2 - continued \n(35 characters)': information.company_name_kor,
            'PE Name_KOR\n(모기업)\n(Data)': information.kor_group_main_company,
            'PE Name_ENG\n(Data)': information.groupname_eng,
            'KOSDAQ\n상장 여부': information.companytype,
            'Street Address\n(Korean)': information.address_kor,
            'Street Address \n(35 characters)': information.eng_add_1,
            "Street Address 2 - continued (information appearing below 'Street Address'\n(35 characters)": np.nan,
            'City': information.eng_add_2,
            'PO Box': np.nan,
            'Postal code for PO Box': np.nan,
            'City of PO Box (if different to Street City)': np.nan,
            'State/Province/Territory': information.eng_add_3,
            'Young Nam province': information.youngnam,
            'Postal Code': information.postcode,
            'Country code ': self.countrycode,
            'Org Telephone Number (no Country code indicator necessary)': information.phonenumber,
            'Org Fax Number (no Country code indicator necessary)': information.fax_number,
            'Website Address': information.homepage,
            'DUNS Number\n(if provided in original data source)': '9999',
            'Pre BP Number\n': np.nan,
            'Business registration, National/Tax ID \n(if DUNS not available)': information.taxnumber,
            'Industry Code (SIC)\n(text name min.)': np.nan,
            'Master Code': np.nan,
            'Master Code Text': np.nan,
            '9차_KS_Code\n(ata)': information.kscode,
            'Industry Description KOR\n(표준산업분류)\n(data)': information.kscode_kor,
            'Industry Description ENG\n(표준산업분류)\n(data)': information.kscode_eng,
            'Local Sales Turnover\n2016 (K won)': information.moneydict[2016],
            'Local Sales Turnover\n2017 (K won)': information.moneydict[2017],
            'EUR Sales Turnover 2016': np.nan,
            'Local Employee Size': information.number_of_employee,
            'Local Employee Size Year': information.year_of_employee,
            'Global Employee Size': np.nan,
            'AE_ID \n(I Number)': np.nan,
            'AE_Last Name': np.nan,
            'AE_First Name': np.nan,
            'Proposed_2018_RBC': 'Net New',
            'Proposed_2018_IAC': 'GB - Lower',
            'Contact Person \nSalutation ': np.nan,
            'Contact Person \nLast Name \n(40 characters)': information.ceo_name_eng_last,
            'Contact Person \nFirst Name \n(40 characters)': information.ceo_name_eng_first,
            'Contact Person Korean Name': information.ceo_name_kor,
            'Contact Email Address\n(40 characters)': np.nan,
            'E-mail Opt-In\n2018 \n(drop-down list)': np.nan,
            'Contact Person \nTelephone Number(no Country code indicator necessary)': information.phonenumber,
            'Contact Person\n Fax Number(no Country code indicator necessary)': np.nan,
            'Contact Person \nMobile Phone Number(no Country code indicator necessary)': np.nan,
            'Contact Person Linkedin \n(URL Link)': np.nan,
            'Miscellaneous Link': np.nan,
            'Job Title \n(free text-60 characters)': 'CEO',
            'Job Title\n(free text/Korean)': '대표이사',
            'Job Function(drop-down list)': 'Chief Exec Officer',
            'Department*\n(drop-down list)': 'Management',
            'Department*\n(free text/Korean)': np.nan,
            'Contact ID\n(from Data Team)': np.nan,
            'CCAP Team Member\n(I-Number)': self.inumber,
            'Company Status': information.companystatus,
            'Contact Status': 'New Contact Discovered',
            'Profile Status': 'Closed',
            'duplicated_tax' : str(information.taxlist)})
        self.adddataframe = pd.DataFrame(basic_form, index=[0])
        self.concat()

    def make_infomation_with_juju(self, information):
        #If you want with juju
        basic_form = collections.OrderedDict({
            'State of BP# Request': 'In Progress',
            'Campaign Name': information.search_term,
            'Requested Person': np.nan,
            'Request Receive Date\ndd/mm/yyyy': self.today,
            "BP Creation Requested Date\ndd/mm/yyyy": np.nan,
            "BP Creation Completed Date\ndd/mm/yyyy": np.nan,
            'MU': self.mu,
            'BP #\n(Account ID)': information.orgid,
            'Organisation Name - full legal version, no abbreviations or marketing or brand names\n(35 characters)': information.company_name_eng,
            'Organisation Name 2 - continued \n(35 characters)': information.company_name_kor,
            'PE Name_KOR\n(모기업)\n(KData)': information.kor_group_main_company,
            'PE Name_ENG\n(Data)': information.groupname_eng,
            'KOSDAQ\n상장 여부': information.companytype,
            'Street Address\n(Korean)': information.address_kor,
            'Street Address \n(35 characters)': information.eng_add_1,
            "Street Address 2 - continued (information appearing below 'Street Address'\n(35 characters)": np.nan,
            'City': information.eng_add_2,
            'PO Box': np.nan,
            'Postal code for PO Box': np.nan,
            'City of PO Box (if different to Street City)': np.nan,
            'State/Province/Territory': information.eng_add_3,
            'Young Nam province': information.youngnam,
            'Postal Code': information.postcode,
            'Country code ': self.countrycode,
            'Org Telephone Number (no Country code indicator necessary)': information.phonenumber,
            'Org Fax Number (no Country code indicator necessary)': information.fax_number,
            'Website Address': information.homepage,
            'DUNS Number\n(if provided in original data source)': '9999',
            'Pre BP Number\n': np.nan,
            'Business registration, National/Tax ID \n(if DUNS not available)': information.taxnumber,
            'Industry Code (SIC)\n(text name min.)': np.nan,
            'Master Code': np.nan,
            'Master Code Text': np.nan,
            '9차_KS_Code\n( data)': information.kscode,
            'Industry Description KOR\n(표준산업분류)\n( data)': information.kscode_kor,
            'Industry Description ENG\n(표준산업분류)\n( data)': information.kscode_eng,
            'Local Sales Turnover\n2016 (K won)': information.moneydict[2016],
            'Local Sales Turnover\n2017 (K won)': information.moneydict[2017],
            'EUR Sales Turnover 2016': np.nan,
            'Local Employee Size': information.number_of_employee,
            'Local Employee Size Year': information.year_of_employee,
            'Global Employee Size': np.nan,
            'AE_ID \n(I Number)': np.nan,
            'AE_Last Name': np.nan,
            'AE_First Name': np.nan,
            'Proposed_2018_RBC': 'Net New',
            'Proposed_2018_IAC': 'GB - Lower',
            'Contact Person \nSalutation ': np.nan,
            'Contact Person \nLast Name \n(40 characters)': information.ceo_name_eng_last,
            'Contact Person \nFirst Name \n(40 characters)': information.ceo_name_eng_first,
            'Contact Person Korean Name': information.ceo_name_kor,
            'Contact Email Address\n(40 characters)': np.nan,
            'E-mail Opt-In\n2018 \n(drop-down list)': np.nan,
            'Contact Person \nTelephone Number(no Country code indicator necessary)': information.phonenumber,
            'Contact Person\n Fax Number(no Country code indicator necessary)': np.nan,
            'Contact Person \nMobile Phone Number(no Country code indicator necessary)': np.nan,
            'Contact Person Linkedin \n(URL Link)': np.nan,
            'Miscellaneous Link': np.nan,
            'Job Title \n(free text-60 characters)': 'CEO',
            'Job Title\n(free text/Korean)': '대표이사',
            'Job Function(drop-down list)': 'Chief Exec Officer',
            'Department*\n(drop-down list)': 'Management',
            'Department*\n(free text/Korean)': np.nan,
            'Contact ID\n(from Data Team)': np.nan,
            'CCAP Team Member\n(I-Number)': self.inumber,
            'Company Status': information.companystatus,
            'Contact Status': 'New Contact Discovered',
            'Profile Status': 'Closed',
            'duplicated_tax': str(information.taxlist),
            '1st JUJU': information.juju[0]['name'],
            '1st status': information.juju[0]['status'],
            '1st Portion': information.juju[0]['portion'],
            '2nd JUJU': information.juju[1]['name'],
            '2nd status': information.juju[1]['status'],
            '2nd Portion': information.juju[1]['portion'],
            '3rd JUJU': information.juju[2]['name'],
            '3rd status': information.juju[2]['status'],
            '3rd Portion': information.juju[2]['portion']
        })
        self.adddataframe = pd.DataFrame(basic_form, index=[0])
        self.concat()


def massive_search():
    #ready for massive_search.
    path = '.\\asset\\static\\massive.xlsx'
    searchfile = pd.read_excel(path)
    search_data = searchfile.columns[0]
    org_data = searchfile.columns[1]
    searchfile[search_data] = searchfile[search_data].apply(lambda x: str(x).replace(".0", ""))
    searchfile[org_data] = searchfile[org_data].apply(lambda x: str(x).replace(".0", "")).fillna(-9999)
    info_additional = []
    info_len = len(searchfile.columns)
    for i in range(info_len):
        if i == 0:
            pass
        else:
            if searchfile[searchfile.columns[i]].unique().shape[0] != 1:
                info_additional.append(searchfile.columns[i])
    output_additional_info_list = []
    for i in info_additional:
        output_additional_info_list.append(searchfile[i].fillna(-9999).tolist())

    return searchfile[search_data].tolist(), searchfile[org_data].tolist(), output_additional_info_list


if __name__ == "__main__":
    seldriver = SelDriver()
    driver = seldriver.control()
    muinfo = seldriver.get_MU_info()
    maindataframe = DataFrameOperator(muinfo)
    print("**Main Dataframe initiated.")

    mode = True
    print("Please Put your 'SEARCH TERM', SEARCH TERM may Company's name or Tax number      : ")
    print("!!!!!!!If you want massive search: Press <<<<9999<<<<<<<<<")
    search_term = input("SEARCH TERM:::::>>>>>>>>              ")

    if search_term == str(9999):
        mode = 9999
        print("""
        !*!*!**!!*!*!*!*!*!!*!*!*!
        WELCOMETOMASSIVESEARCHMODE
        !*!*!**!!*!*!*!*!*!!*!*!*!
                """)
        print("If you want to stop during loop, just close the brower. Python will automactically save the result")
        massivemode = input("Please select massive search mode.        1: normal massive / 2:juju massive ")

        basic_searchlist, org_id, additioanl_info_list = massive_search()
        start_num = int(input("몇부터 시작하시겠습니까? 숫자만 가능. 시작 : 0 입력"))
        searchlist = basic_searchlist[start_num:]
        org_id_list = org_id[start_num:]
        for i in range(len(additioanl_info_list)):
            additioanl_info_list[i] = additioanl_info_list[i][start_num:]
        try:
            while mode != 0:
                for i in range(len(searchlist)):
                    search_object = [searchlist[i], org_id_list[i]]
                    print(searchlist[i])
                    for info_list in additioanl_info_list:
                        if info_list[i] == -9999:
                            pass
                        else:
                            print(info_list[i])

                    if massivemode == "1":
                        information = GiveMeInfo(driver, search_object).solo()
                        information.taxlist = maindataframe.compare_tax(information.taxnumber)
                        maindataframe.make_infomation(information)
                        del information

                    elif massivemode == "2":
                        information = GiveMeInfo(driver, search_object).juju_club()
                        information.taxlist = maindataframe.compare_tax(information.taxnumber)
                        maindataframe.make_infomation_with_juju(information)
                        del information

                    number = start_num + i
                    print(f"{number}번째 작업완료. EXCEL상 {number+2}번째 계정이 완료되었습니다. 재시작시 {number+1}을 입력해주세요.")
                    if (i%100 == 0) & (i != 0):
                        print("For ensure your data, Autosave is performed")
                        maindataframe.plush_to_excel(1)
                        print("Don't worry, I'm only swimming. Let's begin again! :)")
                mode = 0
                print("Completed!")
                print("Be Happy!!!!")
            else:
                print("Done! NOW EXPORTING YOUR DATA......")
                maindataframe.plush_to_excel()
        except Exception as e:
            maindataframe.plush_to_excel()
            print(e)

    else:
        while (mode != "0") & (mode != 9999):
            try:
                information = GiveMeInfo(driver, search_term).solo()
                information.taxlist = maindataframe.compare_tax(information.taxnumber)
                maindataframe.make_infomation(information)
                del information

                print("If you want to continue, please put other SEARCH TERM.         ")
                search_term = str(input("ELSE, EXPORT TO EXCEL >:>:>:>:>:>       PRESS 0                    "))

                if search_term == "0":
                    mode = "0"
                else:
                    mode = 99

            except Exception as e:
                maindataframe.plush_to_excel()
                print(e)
                break
        else:
            print("Completed!")
            print("NOW EXPORTING YOUR DATA......")
            maindataframe.plush_to_excel()
            print("Be Happy!!!!")
