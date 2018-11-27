import os
import json
import csv
import datetime
import time
import urllib.request
import pprint



def Bustracker():
    base = 'http://openapi.seoul.go.kr:8088/'
    credit = input("인증키를 넣어주세요")
    request_service_name = 'CardBusStatisticsServiceNew'
    funder_url = base+credit+'/json/'+request_service_name
    fromnum = 1
    endnum = 1000
    index = f'/{fromnum}/{endnum}/'
    date = '20181114/'
    bus_num = input("몇번버스를 탈까요?") + '/'
    requrl = funder_url+index+date+bus_num

    req = urllib.request.Request(requrl)
    response = urllib.request.urlopen(req)
    data = response.read().decode(response.headers.get_content_charset())
    albumdata = json.loads(data)
    pprint.pprint(albumdata)

    numoflist = albumdata['CardBusStatisticsServiceNew']['list_total_count']
    print(str(numoflist)  + "개 발견!")

    mostpeople = 0
    mostpeople_station = 0
    leastpeople = int(albumdata['CardBusStatisticsServiceNew']['row'][0]['RIDE_PASGR_NUM'])
    leastpeople_station = albumdata['CardBusStatisticsServiceNew']['row'][0]['BUS_STA_NM']

    for i in range(numoflist):
        stationname = albumdata['CardBusStatisticsServiceNew']['row'][i]['BUS_STA_NM']
        people = int(albumdata['CardBusStatisticsServiceNew']['row'][i]['RIDE_PASGR_NUM'])

        if people > mostpeople:
            mostpeople = people
            mostpeople_station = stationname
        elif people < leastpeople:
            leastpeople = people
            leastpeople_station = stationname

        print(f'{stationname}에서는 {people}명이 탔네요!')
    print(f'{date.replace("/","")}에 {bus_num.replace("/","")}버스에서 제일 많이 탄 정거장은 {mostpeople_station}에서 {mostpeople}명 탄게 최대입니다!')
    print(f'{date.replace("/","")}에 {bus_num.replace("/","")}버스에서 제일 적게 탄 정거장은 {leastpeople_station}에서 {leastpeople}명 탄게 최대입니다!')

if __name__ == '__main__':
    Bustracker()
