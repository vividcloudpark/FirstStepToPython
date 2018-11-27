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
    endnum = 100
    index = f'/{fromnum}/{endnum}/'
    date = '20181114/'
    bus_num = input("몇번버스를 탈까요?") + '/'
    requrl = funder_url+index+date+bus_num
    print(requrl)

    req = urllib.request.Request(requrl)
    response = urllib.request.urlopen(req)
    data = response.read().decode(response.headers.get_content_charset())
    albumdata = json.loads(data)
    pprint.pprint(albumdata)

    numoflist = albumdata['CardBusStatisticsServiceNew']['list_total_count']
    print(str(numoflist)  + "개 발견!")
    if numoflist < 100:
        loopnum = numoflist
    else:
        loopnum = 100


    for i in range(loopnum):
        a = 0
        b = 0
        stationname = albumdata['CardBusStatisticsServiceNew']['row'][i]['BUS_STA_NM']
        people = int(albumdata['CardBusStatisticsServiceNew']['row'][i]['RIDE_PASGR_NUM'])
        if people > a:
            a = people
            b = stationname
        print(f'{stationname}에서는 {people}명이 탔네요!')
    print(f'오늘 {bus_num.replace("/","")}버스에서 제일 많이 탄 정거장은 {b}에서 {a}명 탄게 최대입니다!')

if __name__ == '__main__':
    Bustracker()
