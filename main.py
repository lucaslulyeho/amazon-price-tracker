import requests
import smtplib
from bs4 import BeautifulSoup

URL = input("Paste the amazon url of your item of choice: ")
price_cap = input("Enter your price cap for this item: ")
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,la;q=0.7"
}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

item = soup.find(name="span", id="priceblock_ourprice")
# item = soup.find(name="span", id="priceblock_saleprice")
price = item.text
current_price = float(price.split("$")[1])

product_title = soup.find(id="productTitle")
product_title = product_title.text.strip()


if current_price <= float(price_cap):
    sender_email = "******"
    password = "*****"
    recipient_email = "********"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=f"{recipient_email}",
                            msg=f"Subject:Amazon price alert!\n\n{product_title} is now at ${current_price}!"
                            )
else:
    print("Wait till next day")



