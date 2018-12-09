import os
import json
import csv
import datetime
import time
import urllib.request
import pprint

def compose_adddress(credit, bus_num, date):
    base = 'http://openapi.seoul.go.kr:8088/'    
    request_service_name = 'CardBusStatisticsServiceNew'
    funder_url = base+credit+'/json/'+request_service_name
    fromnum = 1
    endnum = 1000
    index = f'/{fromnum}/{endnum}/'
    date = date + '/'
    bus_num = bus_num + '/'
    requrl = funder_url + index + date + bus_num
    return requrl

    
def request_and_jsonlize(requrl):
    try:
        req = urllib.request.Request(requrl)
    except CardBusStatisticsServiceNew:
        print("URL이 잘못된것 같습니다. 인증키문제가 아닐까요?ㅁ")
    response = urllib.request.urlopen(req)
    data = response.read().decode(response.headers.get_content_charset())
    busdata = json.loads(data)
    pprint.pprint(busdata)
    numoflist = busdata['CardBusStatisticsServiceNew']['list_total_count']
    print(str(numoflist)  + "개 발견!")
    return busdata, numoflist
    
def bus_by_bus(busdata, numoflist, date, bus_num):
    mostpeople = 0
    mostpeople_station = 0
    leastpeople = int(busdata['CardBusStatisticsServiceNew']['row'][0]['RIDE_PASGR_NUM'])
    leastpeople_station = busdata['CardBusStatisticsServiceNew']['row'][0]['BUS_STA_NM']

    for i in range(numoflist):
        stationname = busdata['CardBusStatisticsServiceNew']['row'][i]['BUS_STA_NM']
        people = int(busdata['CardBusStatisticsServiceNew']['row'][i]['RIDE_PASGR_NUM'])

        if people > mostpeople:
            mostpeople = people
            mostpeople_station = stationname
        elif people < leastpeople:
            leastpeople = people
            leastpeople_station = stationname

        print(f'{stationname}에서는 {people}명이 탔네요!')
    print(
        f'{date.replace("/","")}에 {bus_num.replace("/","")}버스에서 제일 많이 탄 정거장은 {mostpeople_station}에서 {mostpeople}명 탄게 최대입니다!')
    print(
        f'{date.replace("/","")}에 {bus_num.replace("/","")}버스에서 제일 적게 탄 정거장은 {leastpeople_station}에서 {leastpeople}명 탄게 최대입니다!')
    return


def bustracker(credit):
    stop_button = False
    while stop_button != "0":
        bus_num = input("몇번버스를 탈까요?         ")
        date = input("몇일버스를 탈까요? 20181204 식으로 적어주세요           ")
        compose_adddress(credit, bus_num, date)
        requrl = compose_adddress(credit, bus_num, date)
        busdata, numoflist = request_and_jsonlize(requrl)
        bus_by_bus(busdata, numoflist, date, bus_num)

        stop_button = input("아무값이나 입력해주세요. 그만하고싶으면 0을 입력해주세요  ")
    else:
        print("내리실문은 오른쪽, 오른쪽입니다")
                            


if __name__ == '__main__':
    credit = input("인증키를 넣어주세요     ")
    bustracker(credit)
