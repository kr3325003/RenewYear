import pandas as pd
import random as rand

ip_data = pd.read_csv("C:\\Users\\KB\\Desktop\\김홍근프로\\Raw_DATA\\ipv4.csv", encoding='cp949')
mal_data = pd.read_csv("C:\\Users\\KB\\Desktop\\김홍근프로\\Raw_DATA\\KIS00000000000000004.csv")

def Find_Country(ip='1.1.1.1'):
    sips, dips, countries = [], [], []
    sips = ip_data['시작IP']
    dips = ip_data['끝IP']
    countries = ip_data['국가코드']
    count = []
    ip = list(map(lambda x: int(x), ip.split('.')))

    for sip, dip, country in zip(sips, dips, countries):
        sip = list(map(lambda x: int(x), sip.split('.')))
        dip = list(map(lambda x: int(x), dip.split('.')))

        if sip[0] <= ip[0] <= dip[0]:
            if sip[1] <= ip[1] <= dip[1]:
                if sip[2] <= ip[2] <= dip[2]:
                    return country
    return 'Unknown'


count = 0

for row in mal_data.loc[:, 'IP주소']:
    trans_ip = row.replace('*', str(rand.randrange(0,256)))
    mal_data.loc[count, 'Trans_IP'] = trans_ip
    count += 1
print(mal_data.head(10))

mal_data.to_csv("C:\\Users\\KB\\Desktop\\김홍근프로\\Raw_DATA\\Step1.csv", encoding='cp949')

