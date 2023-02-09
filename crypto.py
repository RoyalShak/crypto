from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import time

load_dotenv()
APIKey = '1151bd0d-4a4d-4414-972a-3313dc3dce34'

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'slug': 'lossless,dogecoin,terra,shiba-inu,bone-shibaswap,terra-luna-v2,polygon,xrp,dent,quant,avalanche,popsicle-finance,metamonkeyai,binance-usd,tether,bitcoin,solana,beam,bancor,ethereum,tamadoge,casper,augur,api3,litecoin,sologenic,terrausd,lever,jasmy,only1',
    'convert': 'USD',
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': APIKey
}

session = Session()
session.headers.update(headers)
try:
    response = session.get(url, params=parameters, headers=headers)
    data = json.loads(response.text)


    # print(data)

    def sendEmail(result, total):
        totalInvest = 10983
        currentStatus = total - totalInvest
        password = 'Xiah!@#1989'
        user = 'support@techticom.com'
        message = "Coin Name   |   Symbol   |   Amount of coins   |   Final coin value   |   percent_change_24h" '\n\n' + result + '\n' + "Portfolio Balance: $" + str(
            total) + '\n\n' + "Total Investment: $" + str(totalInvest) + '\n\n' + "Current Status : $" + str(
            currentStatus)
        smtpsrv = "smtp.office365.com"
        smtpserver = smtplib.SMTP(smtpsrv, 587)

        msg = EmailMessage()
        msg['Subject'] = 'Cryptocurrency daily status' + " " + datetime.now().strftime('%#d %b %Y %H:%M')
        msg['From'] = 'liran@techticom.com'
        msg['To'] = user
        msg.set_content(message)

        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.login(user, password)
        smtpserver.send_message(msg)
        smtpserver.close()
        print(currentStatus)


    def cid():
        myCoin = {'Bitcoin': 0, 'Litecoin': 13.28869800, 'XRP': 0, 'Dogecoin': 0, 'USDT': 0, 'Ethereum': 0,
                  'Augur': 0, 'Bancor': 0, 'Dent': 1039271.5,
                  'Quant': 2.533824, 'Beam': 0, 'Polygon': 55.11880844,
                  'LUNC': 6499743.894257, 'Binance USD': 0, 'Sologenic': 0, 'Solana': 0, 'Avalanche': 0,
                  'Casper': 15648.39104,
                  'Shiba Inu': 102918237.12, 'USTC': 35597, 'API3': 166.54329, 'JasmyCoin': 102763.7683,
                  'Popsicle Finance': 0,
                  'Lossless': 1118.645226, 'Like': 38892.749183, 'Bone ShibaSwap': 167.67, 'Terra': 99.31599,
                  'MetamonkeyAi': 1596207.18871712, 'Lever': 181381.437, 'Tamadoge': 1900}
        myCoinOut = {x: y for x, y in myCoin.items() if y != 0}
        lst = [  # 1, 52, 74, 825, 1027,1104,
            2, 1886, 3155, 3890, 4172,
            #  3702,5426, 1727, 5279,4687,9073,5805,
            5899, 5994, 7129, 7737, 8425, 10103, 10891, 11865, 20314, 21731, 20873, 21968]
        length = len(lst)
        total = 0
        result = ""
        for i in range(length):
            cid = str(lst[i])
            coinName = str(data['data'][cid]['name'])
            coinSymbol = str(data['data'][cid]['symbol'])
            coinPrice = str(data['data'][cid]['quote']['USD']['price'])
            # coinMC = str(data['data'][cid]['quote']['USD']['market_cap'])
            coinAmount = list(myCoinOut.values())
            totalUSD = float(coinAmount[i]) * float(coinPrice)
            totalUSD = f'{totalUSD:.2f}'
            percent_24h = str(data['data'][cid]['quote']['USD']['percent_change_24h'])
            result += coinName + "   |   " + coinSymbol + "   |   " + str(coinAmount[i]) + "   |   $" + str(
                totalUSD) + "   |   " + str(percent_24h) + '%' + '\n\n'
            total += float(totalUSD)
        print(result)
        print(total)
        sendEmail(result, total)


    cid()

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
