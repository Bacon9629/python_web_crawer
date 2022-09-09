import requests
from time import sleep

url = 'http://edge.microsoft.com/captiveportal/generate_204'
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '154',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '_ga=GA1.2.1069986106.1581493645; _cs_c=0; _mkto_trk=id:157-GQE-382&token:_mch-microsoft.com-1616661306285-70075; WRUID=3220945472701351; __CT_Data=gpv=1&ckp=tld&dm=microsoft.com&apv_1067_www32=1&cpv_1067_www32=1&rpv_1067_www32=1; mbox=PC#c306df8c5bfc46dda0f743ac3d59bf03.38_0#1655857574|session#54da4733d380496998407000d5046768#1624911551; _fbp=fb.1.1624909692273.860830520; AMCV_EA76ADE95776D2EC7F000101%40AdobeOrg=1585540135%7CMCMID%7C71083005777599958392487613699984248996%7CMCAAMLH-1625514492%7C11%7CMCAAMB-1625514492%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1624916892s%7CNONE%7CMCAID%7CNONE%7CMCSYNCS%7C411-18319%7CMCIDTS%7C18807%7CMCSYNCSOP%7C411-18719%7CvVersion%7C4.4.0%7CMCCIDH%7C-2133533211',
    'Host': 'edge.microsoft.com',
    'Origin': 'http://edge.microsoft.com',
    'Referer': 'http://edge.microsoft.com/captiveportal/generate_204',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67",
    'X-Mesh-Client-Arch': 'x86_64',
    'X-Mesh-Client-Edge-Channel': 'stable',
    'X-Mesh-Client-Edge-Version': '92.0.902.67',
    'X-Mesh-Client-OS': 'Windows',
    'X-Mesh-Client-OS-Version': '10.0.19042',
    'X-Mesh-Client-WebView': '0'
}
datas = {
    'magic': '729ebfc1e6347a12',
    'username': 's3a812074@student.ncut.edu.tw',
    'password': 'K123177273',
    '4Tredir': 'http://edge.microsoft.com/captiveportal/generate_204'
}


def get_magic_number(html):
    index = html.index('VALUE="') + len('VALUE="')
    return html[index:index + 16]


def test_need_connect():
    # if internet has not connected、return true。if has been connected、return false
    # 204 == connected、200 == not connected
    return requests.get(url).status_code == 200


def go_connect():
    try:
        if test_need_connect():
            html = requests.get(url).text
            datas['magic'] = get_magic_number(html)
            requests.post(url, data=datas, headers=header)
            print("connect success")
        else:
            print("internet has been connected")
    except:
        print("connect fail")


def always_run_connect(sleep_time):
    # sleep_time: 等待幾秒重複執行連線
    while True:
        go_connect()
        sleep(sleep_time)


def just_run_once_connect():
    go_connect()


if "__main__" == __name__:
    always_run_connect(10) # 等待()秒重複執行連線
    
#    just_run_once_connect()
#    with open("history.txt", 'a') as file:
#        localtime = localtime()
#        time_str = strftime("%Y-%m-%d %I:%M:%S %p \n", localtime)
#        file.write(time_str)
