import json

import requests
import datetime


def login(id, password):
    # return a key

    login_url = "https://epidemicapi.ncut.edu.tw/api/login"
    data = {'userId': id, 'password': password, 'remember': True}
    header = {'Accept': 'application/json, text/plain, */*',
              'Accept-Encoding': 'gzip, deflate, br',
              'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
              'Connection': 'keep-alive',
              'Content-Length': '62',
              'Content-Type': 'application/json;charset=UTF-8',
              'Host': 'epidemicapi.ncut.edu.tw',
              'Origin': 'https://epidemic.ncut.edu.tw',
              'Referer': 'https://epidemic.ncut.edu.tw/',
              'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
              'sec-ch-ua-mobile': '?0',
              'Sec-Fetch-Dest': 'empty',
              'Sec-Fetch-Mode': 'cors',
              'Sec-Fetch-Site': 'same-site',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'}

    html = requests.post(login_url, json=data, headers=header)
    # print(html.text)
    return html.json()['token']


def upload(saveDate, key):
    header = {'Accept': 'application/json, text/plain, */*',
              'Accept-Encoding': 'gzip, deflate, br',
              'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
              'authorization': 'Bearer ' + key,
              'Connection': 'keep-alive',
              'Content-Length': '62',
              'Content-Type': 'application/json;charset=UTF-8',
              'Host': 'epidemicapi.ncut.edu.tw',
              'Origin': 'https://epidemic.ncut.edu.tw',
              'Referer': 'https://epidemic.ncut.edu.tw/',
              'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
              'sec-ch-ua-mobile': '?0',
              'Sec-Fetch-Dest': 'empty',
              'Sec-Fetch-Mode': 'cors',
              'Sec-Fetch-Site': 'same-site',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'}

    data = {"id": "3A812074-undefined", "userId": "3A812074",
            "saveDate": saveDate,
            "morningTemp": 34, "noonTemp": 34, "nightTemp": 34,
            "morningActivity": "家中(Home)", "noonActivity": "家中(Home)", "nightActivity": "家中(Home)",
            "departmentId": "11", "className": "四電三乙", "departmentName": "電機系", "type": "1",
            "morningManner": 0, "noonManner": 0, "nightManner": 0, "isMorningFever": None, "isNoonFever": False,
            "isNightFever": None, "isValid": False, "measureTime": "13:09"}

    html2 = requests.put("https://epidemicapi.ncut.edu.tw/api/temperatureSurveys", json=data, headers=header)
    result = html2.json()
    # print(type(result['success']), result['success'])

    if not result["success"]:
        html3 = requests.post("https://epidemicapi.ncut.edu.tw/api/temperatureSurveys", json=data, headers=header)
        result = html3.json()
        print('upload success: ', result['success'], "\nsaveDate: ", result['instance']['saveDate'])
    else:
        print(saveDate, " 已經填過")


def getToday_date():
    return str(datetime.date.today())


def upload_today(id, password):
    try:
        upload(getToday_date(), login(id, password))
        return True
    except json.decoder.JSONDecodeError:
        print("id or password Error")
        # input()
        return False


def upload_allDay(id, password):
    try:
        key = login(id, password)
        today = datetime.date.today()
        print('today: ', today)
        for i in range(8):
            date = str(today - datetime.timedelta(days=i))
            upload(date, key)
        return True
    except json.decoder.JSONDecodeError:
        print("id or password Error")
        # input()
        return False



if "__main__" == __name__:
    # upload_allDay("3A812074", "33701309173")
    # upload(getToday_date(), key)
    # input()
    # upload_today("3A812074", '33701309173')
    login("3A812074", "33701309173")
