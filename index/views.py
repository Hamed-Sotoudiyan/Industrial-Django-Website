from django.shortcuts import render
import requests
import json
import re
from bs4 import BeautifulSoup


# Create your views here.
def home(request):

    # currency_response = requests.get("https://api.navasan.tech/latest/?api_key=freer4qaU2ifnW0lOTLdk5TQnX63X8PF")
    # print(currency_response)
    # currency_response_json_data = json.loads(currency_response.text)
    # bitcoin_response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # bitcoin_response_json_data = json.loads(bitcoin_response.text)
    # context = {
    #     "Dollar": currency_response_json_data["usd_buy"]["value"],
    #     "Euro": currency_response_json_data["eur"]["value"],
    #     "Derham": currency_response_json_data["aed"]["value"],
    #     "Lira": currency_response_json_data["try"]["value"],
    #     "Yuan": currency_response_json_data["cny"]["value"],
    #     "Canadian_Dollar": currency_response_json_data["cad"]["value"],
    #     "Pound": currency_response_json_data["gbp"]["value"],
    #     "Bitcoin": bitcoin_response_json_data["bpi"]["USD"]["rate"],
    # }
    context={}
    return render(request, 'index/index.html', context)
