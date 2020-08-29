from flask import Flask, render_template, url_for, request
from nepal_forex.nepal_forex import nepal_forex
app = Flask(__name__)

@app.route('/')
def hello_world():
    def conversion(cur):
        return(nepal_forex.exchange_rate(currency=cur))
    USD=conversion("USD")
    INR=conversion("INR")
    EUR=conversion("EUR")
    GBP=conversion("GBP")
    CHF=conversion("CHF")
    AUD=conversion("AUD")
    CAD=conversion("CAD")
    SGD=conversion("SGD")
    JPY=conversion("JPY")
    SAR=conversion("SAR")
    QAR=conversion("QAR")
    THB=conversion("THB")
    AED=conversion("AED")
    MYR=conversion("MYR")
    KRW=conversion("KRW")
    SEK=conversion("SEK")
    DKK=conversion("DKK")
    HKD=conversion("HKD")
    BHD=conversion("BHD")
    return render_template('index.html', usd=USD, inr= INR, eur=EUR, gbp=GBP, chf=CHF, aud=AUD, cad=CAD, sgd=SGD, jpy=JPY, sar=SAR, qar=QAR, thb=THB, aed=AED, myr=MYR, krw=KRW, sek=SEK, dkk=DKK, hkd=HKD, bhd=BHD) 
