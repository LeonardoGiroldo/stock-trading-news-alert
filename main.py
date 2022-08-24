import requests
from datetime import datetime

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?'

apikey = "MEYKZ4FB2R193UKY"

parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "outputsize" : "compact",
    "apikey" : apikey
}

news_url = "https://newsapi.org/v2/everything?"
COMPANY_NAME = "Tesla Inc"
today_date = datetime.today().strftime("%Y-%m-%d")
news_apikey = "9510b6784bc0453ba142ea6df7c9a295"

news_parameters = {
    "q" : COMPANY_NAME,
    "from" : "2022-08-24",
    "sortBy" : "popularity",
    "apiKey" : news_apikey
}


r = requests.get(url, params= parameters, )
data = r.json()

#Get yesterday's closing stock price
yesterday_closing_price = [float(value['4. close']) for key, value in data["Time Series (Daily)"].items()]
print(yesterday_closing_price[0])

#Get the day before yesterday's closing stock price
before_yesterday_closing_price = yesterday_closing_price[1]
print(before_yesterday_closing_price)

#Find the positive difference between yesterday and before yesterday closing price

diff = yesterday_closing_price[0] - before_yesterday_closing_price
print(diff)

#Find the percentage difference in price between closing price yesterday and closing price the day before yesterday.

perc_diff = abs((yesterday_closing_price[0] - before_yesterday_closing_price) / before_yesterday_closing_price)
print(perc_diff)

#If percentage is greater than 5 use the News API to get articles related to the COMPANY_NAME.

get_news = False

if perc_diff > 5:
    get_news = True

if get_news == True:
    r = requests.get(news_url, params= news_parameters, )
    # Create a new list of the first 3 article's headline, description and URL using list comprehension.
    data = r.json()['articles'][0:3]
    formatted_articles = [f"Headline: {each_item['title']}, Brief: {each_item['description']}, URL: {each_item['url']} "  for each_item in data]
    print(formatted_articles)
   
