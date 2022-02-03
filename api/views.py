from email import message
from django.shortcuts import render
from api.utils.send_email import send_email
from bs4 import BeautifulSoup
import requests
from api.models import StockStatus
# Create your views here.


def home(request):
    # root url containing page with all excel sheets.
    
    ctx = {
        "netonnet": StockStatus.objects.order_by('-created_at').filter(vendor="NetOnNet")[:1],
        "netonnet_url": "https://www.netonnet.se/art/gaming/spel-och-konsol/xbox/xbox-konsol/microsoft-xbox-series-x/1011151.14412/",
        "elgiganten": StockStatus.objects.order_by('-created_at').filter(vendor="ElGiganten")[:1],
        "elgiganten_url": "https://www.elgiganten.se/product/gaming/spelkonsoler-tillbehor/xbox/xbox-konsol/xbox-series-x-1-tb-svart/218667",
        "kjell": StockStatus.objects.order_by('-created_at').filter(vendor="Kjell")[:1],
        "kjell_url": "https://www.kjell.com/se/produkter/tv-spel-gaming/xbox-series-xs/xbox-series-x-1-tb-spelkonsol-p62914?utm_medium=affiliate&utm_content=textlink&utm_campaign=aff_1_2015&utm_source=adtraction_PriceRunner.se&at_gd=C826DA51DA581F69B2C4D93D85F98FE0903A1EC1",
        "komplett": StockStatus.objects.order_by('-created_at').filter(vendor="Komplett")[:1],
        "komplett_url": "https://www.komplett.se/product/1132588/gaming/xbox/xbox-series-x-1tb-svart",
    }
    return render(request, 'index.html', context=ctx)


def netonnet_status():
    return "no"
