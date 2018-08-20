# 本例测试抓取GoogleTrend feed流
import requests
import json

global count
count = 0
countries = ['JP', 'US', 'GB', 'HK', 'TW', 'RU', 'AU', 'KR']
countriesCN = ['日本', '美国', '英国', '香港', '台湾', '俄罗斯', '澳大利亚', '韩国']
url = 'https://trends.google.com/trends/api/dailytrends'

print('GoogleTrends 日趋势排行 请求开始')


def get_trends():
    global count
    params = {
        "hl": 'zh-CN',
        'tz': -480,
        'geo': countries[count],
        'ns': 15
    }
    print('\n***************  ', countriesCN[count], '  ***************\n')
    resp = requests.get(url, params)
    if resp.status_code != 200:
        print("{0} 请求失败 {1}".format(countries[count], resp.status_code))
        if count < len(countries) - 1:
            count = count + 1
            get_trends()
    else:
        temp = resp.content
        jsonStr = temp[6: len(temp)]
        b = json.loads(jsonStr)
        newsList = b['default']['trendingSearchesDays'][0]['trendingSearches']
        for index, item in enumerate(newsList):
            print('{0:2}  查询次数 {1:7}  关键字 {2:30}'.format(index, item['formattedTraffic'], item['title']['query']))
            if index == len(newsList) - 1 and count < len(countries) - 1:
                count = count + 1
                get_trends()


if __name__ == "__main__":
    get_trends()
