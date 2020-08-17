import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Apple-iPhone-XR-64GB-Yellow/dp/B07JWV47JW/ref=sr_1_1_sspa?keywords=iphone%2Bxr&qid=1577890843&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExOUJUMFpCTE9TSUFLJmVuY3J5cHRlZElkPUEwMDM4NzEyUDE3REUyRjJKRzBOJmVuY3J5cHRlZEFkSWQ9QTA0Mjk2NTQ0N01XV0ZPVTdaVlYmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1'

headers = {"User-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    # To print the title type: print(title.strip())

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = (price[2:8])
    print(price)
    # This steps helps convert this string to our float , this replace function is quite important
    converted_price = float(converted_price.replace(',', ''))
    print(converted_price)

    if (converted_price < 50000):
        send_mail()

    print(converted_price)
    if (converted_price <50000):
        send_mail()




def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('haiderrizvi1441@gmail.com', 'vvabundcshpeplen')

    subject = 'Price fell Down!'
    body = 'Check the amazon link https://www.amazon.in/Apple-iPhone-XR-64GB-Yellow/dp/B07JWV47JW/ref=sr_1_1_sspa?keywords=iphone%2Bxr&qid=1577890843&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExOUJUMFpCTE9TSUFLJmVuY3J5cHRlZElkPUEwMDM4NzEyUDE3REUyRjJKRzBOJmVuY3J5cHRlZEFkSWQ9QTA0Mjk2NTQ0N01XV0ZPVTdaVlYmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1 '

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'haiderrizvi1441@gmail.com',
        'blurryfaceearner@gmail.com',
        msg
    )
    print(" MAIL HAS BEEN SENT")
    server.quit()


check_price()







