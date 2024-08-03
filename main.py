import db
import requests, os
from bs4 import BeautifulSoup
from flask import Flask, render_template
import schedule


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/display')
def display():
    post = fetch_stock()
    return render_template('base.html', post = post)

@app.route('/5days_display')
def display_five_days():
    post = db.fetch_five_days()
    return render_template('five_days.html', post = post)

@app.route('/10days_display')
def display_ten_days():
    post = db.fetch_ten_days()
    return render_template('ten_days.html', post = post)

@app.route('/20days_display')
def display_twenty_days():
    post = db.fetch_twenty_days()
    return render_template('twenty_days.html', post = post)

def fetch_stock():
    resp = requests.get("https://www.tradingview.com/markets/stocks-usa/market-movers-active/",
                        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'})


    if resp.status_code == 200:
        db.create_table()
        soup = BeautifulSoup(resp.text, "html.parser")
        target_tr = soup.find_all('tr', class_="row-RdUXZpkv listRow")

        num = 1
        for tr in target_tr:
            stock_name = tr["data-rowkey"]
            colon = stock_name.index(":")
            # get the name of the stock
            stock_name = stock_name[colon + 1:]

            if num > 20:
                break

            td_tags = tr.find_all('td')
            change = td_tags[3].text
            rel_volumn = td_tags[5].text
            p_e = td_tags[7].text

            db.insert_data(stock_name, change, rel_volumn, p_e)
            num += 1
        
        post = db.fetch_today_data()
        return post
    
schedule.every().day.at("00:00").do(fetch_stock)