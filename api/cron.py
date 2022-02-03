
from email import message
from django.shortcuts import render
from api.utils.send_email import send_email
from bs4 import BeautifulSoup
import requests
from api.models import StockStatus
# Create your views here.


def checkstock(url, vendor=""):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
        "Upgrade-Insecure-Requests": "1",
        "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br"
    }
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")
    # print(soup.prettify())
    lagerstatus = "Ej i Lager"
    # Netonnet code
    if vendor == "NetOnNet":
        job_elements = soup.find_all("div", class_="deliveryInfoText")
        for jobelement in job_elements:
            if jobelement.span.text == "I lager":
                lagerstatus = "Finns i Lager"
                StockStatus.objects.create(
                    message=jobelement.span.text,
                    vendor="NetOnNet",
                    instock=True
                )
            else:
                lagerstatus = jobelement.span.text
                StockStatus.objects.create(
                    message=jobelement.span.text,
                    vendor="NetOnNet",
                    instock=False
                )
                
    # Elgiganten Code
    if vendor == "ElGiganten":
        job_elements = soup.find_all("elk-product-presale")
        for jobelement in job_elements:
            if jobelement.span.text != "Releasedatum okänt":
                lagerstatus = "I lager"
                StockStatus.objects.create(
                    message=jobelement.span.text,
                    vendor="ElGiganten",
                    instock=True
                )
            else:
                lagerstatus = jobelement.span.text
                StockStatus.objects.create(
                    message=jobelement.span.text,
                    vendor="ElGiganten",
                    instock=False
                )
    if vendor == "Kjell":
        job_elements = soup.find("div", class_="hn hm fs eb b a3 ao es")
        print(job_elements.text)
        if job_elements.text != "Ej i lager":
            lagerstatus = "I Lager"
            StockStatus.objects.create(
                message=job_elements.text,
                vendor="Kjell",
                instock=True
            )
        else:
            lagerstatus = job_elements.text
            StockStatus.objects.create(
                message=job_elements.text,
                vendor="Kjell",
                instock=False
            )
    if vendor == "Komplett":
        job_elements = soup.find("button", class_="btn-large secondary")
        if job_elements.span.text != "Meddela mig":
            lagerstatus = "I lager"
            StockStatus.objects.create(
                message=job_elements.span.text,
                vendor="Komplett",
                instock=True
            )
        else:
            StockStatus.objects.create(
                message=job_elements.span.text,
                vendor="Komplett",
                instock=False
            )
            lagerstatus = job_elements.span.text

    if vendor == "MediaMarkt":
        job_elements = soup.find("div", class_="box infobox availability")
        print(job_elements)

    return lagerstatus
def runcronjob():
    checkstock(url="https://www.elgiganten.se/product/gaming/spelkonsoler-tillbehor/xbox/xbox-konsol/xbox-series-x-1-tb-svart/218667",
                            vendor="ElGiganten"
                            )
    checkstock(url="https://www.netonnet.se/art/gaming/spel-och-konsol/xbox/xbox-konsol/microsoft-xbox-series-x/1011151.14412/",
                          vendor="NetOnNet")
    checkstock("https://www.kjell.com/se/produkter/tv-spel-gaming/xbox-series-xs/xbox-series-x-1-tb-spelkonsol-p62914?utm_medium=affiliate&utm_content=textlink&utm_campaign=aff_1_2015&utm_source=adtraction_PriceRunner.se&at_gd=C826DA51DA581F69B2C4D93D85F98FE0903A1EC1", vendor="Kjell")
    checkstock(
        "https://www.komplett.se/product/1132588/gaming/xbox/xbox-series-x-1tb-svart", vendor="Komplett")
    checkstock(
        "https://www.mediamarkt.se/sv/product/_microsoft-xbox-series-x-1tb-spelkonsol-1317148.html", vendor="MediaMarkt")
    print("cronjob runnin")
    return ""