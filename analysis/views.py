from django.shortcuts import render, redirect
from analysis.models import blogs
from analysis.models import faq
from analysis.models import experts
from analysis.models import latest_news
from analysis.models import myreview
from analysis.models import contact_us
from analysis.models import userregister
from analysis.models import helpsupport
from analysis.models import tutorials
from django.conf import settings
from django.core.mail import send_mail
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import datetime
from datetime import date
from newsapi.newsapi_client import NewsApiClient
import yfinance as yf
from django.shortcuts import render
import csv
from textblob import TextBlob
from django.http import FileResponse 
from django.http import HttpResponse
import os
import json
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.models import User
from django.conf import settings

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import random
# Create your views here.
def footer(request):
	return render(request,'footer.html')

def nav(request):
	return render(request,'nav.html')

def reliance(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	start=2024
	end=2024
	def get_first_day_of_january_start(year):
		return datetime.date(year, 1, 1)

	def get_first_day_of_january_end(year):
		return datetime.date(year, 12, 31)

	start_date = get_first_day_of_january_start(start)
	end_date = get_first_day_of_january_end(end)

	def parse_csv(file_path):
		with open(file_path, 'r') as file:
			reader = csv.DictReader(file)
			data = [row for row in reader]
		return data

	st="RELIANCE"			
	df= yf.download(tickers="RELIANCE.NS", start=start_date, end=end_date)
	df.to_csv('statics/RELIANCE.NS.csv')
	df=pd.read_csv('statics/RELIANCE.NS.csv',parse_dates=['Date'])
	df['Date']=df['Date'].dt.strftime('%Y-%m-%d')
	p='RELIANCE.NS.csv'
	print('data',df)
	json_records = df.reset_index().to_json(orient ='records') 
	data = [] 
	data = json.loads(json_records) 
	fig = go.Figure(data=[go.Candlestick(x=df['Date'],
		open=df['Open'],
		high=df['High'],
		low=df['Low'],
		close=df['Close'])])
	fig.update_layout(
		plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		paper_bgcolor='rgba(8, 17, 8, 0.9)',
		font=dict(color='#00d094'),
		)
	graph=fig.to_html()
					
	query="latest news for the stock "+st					
	newsapi=NewsApiClient(api_key='40f8fa21da67431885edfaec3fa49ac4')
	json_data= newsapi.get_everything(q=query,language='en',
		from_param=str(date.today()-datetime.timedelta(days=29)),
		to=str(date.today()),page_size=10,page=1,sort_by='relevancy')
	k=json_data['articles']

	def analyze_sentiment(text):
		blob = TextBlob(text)
		sentiment_score = blob.sentiment.polarity
		if sentiment_score > 0:
			return 'positive'
		elif sentiment_score < 0:
			return 'negative'
		else:
			return 'neutral'
				# Initialize counters
	positive_count = 0
	negative_count = 0
	neutral_count = 0
				# Iterate through the fetched articles and perform sentiment analysis
	for article in k:
	    sentiment = analyze_sentiment(article['description'])
	    if sentiment == 'positive':
	    	positive_count += 1
	    elif sentiment == 'negative':
	    	negative_count += 1
	    else:
	    	neutral_count += 1
	ms="sentiment"
	positive="Positive "+"("+str(positive_count)+")"
	negative="Negative "+"("+str(negative_count)+")"
	neutral="Neutral "+"("+str(neutral_count)+")"

	labels=[positive,negative,neutral]
	values=[positive_count,negative_count,neutral_count]
	fig1= go.Figure(data=[go.Pie(labels=labels,values=values)])
	title="Sentiment Analysis"
	fig1.update_layout(title_text=title, paper_bgcolor='#081108',
        font_color='white')
	graph1=fig1.to_html()

	return render(request,'reliance.html',{'graph':graph,'p':p,'d':data,'k':k,'graph1':graph1})



def bajaj(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	start=2024
	end=2024
	def get_first_day_of_january_start(year):
		return datetime.date(year, 1, 1)

	def get_first_day_of_january_end(year):
		return datetime.date(year, 12, 31)

	start_date = get_first_day_of_january_start(start)
	end_date = get_first_day_of_january_end(end)

	def parse_csv(file_path):
		with open(file_path, 'r') as file:
			reader = csv.DictReader(file)
			data = [row for row in reader]
		return data

	st="BAJFINANCE"			
	df= yf.download(tickers="BAJFINANCE.NS", start=start_date, end=end_date)
	df.to_csv('statics/BAJFINANCE.NS.csv')
	df=pd.read_csv('statics/BAJFINANCE.NS.csv',parse_dates=['Date'])
	df['Date']=df['Date'].dt.strftime('%Y-%m-%d')
	p='BAJFINANCE.NS.csv'
	print('data',df)
	json_records = df.reset_index().to_json(orient ='records') 
	data = [] 
	data = json.loads(json_records) 
	fig = go.Figure(data=[go.Candlestick(x=df['Date'],
		open=df['Open'],
		high=df['High'],
		low=df['Low'],
		close=df['Close'])])
	fig.update_layout(
		plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		paper_bgcolor='rgba(8, 17, 8, 0.9)',
		font=dict(color='#00d094'),
		)
	graph=fig.to_html()
					
	query="latest news for the stock Bajaj Finance"					
	newsapi=NewsApiClient(api_key='40f8fa21da67431885edfaec3fa49ac4')
	json_data= newsapi.get_everything(q=query,language='en',
		from_param=str(date.today()-datetime.timedelta(days=29)),
		to=str(date.today()),page_size=12,page=1,sort_by='relevancy')
	k=json_data['articles']

	def analyze_sentiment(text):
		blob = TextBlob(text)
		sentiment_score = blob.sentiment.polarity
		if sentiment_score > 0:
			return 'positive'
		elif sentiment_score < 0:
			return 'negative'
		else:
			return 'neutral'
				# Initialize counters
	positive_count = 0
	negative_count = 0
	neutral_count = 0
				# Iterate through the fetched articles and perform sentiment analysis
	for article in k:
	    sentiment = analyze_sentiment(article['description'])
	    if sentiment == 'positive':
	    	positive_count += 1
	    elif sentiment == 'negative':
	    	negative_count += 1
	    else:
	    	neutral_count += 1
	ms="sentiment"
	positive="Positive "+"("+str(positive_count)+")"
	negative="Negative "+"("+str(negative_count)+")"
	neutral="Neutral "+"("+str(neutral_count)+")"

	labels=[positive,negative,neutral]
	values=[positive_count,negative_count,neutral_count]
	fig1= go.Figure(data=[go.Pie(labels=labels,values=values)])
	title="Sentiment Analysis"
	fig1.update_layout(title_text=title, paper_bgcolor='#081108',
        font_color='white')
	graph1=fig1.to_html()
	print(k)
	return render(request,'bajaj.html',{'graph':graph,'p':p,'d':data,'k':k,'graph1':graph1})

def tata(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	start=2024
	end=2024
	def get_first_day_of_january_start(year):
		return datetime.date(year, 1, 1)

	def get_first_day_of_january_end(year):
		return datetime.date(year, 12, 31)

	start_date = get_first_day_of_january_start(start)
	end_date = get_first_day_of_january_end(end)

	def parse_csv(file_path):
		with open(file_path, 'r') as file:
			reader = csv.DictReader(file)
			data = [row for row in reader]
		return data

	st="TATAMOTORS"			
	df= yf.download(tickers="TATAMOTORS.NS", start=start_date, end=end_date)
	df.to_csv('statics/TATAMOTORS.NS.csv')
	df=pd.read_csv('statics/TATAMOTORS.NS.csv',parse_dates=['Date'])
	df['Date']=df['Date'].dt.strftime('%Y-%m-%d')
	p='TATAMOTORS.NS.csv'
	print('data',df)
	json_records = df.reset_index().to_json(orient ='records') 
	data = [] 
	data = json.loads(json_records) 
	fig = go.Figure(data=[go.Candlestick(x=df['Date'],
		open=df['Open'],
		high=df['High'],
		low=df['Low'],
		close=df['Close'])])
	fig.update_layout(
		plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		paper_bgcolor='rgba(8, 17, 8, 0.9)',
		font=dict(color='#00d094'),
		)
	graph=fig.to_html()
					
	query="latest news for the stock Tata Motors"					
	newsapi=NewsApiClient(api_key='40f8fa21da67431885edfaec3fa49ac4')
	json_data= newsapi.get_everything(q=query,language='en',
		from_param=str(date.today()-datetime.timedelta(days=29)),
		to=str(date.today()),page_size=12,page=1,sort_by='relevancy')
	k=json_data['articles']

	def analyze_sentiment(text):
		blob = TextBlob(text)
		sentiment_score = blob.sentiment.polarity
		if sentiment_score > 0:
			return 'positive'
		elif sentiment_score < 0:
			return 'negative'
		else:
			return 'neutral'
				# Initialize counters
	positive_count = 0
	negative_count = 0
	neutral_count = 0
				# Iterate through the fetched articles and perform sentiment analysis
	for article in k:
	    sentiment = analyze_sentiment(article['description'])
	    if sentiment == 'positive':
	    	positive_count += 1
	    elif sentiment == 'negative':
	    	negative_count += 1
	    else:
	    	neutral_count += 1
	ms="sentiment"
	positive="Positive "+"("+str(positive_count)+")"
	negative="Negative "+"("+str(negative_count)+")"
	neutral="Neutral "+"("+str(neutral_count)+")"

	labels=[positive,negative,neutral]
	values=[positive_count,negative_count,neutral_count]
	fig1= go.Figure(data=[go.Pie(labels=labels,values=values)])
	title="Sentiment Analysis"
	fig1.update_layout(title_text=title, paper_bgcolor='#081108',
        font_color='white')
	graph1=fig1.to_html()

	return render(request,'tata.html',{'graph':graph,'p':p,'d':data,'k':k,'graph1':graph1})

def infy(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	start=2024
	end=2024
	def get_first_day_of_january_start(year):
		return datetime.date(year, 1, 1)

	def get_first_day_of_january_end(year):
		return datetime.date(year, 12, 31)

	start_date = get_first_day_of_january_start(start)
	end_date = get_first_day_of_january_end(end)

	def parse_csv(file_path):
		with open(file_path, 'r') as file:
			reader = csv.DictReader(file)
			data = [row for row in reader]
		return data

	st="INFY"			
	df= yf.download(tickers="INFY.NS", start=start_date, end=end_date)
	df.to_csv('statics/INFY.NS.csv')
	df=pd.read_csv('statics/INFY.NS.csv',parse_dates=['Date'])
	df['Date']=df['Date'].dt.strftime('%Y-%m-%d')
	p='INFY.NS.csv'
	print('data',df)
	json_records = df.reset_index().to_json(orient ='records') 
	data = [] 
	data = json.loads(json_records) 
	fig = go.Figure(data=[go.Candlestick(x=df['Date'],
		open=df['Open'],
		high=df['High'],
		low=df['Low'],
		close=df['Close'])])
	fig.update_layout(
		plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		paper_bgcolor='rgba(8, 17, 8, 0.9)',
		font=dict(color='#00d094'),
		)
	graph=fig.to_html()
					
	query="latest news for the stock Infosys"					
	newsapi=NewsApiClient(api_key='40f8fa21da67431885edfaec3fa49ac4')
	json_data= newsapi.get_everything(q=query,language='en',
		from_param=str(date.today()-datetime.timedelta(days=29)),
		to=str(date.today()),page_size=12,page=1,sort_by='relevancy')
	k=json_data['articles']

	def analyze_sentiment(text):
		blob = TextBlob(text)
		sentiment_score = blob.sentiment.polarity
		if sentiment_score > 0:
			return 'positive'
		elif sentiment_score < 0:
			return 'negative'
		else:
			return 'neutral'
				# Initialize counters
	positive_count = 0
	negative_count = 0
	neutral_count = 0
				# Iterate through the fetched articles and perform sentiment analysis
	for article in k:
	    sentiment = analyze_sentiment(article['description'])
	    if sentiment == 'positive':
	    	positive_count += 1
	    elif sentiment == 'negative':
	    	negative_count += 1
	    else:
	    	neutral_count += 1
	ms="sentiment"
	positive="Positive "+"("+str(positive_count)+")"
	negative="Negative "+"("+str(negative_count)+")"
	neutral="Neutral "+"("+str(neutral_count)+")"

	labels=[positive,negative,neutral]
	values=[positive_count,negative_count,neutral_count]
	fig1= go.Figure(data=[go.Pie(labels=labels,values=values)])
	title="Sentiment Analysis"
	fig1.update_layout(title_text=title, paper_bgcolor='#081108',
        font_color='white')
	graph1=fig1.to_html()

	return render(request,'infy.html',{'graph':graph,'p':p,'d':data,'k':k,'graph1':graph1})

def itc(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	start=2024
	end=2024
	def get_first_day_of_january_start(year):
		return datetime.date(year, 1, 1)

	def get_first_day_of_january_end(year):
		return datetime.date(year, 12, 31)

	start_date = get_first_day_of_january_start(start)
	end_date = get_first_day_of_january_end(end)

	def parse_csv(file_path):
		with open(file_path, 'r') as file:
			reader = csv.DictReader(file)
			data = [row for row in reader]
		return data

	st="ITC"			
	df= yf.download(tickers="ITC.NS", start=start_date, end=end_date)
	df.to_csv('statics/ITC.NS.csv')
	df=pd.read_csv('statics/ITC.NS.csv',parse_dates=['Date'])
	df['Date']=df['Date'].dt.strftime('%Y-%m-%d')
	p='ITC.NS.csv'
	print('data',df)
	json_records = df.reset_index().to_json(orient ='records') 
	data = [] 
	data = json.loads(json_records) 
	fig = go.Figure(data=[go.Candlestick(x=df['Date'],
		open=df['Open'],
		high=df['High'],
		low=df['Low'],
		close=df['Close'])])
	fig.update_layout(
		plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		paper_bgcolor='rgba(8, 17, 8, 0.9)',
		font=dict(color='#00d094'),
		)
	graph=fig.to_html()
					
	query="latest news for the stock ITC"					
	newsapi=NewsApiClient(api_key='40f8fa21da67431885edfaec3fa49ac4')
	json_data= newsapi.get_everything(q=query,language='en',
		from_param=str(date.today()-datetime.timedelta(days=29)),
		to=str(date.today()),page_size=12,page=1,sort_by='relevancy')
	k=json_data['articles']

	def analyze_sentiment(text):
		blob = TextBlob(text)
		sentiment_score = blob.sentiment.polarity
		if sentiment_score > 0:
			return 'positive'
		elif sentiment_score < 0:
			return 'negative'
		else:
			return 'neutral'
				# Initialize counters
	positive_count = 0
	negative_count = 0
	neutral_count = 0
				# Iterate through the fetched articles and perform sentiment analysis
	for article in k:
	    sentiment = analyze_sentiment(article['description'])
	    if sentiment == 'positive':
	    	positive_count += 1
	    elif sentiment == 'negative':
	    	negative_count += 1
	    else:
	    	neutral_count += 1
	ms="sentiment"
	positive="Positive "+"("+str(positive_count)+")"
	negative="Negative "+"("+str(negative_count)+")"
	neutral="Neutral "+"("+str(neutral_count)+")"

	labels=[positive,negative,neutral]
	values=[positive_count,negative_count,neutral_count]
	fig1= go.Figure(data=[go.Pie(labels=labels,values=values)])
	title="Sentiment Analysis"
	fig1.update_layout(title_text=title, paper_bgcolor='#081108',
        font_color='white')
	graph1=fig1.to_html()

	return render(request,'itc.html',{'graph':graph,'p':p,'d':data,'k':k,'graph1':graph1})

def sbi(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	start=2024
	end=2024
	def get_first_day_of_january_start(year):
		return datetime.date(year, 1, 1)

	def get_first_day_of_january_end(year):
		return datetime.date(year, 12, 31)

	start_date = get_first_day_of_january_start(start)
	end_date = get_first_day_of_january_end(end)

	def parse_csv(file_path):
		with open(file_path, 'r') as file:
			reader = csv.DictReader(file)
			data = [row for row in reader]
		return data

	st="SBIN"			
	df= yf.download(tickers="SBIN.NS", start=start_date, end=end_date)
	df.to_csv('statics/SBIN.NS.csv')
	df=pd.read_csv('statics/SBIN.NS.csv',parse_dates=['Date'])
	df['Date']=df['Date'].dt.strftime('%Y-%m-%d')
	p='SBIN.NS.csv'
	print('data',df)
	json_records = df.reset_index().to_json(orient ='records') 
	data = [] 
	data = json.loads(json_records) 
	fig = go.Figure(data=[go.Candlestick(x=df['Date'],
		open=df['Open'],
		high=df['High'],
		low=df['Low'],
		close=df['Close'])])
	fig.update_layout(
		plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		paper_bgcolor='rgba(8, 17, 8, 0.9)',
		font=dict(color='#00d094'),
		)
	graph=fig.to_html()
					
	query="latest news for the stock SBI Bank"					
	newsapi=NewsApiClient(api_key='40f8fa21da67431885edfaec3fa49ac4')
	json_data= newsapi.get_everything(q=query,language='en',
		from_param=str(date.today()-datetime.timedelta(days=29)),
		to=str(date.today()),page_size=12,page=1,sort_by='relevancy')
	k=json_data['articles']

	def analyze_sentiment(text):
		blob = TextBlob(text)
		sentiment_score = blob.sentiment.polarity
		if sentiment_score > 0:
			return 'positive'
		elif sentiment_score < 0:
			return 'negative'
		else:
			return 'neutral'
				# Initialize counters
	positive_count = 0
	negative_count = 0
	neutral_count = 0
				# Iterate through the fetched articles and perform sentiment analysis
	for article in k:
	    sentiment = analyze_sentiment(article['description'])
	    if sentiment == 'positive':
	    	positive_count += 1
	    elif sentiment == 'negative':
	    	negative_count += 1
	    else:
	    	neutral_count += 1
	ms="sentiment"
	positive="Positive "+"("+str(positive_count)+")"
	negative="Negative "+"("+str(negative_count)+")"
	neutral="Neutral "+"("+str(neutral_count)+")"

	labels=[positive,negative,neutral]
	values=[positive_count,negative_count,neutral_count]
	fig1= go.Figure(data=[go.Pie(labels=labels,values=values)])
	title="Sentiment Analysis"
	fig1.update_layout(title_text=title, paper_bgcolor='#081108',
        font_color='white')
	graph1=fig1.to_html()

	return render(request,'sbi.html',{'graph':graph,'p':p,'d':data,'k':k,'graph1':graph1})

def hdfc(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	start=2024
	end=2024
	def get_first_day_of_january_start(year):
		return datetime.date(year, 1, 1)

	def get_first_day_of_january_end(year):
		return datetime.date(year, 12, 31)

	start_date = get_first_day_of_january_start(start)
	end_date = get_first_day_of_january_end(end)

	def parse_csv(file_path):
		with open(file_path, 'r') as file:
			reader = csv.DictReader(file)
			data = [row for row in reader]
		return data

	st="HDFCBANK"			
	df= yf.download(tickers="HDFCBANK.NS", start=start_date, end=end_date)
	df.to_csv('statics/HDFCBANK.NS.csv')
	df=pd.read_csv('statics/HDFCBANK.NS.csv',parse_dates=['Date'])
	df['Date']=df['Date'].dt.strftime('%Y-%m-%d')
	p='HDFCBANK.NS.csv'
	print('data',df)
	json_records = df.reset_index().to_json(orient ='records') 
	data = [] 
	data = json.loads(json_records) 
	fig = go.Figure(data=[go.Candlestick(x=df['Date'],
		open=df['Open'],
		high=df['High'],
		low=df['Low'],
		close=df['Close'])])
	fig.update_layout(
		plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		paper_bgcolor='rgba(8, 17, 8, 0.9)',
		font=dict(color='#00d094'),
		)
	graph=fig.to_html()
					
	query="latest news for the stock HDFC Bank"					
	newsapi=NewsApiClient(api_key='40f8fa21da67431885edfaec3fa49ac4')
	json_data= newsapi.get_everything(q=query,language='en',
		from_param=str(date.today()-datetime.timedelta(days=29)),
		to=str(date.today()),page_size=12,page=1,sort_by='relevancy')
	k=json_data['articles']

	def analyze_sentiment(text):
		blob = TextBlob(text)
		sentiment_score = blob.sentiment.polarity
		if sentiment_score > 0:
			return 'positive'
		elif sentiment_score < 0:
			return 'negative'
		else:
			return 'neutral'
				# Initialize counters
	positive_count = 0
	negative_count = 0
	neutral_count = 0
				# Iterate through the fetched articles and perform sentiment analysis
	for article in k:
	    sentiment = analyze_sentiment(article['description'])
	    if sentiment == 'positive':
	    	positive_count += 1
	    elif sentiment == 'negative':
	    	negative_count += 1
	    else:
	    	neutral_count += 1
	ms="sentiment"
	positive="Positive "+"("+str(positive_count)+")"
	negative="Negative "+"("+str(negative_count)+")"
	neutral="Neutral "+"("+str(neutral_count)+")"

	labels=[positive,negative,neutral]
	values=[positive_count,negative_count,neutral_count]
	fig1= go.Figure(data=[go.Pie(labels=labels,values=values)])
	title="Sentiment Analysis"
	fig1.update_layout(title_text=title, paper_bgcolor='#081108',
        font_color='white')
	graph1=fig1.to_html()

	return render(request,'hdfc.html',{'graph':graph,'p':p,'d':data,'k':k,'graph1':graph1})

def icici(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	start=2024
	end=2024
	def get_first_day_of_january_start(year):
		return datetime.date(year, 1, 1)

	def get_first_day_of_january_end(year):
		return datetime.date(year, 12, 31)

	start_date = get_first_day_of_january_start(start)
	end_date = get_first_day_of_january_end(end)

	def parse_csv(file_path):
		with open(file_path, 'r') as file:
			reader = csv.DictReader(file)
			data = [row for row in reader]
		return data

	st="ICICIBANK"			
	df= yf.download(tickers="ICICIBANK.NS", start=start_date, end=end_date)
	df.to_csv('statics/ICICIBANK.NS.csv')
	df=pd.read_csv('statics/ICICIBANK.NS.csv',parse_dates=['Date'])
	df['Date']=df['Date'].dt.strftime('%Y-%m-%d')
	p='ICICIBANK.NS.csv'
	print('data',df)
	json_records = df.reset_index().to_json(orient ='records') 
	data = [] 
	data = json.loads(json_records) 
	fig = go.Figure(data=[go.Candlestick(x=df['Date'],
		open=df['Open'],
		high=df['High'],
		low=df['Low'],
		close=df['Close'])])
	fig.update_layout(
		plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		paper_bgcolor='rgba(8, 17, 8, 0.9)',
		font=dict(color='#00d094'),
		)
	graph=fig.to_html()
					
	query="latest news for the stock ICICI Bank"					
	newsapi=NewsApiClient(api_key='40f8fa21da67431885edfaec3fa49ac4')
	json_data= newsapi.get_everything(q=query,language='en',
		from_param=str(date.today()-datetime.timedelta(days=29)),
		to=str(date.today()),page_size=12,page=1,sort_by='relevancy')
	k=json_data['articles']

	def analyze_sentiment(text):
		blob = TextBlob(text)
		sentiment_score = blob.sentiment.polarity
		if sentiment_score > 0:
			return 'positive'
		elif sentiment_score < 0:
			return 'negative'
		else:
			return 'neutral'
				# Initialize counters
	positive_count = 0
	negative_count = 0
	neutral_count = 0
				# Iterate through the fetched articles and perform sentiment analysis
	for article in k:
	    sentiment = analyze_sentiment(article['description'])
	    if sentiment == 'positive':
	    	positive_count += 1
	    elif sentiment == 'negative':
	    	negative_count += 1
	    else:
	    	neutral_count += 1
	ms="sentiment"
	positive="Positive "+"("+str(positive_count)+")"
	negative="Negative "+"("+str(negative_count)+")"
	neutral="Neutral "+"("+str(neutral_count)+")"

	labels=[positive,negative,neutral]
	values=[positive_count,negative_count,neutral_count]
	fig1= go.Figure(data=[go.Pie(labels=labels,values=values)])
	title="Sentiment Analysis"
	fig1.update_layout(title_text=title, paper_bgcolor='#081108',
        font_color='white')
	graph1=fig1.to_html()

	return render(request,'icici.html',{'graph':graph,'p':p,'d':data,'k':k,'graph1':graph1})

def sun(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	start=2024
	end=2024
	def get_first_day_of_january_start(year):
		return datetime.date(year, 1, 1)

	def get_first_day_of_january_end(year):
		return datetime.date(year, 12, 31)

	start_date = get_first_day_of_january_start(start)
	end_date = get_first_day_of_january_end(end)

	def parse_csv(file_path):
		with open(file_path, 'r') as file:
			reader = csv.DictReader(file)
			data = [row for row in reader]
		return data

	st="SUNPHARMA"			
	df= yf.download(tickers="SUNPHARMA.NS", start=start_date, end=end_date)
	df.to_csv('statics/SUNPHARMA.NS.csv')
	df=pd.read_csv('statics/SUNPHARMA.NS.csv',parse_dates=['Date'])
	df['Date']=df['Date'].dt.strftime('%Y-%m-%d')
	p='SUNPHARMA.NS.csv'
	print('data',df)
	json_records = df.reset_index().to_json(orient ='records') 
	data = [] 
	data = json.loads(json_records) 
	fig = go.Figure(data=[go.Candlestick(x=df['Date'],
		open=df['Open'],
		high=df['High'],
		low=df['Low'],
		close=df['Close'])])
	fig.update_layout(
		plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		paper_bgcolor='rgba(8, 17, 8, 0.9)',
		font=dict(color='#00d094'),
		)
	graph=fig.to_html()
					
	query="latest news for the stock Sun Pharma"					
	newsapi=NewsApiClient(api_key='40f8fa21da67431885edfaec3fa49ac4')
	json_data= newsapi.get_everything(q=query,language='en',
		from_param=str(date.today()-datetime.timedelta(days=29)),
		to=str(date.today()),page_size=12,page=1,sort_by='relevancy')
	k=json_data['articles']

	def analyze_sentiment(text):
		blob = TextBlob(text)
		sentiment_score = blob.sentiment.polarity
		if sentiment_score > 0:
			return 'positive'
		elif sentiment_score < 0:
			return 'negative'
		else:
			return 'neutral'
				# Initialize counters
	positive_count = 0
	negative_count = 0
	neutral_count = 0
				# Iterate through the fetched articles and perform sentiment analysis
	for article in k:
	    sentiment = analyze_sentiment(article['description'])
	    if sentiment == 'positive':
	    	positive_count += 1
	    elif sentiment == 'negative':
	    	negative_count += 1
	    else:
	    	neutral_count += 1
	ms="sentiment"
	positive="Positive "+"("+str(positive_count)+")"
	negative="Negative "+"("+str(negative_count)+")"
	neutral="Neutral "+"("+str(neutral_count)+")"

	labels=[positive,negative,neutral]
	values=[positive_count,negative_count,neutral_count]
	fig1= go.Figure(data=[go.Pie(labels=labels,values=values)])
	title="Sentiment Analysis"
	fig1.update_layout(title_text=title, paper_bgcolor='#081108',
        font_color='white')
	graph1=fig1.to_html()

	return render(request,'sun.html',{'graph':graph,'p':p,'d':data,'k':k,'graph1':graph1})

def tcs(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	start=2024
	end=2024
	def get_first_day_of_january_start(year):
		return datetime.date(year, 1, 1)

	def get_first_day_of_january_end(year):
		return datetime.date(year, 12, 31)

	start_date = get_first_day_of_january_start(start)
	end_date = get_first_day_of_january_end(end)

	def parse_csv(file_path):
		with open(file_path, 'r') as file:
			reader = csv.DictReader(file)
			data = [row for row in reader]
		return data

	st="TCS"			
	df= yf.download(tickers="TCS.NS", start=start_date, end=end_date)
	df.to_csv('statics/TCS.NS.csv')
	df=pd.read_csv('statics/TCS.NS.csv',parse_dates=['Date'])
	df['Date']=df['Date'].dt.strftime('%Y-%m-%d')
	p='TCS.NS.csv'
	print('data',df)
	json_records = df.reset_index().to_json(orient ='records') 
	data = [] 
	data = json.loads(json_records) 
	fig = go.Figure(data=[go.Candlestick(x=df['Date'],
		open=df['Open'],
		high=df['High'],
		low=df['Low'],
		close=df['Close'])])
	fig.update_layout(
		plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		paper_bgcolor='rgba(8, 17, 8, 0.9)',
		font=dict(color='#00d094'),
		)
	graph=fig.to_html()
					
	query="latest news for the stock TCS"					
	newsapi=NewsApiClient(api_key='40f8fa21da67431885edfaec3fa49ac4')
	json_data= newsapi.get_everything(q=query,language='en',
		from_param=str(date.today()-datetime.timedelta(days=29)),
		to=str(date.today()),page_size=12,page=1,sort_by='relevancy')
	k=json_data['articles']

	def analyze_sentiment(text):
		blob = TextBlob(text)
		sentiment_score = blob.sentiment.polarity
		if sentiment_score > 0:
			return 'positive'
		elif sentiment_score < 0:
			return 'negative'
		else:
			return 'neutral'
				# Initialize counters
	positive_count = 0
	negative_count = 0
	neutral_count = 0
				# Iterate through the fetched articles and perform sentiment analysis
	for article in k:
	    sentiment = analyze_sentiment(article['description'])
	    if sentiment == 'positive':
	    	positive_count += 1
	    elif sentiment == 'negative':
	    	negative_count += 1
	    else:
	    	neutral_count += 1
	ms="sentiment"
	positive="Positive "+"("+str(positive_count)+")"
	negative="Negative "+"("+str(negative_count)+")"
	neutral="Neutral "+"("+str(neutral_count)+")"

	labels=[positive,negative,neutral]
	values=[positive_count,negative_count,neutral_count]
	fig1= go.Figure(data=[go.Pie(labels=labels,values=values)])
	title="Sentiment Analysis"
	fig1.update_layout(title_text=title, paper_bgcolor='#081108',
        font_color='white')
	graph1=fig1.to_html()

	return render(request,'tcs.html',{'graph':graph,'p':p,'d':data,'k':k,'graph1':graph1})



def stnews(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	newsapi=NewsApiClient(api_key='40f8fa21da67431885edfaec3fa49ac4')
	json_data= newsapi.get_everything(q='Indian Stock Exchange National Stock Exchange',language='en',
		from_param=str(date.today()-datetime.timedelta(days=29)),
		to=str(date.today()),page_size=18,page=1,sort_by='relevancy')
	k=json_data['articles']
	return render(request,'stnews.html',{'k':k})


def sentiment(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		newsapi=NewsApiClient(api_key='40f8fa21da67431885edfaec3fa49ac4')
		st_1= str(request.POST.get('stock'))
		st="latest news for the stock "+st_1
		if st_1=="Select the Stock":
			msg="Please Select the Stock"
			return render(request,'sentiment.html',{'msg':msg,'st_1':st_1})
		else:
			print("stock"+st)
			json_data= newsapi.get_everything(q=st,language='en',
				from_param=str(date.today()-datetime.timedelta(days=29)),
				to=str(date.today()),page_size=18,page=1,sort_by='relevancy')
			k=json_data['articles']
			def analyze_sentiment(text):
				blob = TextBlob(text)
				sentiment_score = blob.sentiment.polarity
				if sentiment_score > 0:
					return 'positive'
				elif sentiment_score < 0:
					return 'negative'
				else:
					return 'neutral'
				# Initialize counters
			positive_count = 0
			negative_count = 0
			neutral_count = 0
				# Iterate through the fetched articles and perform sentiment analysis
			for article in k:
			    sentiment = analyze_sentiment(article['description'])
			    if sentiment == 'positive':
				    positive_count += 1
			    elif sentiment == 'negative':
				    negative_count += 1
			    else:
				    neutral_count += 1
			ms="sentiment"
			positive="Positive "+"("+str(positive_count)+")"
			negative="Negative "+"("+str(negative_count)+")"
			neutral="Neutral "+"("+str(neutral_count)+")"

			labels=[positive,negative,neutral]
			values=[positive_count,negative_count,neutral_count]
			fig= go.Figure(data=[go.Pie(labels=labels,values=values)])
			title="Sentiment Analysis of the "+st_1
			fig.update_layout(title_text=title, paper_bgcolor='rgba(30, 30, 30, 0.5)',
                font_color='white')
			graph=fig.to_html()
			ms= 1
			return render(request,'sentiment.html',{"p":positive_count,"n":negative_count,"nt":neutral_count,"ms":ms,"graph":graph,"st_1":st_1})
	else:
		return render(request,'sentiment.html')
# def stock_csv(request):
# 	p='stock.csv'
# 	return FileResponse(open(p),'rb')
#rgb(35,35,35)
def stock_csv(request):

    # Path to your CSV file within the static directory
    csv_file_path = 'stock.csv'
   
    # Read the CSV file
    with open(csv_file_path, 'r') as file:
        csv_data = file.read()
   
    # Return CSV data as HTTP response
    response = HttpResponse(csv_data, content_type='text/csv')
    response['Content-Disposition'] = 'inline; filename=file.csv'
    return response


def live(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		import csv
		st=str(request.POST.get('stock'))
		start1=request.POST.get('start')
		end1=request.POST.get('end')
		if start1 is None or start1 == '' or start1 == "Select the Start Year" or end1 is None or end1 == '' or end1 == "Select the End Year" or st=="Select the Stock":
			msg="Please select all the fields"
			return render(request, 'live.html', {'msg': msg})
		else:
			start=int(start1)
			end=int(end1)
			def get_first_day_of_january_start(year):
				return datetime.date(year, 1, 1)

			def get_first_day_of_january_end(year):
				return datetime.date(year, 12, 31)

			start_date = get_first_day_of_january_start(start)
			end_date = get_first_day_of_january_end(end)


			def parse_csv(file_path):
				with open(file_path, 'r') as file:
					reader = csv.DictReader(file)
					data = [row for row in reader]
				return data

			if st == "SBIN":
				
				df= yf.download(tickers="SBIN.NS", start=start_date, end=end_date)

				df.to_csv('statics/SBIN.NS.csv')
				df=pd.read_csv('statics/SBIN.NS.csv',parse_dates=['Date'])
				df['Date']=df['Date'].dt.strftime('%Y-%m-%d')

				p='SBIN.NS.csv'
				print('data',df)
				json_records = df.reset_index().to_json(orient ='records') 
				data = [] 
				data = json.loads(json_records) 
				return render(request, 'live.html', {'p': p,'d':data})
				

			elif st == "BAJFINANCE":
				
				df= yf.download(tickers="BAJFINANCE.NS", start=start_date, end=end_date)

				df.to_csv('statics/BAJFINANCE.NS.csv')
				df=pd.read_csv('statics/BAJFINANCE.NS.csv',parse_dates=['Date'])
				df['Date']=df['Date'].dt.strftime('%Y-%m-%d')

				p='BAJFINANCE.NS.csv'
				print('data',df)
				json_records = df.reset_index().to_json(orient ='records') 
				data = [] 
				data = json.loads(json_records) 
				return render(request, 'live.html', {'p': p,'d':data})
				

			elif st == "HDFCBANK":
				
				df= yf.download(tickers="HDFCBANK.NS", start=start_date, end=end_date)

				df.to_csv('statics/HDFCBANK.NS.csv')
				df=pd.read_csv('statics/HDFCBANK.NS.csv',parse_dates=['Date'])
				df['Date']=df['Date'].dt.strftime('%Y-%m-%d')

				p='HDFCBANK.NS.csv'
				print('data',df)
				json_records = df.reset_index().to_json(orient ='records') 
				data = [] 
				data = json.loads(json_records) 
				return render(request, 'live.html', {'p': p,'d':data})




			elif st == "ICICIBANK":
				
				df= yf.download(tickers="ICICIBANK.NS", start=start_date, end=end_date)

				df.to_csv('statics/ICICIBANK.NS.csv')
				df=pd.read_csv('statics/ICICIBANK.NS.csv',parse_dates=['Date'])
				df['Date']=df['Date'].dt.strftime('%Y-%m-%d')

				p='ICICIBANK.NS.csv'
				print('data',df)
				json_records = df.reset_index().to_json(orient ='records') 
				data = [] 
				data = json.loads(json_records) 
				return render(request, 'live.html', {'p': p,'d':data})


			elif st == "INFY":
				
				df= yf.download(tickers="INFY.NS", start=start_date, end=end_date)

				df.to_csv('statics/INFY.NS.csv')
				df=pd.read_csv('statics/INFY.NS.csv',parse_dates=['Date'])
				df['Date']=df['Date'].dt.strftime('%Y-%m-%d')

				p='INFY.NS.csv'
				print('data',df)
				json_records = df.reset_index().to_json(orient ='records') 
				data = [] 
				data = json.loads(json_records) 
				return render(request, 'live.html', {'p': p,'d':data})



			elif st == "ITC":
				
				df= yf.download(tickers="ITC.NS", start=start_date, end=end_date)

				df.to_csv('statics/ITC.NS.csv')
				df=pd.read_csv('statics/ITC.NS.csv',parse_dates=['Date'])
				df['Date']=df['Date'].dt.strftime('%Y-%m-%d')

				p='ITC.NS.csv'
				print('data',df)
				json_records = df.reset_index().to_json(orient ='records') 
				data = [] 
				data = json.loads(json_records) 
				return render(request, 'live.html', {'p': p,'d':data})




			elif st == "RELIANCE":
				
				df= yf.download(tickers="RELIANCE.NS", start=start_date, end=end_date)

				df.to_csv('statics/RELIANCE.NS.csv')
				df=pd.read_csv('statics/RELIANCE.NS.csv',parse_dates=['Date'])
				df['Date']=df['Date'].dt.strftime('%Y-%m-%d')

				p='RELIANCE.NS.csv'
				print('data',df)
				json_records = df.reset_index().to_json(orient ='records') 
				data = [] 
				data = json.loads(json_records) 
				return render(request, 'live.html', {'p': p,'d':data})



			elif st == "SUNPHARMA":
				
				df= yf.download(tickers="SUNPHARMA.NS", start=start_date, end=end_date)

				df.to_csv('statics/SUNPHARMA.NS.csv')
				df=pd.read_csv('statics/SUNPHARMA.NS.csv',parse_dates=['Date'])
				df['Date']=df['Date'].dt.strftime('%Y-%m-%d')

				p='SUNPHARMA.NS.csv'
				print('data',df)
				json_records = df.reset_index().to_json(orient ='records') 
				data = [] 
				data = json.loads(json_records) 
				return render(request, 'live.html', {'p': p,'d':data})


			elif st == "TATAMOTORS":
				
				df= yf.download(tickers="TATAMOTORS.NS", start=start_date, end=end_date)

				df.to_csv('statics/TATAMOTORS.NS.csv')
				df=pd.read_csv('statics/TATAMOTORS.NS.csv',parse_dates=['Date'])
				df['Date']=df['Date'].dt.strftime('%Y-%m-%d')

				p='TATAMOTORS.NS.csv'
				print('data',df)
				json_records = df.reset_index().to_json(orient ='records') 
				data = [] 
				data = json.loads(json_records) 
				return render(request, 'live.html', {'p': p,'d':data})

			elif st == "TCS":
				
				df= yf.download(tickers="TCS.NS", start=start_date, end=end_date)

				df.to_csv('statics/TCS.NS.csv')
				df=pd.read_csv('statics/TCS.NS.csv',parse_dates=['Date'])
				df['Date']=df['Date'].dt.strftime('%Y-%m-%d')

				p='TCS.NS.csv'
				print('data',df)
				json_records = df.reset_index().to_json(orient ='records') 
				data = [] 
				data = json.loads(json_records) 
				return render(request, 'live.html', {'p': p,'d':data})

			else:
				msg="Please select the stock"
				return render(request, 'live.html', {'msg':msg})
	else:
		return render(request,'live.html')

		"""
		if st=="ITC":
			
			data= yf.download(tickers="SBIN.NS", start="1900-01-01", end="2023-12-31")
			data.to_csv('statics/SBIN.NS.csv')
			k=data.to_html()
			f='statics/SBIN.NS.csv'
		elif st=="TCS":
			df = pd.read_csv('TCS.csv',parse_dates=['Date'])


		elif st=="TATAMOTORS":
			df = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

		elif st=="SUNPHARMA":
			df = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

		elif st=="SBIN":
			df = pd.read_csv('SBIN.csv',parse_dates=['Date'])

		elif st=="INFY":
			df = pd.read_csv('INFY.csv',parse_dates=['Date'])

		elif st=="ICICIBANK":
			df = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

		elif st=="HDFCBANK":
			df = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

		elif st=="BAJFINANCE":
			df = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

		else:
			message="Select one of the stock from the list"

		return render(request,'live.html',{'f':f,'k':k})

		"""


def dashboard(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	user=userregister.objects.get(email=request.session['email'])
	return render(request,'dashboard.html',{'user':user})

def ques(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	return render(request,'ques.html')

def ques_2(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	return render(request,'ques_2.html')

def ques_3(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	return render(request,'ques_3.html')

def ques_candle(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	return render(request,'ques_candle.html')

def allyears(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		atype=request.POST.get('atype')
		st=str(request.POST.get('stock'))
		print(atype)
		if atype=="Select the Price" or st=="Select the Stock":
			msg="PLEASE SELECT BOTH THE FIELDS"
			if atype=="Select the Price" and st=="Select the Stock":
				msg=msg
				return render(request,'allyears.html',{'msg':msg})
			elif atype=="Select the Price":
				msg="PLEASE SELECT THE PRICE"
				return render(request,'allyears.html',{'msg':msg,'st':st,'atype':atype})
			else:
				msg="PLEASE SELECT THE STOCK"
				return render(request,'allyears.html',{'msg':msg,'atype':atype,'st':st})

		else:
			if st=="RELIANCE":
				df = pd.read_csv('RELIANCE.csv',parse_dates=['Date'])

			elif st=="BAJFINANCE":
				df = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			elif st=="TATAMOTORS":
				df = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st=="ITC":
				df = pd.read_csv('ITC.csv',parse_dates=['Date'])

			elif st=="TCS":
				df = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st=="SUNPHARMA":
				df = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st=="SBIN":
				df = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st=="INFY":
				df = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st=="ICICIBANK":
				df = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st=="HDFCBANK":
				df = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			else:
				message="None is selected"

			title=atype+' price analysis of all years'
			fig = px.line(df, x="Date", y=atype, title=title)
			fig.update_layout(
		        plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		        paper_bgcolor='rgba(8, 17, 8, 0.9)',
		   	    font=dict(color='#00d094'), 
		    )
			graph=fig.to_html()
			msg=1
			return render(request,'allyears.html',{'graph':graph,'atype':atype,'st':st,'msg':msg})
	else:
		return render(request,'allyears.html')

def year(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		atype=request.POST.get('atype')
		st=request.POST.get('stock')
		year1=request.POST.get('year')
		if st=="Select the Stock" or atype=="Select the Price" or year1 is None or year1=='':
			msg="PLEASE SELECT ALL THE FIELDS"
			return render(request,'year.html',{'msg':msg})
		else:
			year=int(year1)
			if st=="RELIANCE":
				df = pd.read_csv('RELIANCE.csv',parse_dates=['Date'])

			elif st=="BAJFINANCE":
				df = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			elif st=="TATAMOTORS":
				df = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st=="ITC":
				df = pd.read_csv('ITC.csv',parse_dates=['Date'])

			elif st=="TCS":
				df = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st=="SUNPHARMA":
				df = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st=="SBIN":
				df = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st=="INFY":
				df = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st=="ICICIBANK":
				df = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st=="HDFCBANK":
				df = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			else:
				message="None is selected"
					
			df['Year']=df['Date'].dt.year
			title=atype+' Price analysis of the year '+ str(year)
			df1=df[df['Year']==year]
			fig = px.line(df1, x="Date", y=atype, title=title)
			fig.update_layout(
			    plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
			    paper_bgcolor='rgba(8, 17, 8, 0.9)',
			    font=dict(color='#00d094'),
		    )
			graph=fig.to_html()
			return render(request,'year.html',{'graph':graph,'st':st})
	else:
		return render(request,'year.html')

def month(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		atype=request.POST.get('atype')
		year1=request.POST.get('year')
		month1=request.POST.get('month')
		st=request.POST.get('stock')
		if st=="Select the Stock" or atype=="Select the Price" or year1 is None or year1=='' or month1=="Select the Month":
			msg="PLEASE SELECT ALL THE FIELDS"
			return render(request,'month.html',{'msg':msg})
		else:
			year=int(year1)
			month=int(month1)
			print(atype)
			if st=="RELIANCE":
				df = pd.read_csv('RELIANCE.csv',parse_dates=['Date'])

			elif st=="BAJFINANCE":
				df = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			elif st=="TATAMOTORS":
				df = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st=="ITC":
				df = pd.read_csv('ITC.csv',parse_dates=['Date'])

			elif st=="TCS":
				df = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st=="SUNPHARMA":
				df = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st=="SBIN":
				df = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st=="INFY":
				df = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st=="ICICIBANK":
				df = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st=="HDFCBANK":
				df = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			else:
				message="None is selected"
				
			df['Year']=df['Date'].dt.year
			df['Month']=df['Date'].dt.month
			df1=df[df['Year']==year]
			df2=df1[df1['Month']==month]
			if month==1:
				month="January"
			if month==2:
				month="February"
			if month==3:
				month="March"
			if month==4:
				month="April"
			if month==5:
				month="May"
			if month==6:
				month="June"
			if month==7:
				month="July"
			if month==8:
				month="August"
			if month==9:
				month="September"
			if month==10:
				month="October"
			if month==11:
				month="November"
			if month==12:
				month="December"
			title=atype+' Price analysis of the '+month+ " ("+ str(year)+")"
			fig = px.line(df2, x="Date", y=atype, title=title)
			fig.update_layout(
	            plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
	            paper_bgcolor='rgba(8, 17, 8, 0.9)',
	            font=dict(color='#00d094'),
	        )
			graph=fig.to_html()
			return render(request,'month.html',{'graph':graph,'st':st})
	else:
		return render(request,'month.html')


def range(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		atype=request.POST.get('atype')
		st=request.POST.get('stock')
		start1=request.POST.get('start')
		end1=request.POST.get('end')
		if st=="Select the Stock" or atype=="Select the Price" or start1 is None or start1=='' or end1 is None or end1=='':
			msg="PLEASE SELECT ALL THE FIELDS"
			return render(request,'range.html',{'msg':msg})
		else:
			start=int(start1)
			end=int(end1)
			if st=="RELIANCE":
				df = pd.read_csv('RELIANCE.csv',parse_dates=['Date'])

			elif st=="BAJFINANCE":
				df = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			elif st=="TATAMOTORS":
				df = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st=="ITC":
				df = pd.read_csv('ITC.csv',parse_dates=['Date'])

			elif st=="TCS":
				df = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st=="SUNPHARMA":
				df = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st=="SBIN":
				df = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st=="INFY":
				df = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st=="ICICIBANK":
				df = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st=="HDFCBANK":
				df = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			else:
				message="None is selected"
					
			df['Year']=df['Date'].dt.year
			title=atype+' Price analysis from the year '+ str(start) + ' to '+ str(end)
			df1= df[(df['Year']>=start) & (df['Year']<=end)]
			fig = px.line(df1, x="Date", y=atype, title=title)
			fig.update_layout(
			    plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
			    paper_bgcolor='rgba(8, 17, 8, 0.9)',
			    font=dict(color='#00d094'),
		    )
			graph=fig.to_html()
			return render(request,'range.html',{'graph':graph,'st':st})
	else:
		return render(request,'range.html')
	

def candle(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		st=request.POST.get('stock')
		if st=="Select the Stock":
			msg="PLEASE SELECT THE STOCK"
			return render(request,'candle.html',{'msg':msg})
		else:
			if st=="RELIANCE":
				df = pd.read_csv('RELIANCE.csv',parse_dates=['Date'])

			elif st=="BAJFINANCE":
				df = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			elif st=="TATAMOTORS":
				df = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st=="ITC":
				df = pd.read_csv('ITC.csv',parse_dates=['Date'])

			elif st=="TCS":
				df = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st=="SUNPHARMA":
				df = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st=="SBIN":
				df = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st=="INFY":
				df = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st=="ICICIBANK":
				df = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st=="HDFCBANK":
				df = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			else:
				message="None is selected"
			fig = go.Figure(data=[go.Candlestick(x=df['Date'],
				open=df['Open'],
		        high=df['High'],
		        low=df['Low'],
		        close=df['Close'])])
			fig.update_layout(
		        plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		        paper_bgcolor='rgba(8, 17, 8, 0.9)',
		        font=dict(color='#00d094'),
		        )
			graph=fig.to_html()
			return render(request,'candle.html',{'graph':graph,'st':st})
	else:
		return render(request,'candle.html')



def candle_year(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		st=request.POST.get('stock')
		year1=request.POST.get('year')
		if year1 is None or year1=='' or st=="Select the Stock":
			msg="PLEASE SELECT BOTH THE FIELDS"
			return render(request,'candle_year.html',{'msg':msg})
		else:
			year=int(year1)
			if st=="RELIANCE":
				df = pd.read_csv('RELIANCE.csv',parse_dates=['Date'])

			elif st=="BAJFINANCE":
				df = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			elif st=="TATAMOTORS":
				df = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st=="ITC":
				df = pd.read_csv('ITC.csv',parse_dates=['Date'])

			elif st=="TCS":
				df = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st=="SUNPHARMA":
				df = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st=="SBIN":
				df = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st=="INFY":
				df = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st=="ICICIBANK":
				df = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st=="HDFCBANK":
				df = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			else:
				message="None is selected"
			df['Year']=df['Date'].dt.year
			df1=df[df['Year']==year]
			fig = go.Figure(data=[go.Candlestick(x=df1['Date'],
		            open=df1['Open'],
		            high=df1['High'],
		            low=df1['Low'],
		            close=df1['Close'])])
			fig.update_layout(
		        plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		        paper_bgcolor='rgba(8, 17, 8, 0.9)',
		        font=dict(color='#00d094'),
		        )
			graph=fig.to_html()

			return render(request,'candle_year.html',{'graph':graph,'st':st})
	else:
		return render(request,'candle_year.html')

def comp_2(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		atype=request.POST.get('atype')
		st1=str(request.POST.get('stock1'))
		st2=str(request.POST.get('stock2'))
		print(atype)
		if atype=="Select the Price" or st1=="Select the Stock One" or st2=="Select the Stock Two":
			msg="Please select all the fields"
			return render(request,'comp_2.html',{'msg':msg})
		else:
			if st1=="RELIANCE":
				df = pd.read_csv('RELIANCE.csv',parse_dates=['Date'])

			elif st1=="BAJFINANCE":
				df = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			elif st1=="TATAMOTORS":
				df = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st1=="ITC":
				df = pd.read_csv('ITC.csv',parse_dates=['Date'])

			elif st1=="TCS":
				df = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st1=="SUNPHARMA":
				df = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st1=="SBIN":
				df = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st1=="INFY":
				df = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st1=="ICICIBANK":
				df = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st1=="HDFCBANK":
				df = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			else:
				message="None is selected"


			if st2=="ITC":
				df1 = pd.read_csv('ITC.csv',parse_dates=['Date'])
			elif st2=="TCS":
				df1 = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st2=="TATAMOTORS":
				df1 = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st2=="SUNPHARMA":
				df1 = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st2=="SBIN":
				df1 = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st2=="INFY":
				df1 = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st2=="ICICIBANK":
				df1 = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st2=="HDFCBANK":
				df1 = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			elif st2=="BAJFINANCE":
				df1 = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			else:
				message="None is selected"

			stock1 = df[atype]
			stock2 = df1[atype]
			trace1 = go.Scatter(x=df['Date'], y=stock1, mode='lines', name=st1)
			trace2 = go.Scatter(x=df1['Date'], y=stock2, mode='lines', name=st2)

			title=atype+" price analysis of the "+st1+" and "+st2
			layout = go.Layout(title=title,
				xaxis=dict(title='Date'),
			    yaxis=dict(title=atype))

			fig = go.Figure([trace1, trace2], layout)
			fig.update_layout(
	            plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
	            paper_bgcolor='rgba(8, 17, 8, 0.9)',
	            font=dict(color='#00d094'), 
	        )
			graph=fig.to_html()

			return render(request,'comp_2.html',{'graph':graph})
	else:
		return render(request,'comp_2.html')


def compyear_2(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		atype=request.POST.get('atype')
		year1=request.POST.get('year')
		st_1=str(request.POST.get('stock1'))
		st_2=str(request.POST.get('stock2'))
		print(atype)
		if atype=="Select the Price" or st_1=="Select the Stock One" or st_2=="Select the Stock Two" or year1=="Select the Year":
			msg="Please select all the fields"
			return render(request,'compyear_2.html',{'msg':msg})
		else:
			year=int(year1)
			if st_1=="RELIANCE":
				df = pd.read_csv('RELIANCE.csv',parse_dates=['Date'])

			elif st_1=="BAJFINANCE":
				df = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			elif st_1=="TATAMOTORS":
				df = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_1=="ITC":
				df = pd.read_csv('ITC.csv',parse_dates=['Date'])

			elif st_1=="TCS":
				df = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_1=="SUNPHARMA":
				df = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_1=="SBIN":
				df = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_1=="INFY":
				df = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_1=="ICICIBANK":
				df = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_1=="HDFCBANK":
				df = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			else:
				message="None is selected"


			if st_2=="ITC":
				df1 = pd.read_csv('ITC.csv',parse_dates=['Date'])
			elif st_2=="TCS":
				df1 = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_2=="TATAMOTORS":
				df1 = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_2=="SUNPHARMA":
				df1 = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_2=="SBIN":
				df1 = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_2=="INFY":
				df1 = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_2=="ICICIBANK":
				df1 = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_2=="HDFCBANK":
				df1 = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			elif st_2=="BAJFINANCE":
				df1 = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			else:
				message="None is selected"
			
			stock1 = df[atype]
			stock2 = df1[atype]
			df['Year']=df['Date'].dt.year
			df1['Year']=df1['Date'].dt.year
			st1=df[df['Year']==year]
			st2=df1[df1['Year']==year]
			if len(st1)==0 or len(st2)==0:
				error="YEAR MUST INCLUDE IN BOTH THE STOCKS"
				return render(request,'compyear_2.html',{'error':error})
			else:

				trace1 = go.Scatter(x=st1['Date'], y=stock1, mode='lines', name=st_1)
				trace2 = go.Scatter(x=st2['Date'], y=stock2, mode='lines', name=st_2)

				title=atype+" price analysis of "+st_1+" and "+st_2+" of the year "+str(year)
				layout = go.Layout(title= title,
					xaxis=dict(title='Date'),
	                yaxis=dict(title=atype))

				fig = go.Figure([trace1, trace2], layout)
				fig.update_layout(
		            plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		            paper_bgcolor='rgba(8, 17, 8, 0.9)',
		            font=dict(color='#00d094'),
		        )
				graph=fig.to_html()

				return render(request,'compyear_2.html',{'graph':graph})
	else:
		return render(request,'compyear_2.html')


def compmonth_2(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		atype=request.POST.get('atype')
		year1=request.POST.get('year')
		month1=request.POST.get('month')
		st_1=str(request.POST.get('stock1'))
		st_2=str(request.POST.get('stock2'))
		print(atype)
		if atype=="Select the Price" or st_1=="Select the Stock One" or st_2=="Select the Stock Two" or year1 =="Select the Year" or month1=="Select the Month":
			msg="Please select all the fields"
			return render(request,'compmonth_2.html',{'msg':msg})
		else:
			year=int(year1)
			month=int(month1)
			if st_1=="RELIANCE":
				df = pd.read_csv('RELIANCE.csv',parse_dates=['Date'])

			elif st_1=="BAJFINANCE":
				df = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			elif st_1=="TATAMOTORS":
				df = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_1=="ITC":
				df = pd.read_csv('ITC.csv',parse_dates=['Date'])

			elif st_1=="TCS":
				df = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_1=="SUNPHARMA":
				df = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_1=="SBIN":
				df = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_1=="INFY":
				df = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_1=="ICICIBANK":
				df = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_1=="HDFCBANK":
				df = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			else:
				message="None is selected"


			if st_2=="ITC":
				df1 = pd.read_csv('ITC.csv',parse_dates=['Date'])
			elif st_2=="TCS":
				df1 = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_2=="TATAMOTORS":
				df1 = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_2=="SUNPHARMA":
				df1 = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_2=="SBIN":
				df1 = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_2=="INFY":
				df1 = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_2=="ICICIBANK":
				df1 = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_2=="HDFCBANK":
				df1 = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			elif st_2=="BAJFINANCE":
				df1 = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			else:
				message="None is selected"


			stock1 = df[atype]
			stock2 = df1[atype]
					
			df['Year']=df['Date'].dt.year
			df['Month']=df['Date'].dt.month
			df_1=df[df['Year']==year]
			df_2=df_1[df_1['Month']==month]



			df1['Year']=df1['Date'].dt.year
			df1['Month']=df1['Date'].dt.month
			df1_1=df1[df1['Year']==year]
			df1_2=df1_1[df1_1['Month']==month]
			if len(df_2)==0 or len(df1_2)==0:
				error="*YEAR MUST INCLUDE IN BOTH THE STOCKS"
				print(error)
				return render(request,'compmonth_2.html',{'error':error})
			else:
				trace1 = go.Scatter(x=df_2['Date'], y=stock1, mode='lines', name=st_1)
				trace2 = go.Scatter(x=df1_2['Date'], y=stock2, mode='lines', name=st_2)
				if month==1:
					month="January"
				if month==2:
					month="February"
				if month==3:
					month="March"
				if month==4:
					month="April"
				if month==5:
					month="May"
				if month==6:
					month="June"
				if month==7:
					month="July"
				if month==8:
					month="August"
				if month==9:
					month="September"
				if month==10:
					month="October"
				if month==11:
					month="November"
				if month==12:
					month="December"
				title=atype+' Price analysis of the '+st_1+" and "+st_2+" of "+month+ " ("+ str(year)+")"

				layout = go.Layout(title=title,
					xaxis=dict(title='Date'),
					yaxis=dict(title=atype))
				fig = go.Figure([trace1, trace2], layout)
				fig.update_layout(
		            plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		            paper_bgcolor='rgba(8, 17, 8, 0.9)',
		            font=dict(color='#00d094'),
		        )
				graph=fig.to_html()

				return render(request,'compmonth_2.html',{'graph':graph})
	else:
		return render(request,'compmonth_2.html')


def comprange_2(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		atype=request.POST.get('atype')
		st_1=str(request.POST.get('stock1'))
		st_2=str(request.POST.get('stock2'))
		start1=request.POST.get('start')
		end1=request.POST.get('end')
		if st_1=="Select the Stock One" or st_2=="Select the Stock Two" or atype=="Select the Price" or start1 is None or start1=='' or end1 is None or end1=='':
			msg="Please select all the fields"
			return render(request,'comprange_2.html',{'msg':msg})
		else:
			start=int(start1)
			end=int(end1)
			if st_1=="RELIANCE":
				df = pd.read_csv('RELIANCE.csv',parse_dates=['Date'])

			elif st_1=="BAJFINANCE":
				df = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			elif st_1=="TATAMOTORS":
				df = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_1=="ITC":
				df = pd.read_csv('ITC.csv',parse_dates=['Date'])

			elif st_1=="TCS":
				df = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_1=="SUNPHARMA":
				df = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_1=="SBIN":
				df = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_1=="INFY":
				df = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_1=="ICICIBANK":
				df = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_1=="HDFCBANK":
				df = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			else:
				message="None is selected"


			if st_2=="ITC":
				df1 = pd.read_csv('ITC.csv',parse_dates=['Date'])
			elif st_2=="TCS":
				df1 = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_2=="TATAMOTORS":
				df1 = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_2=="SUNPHARMA":
				df1 = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_2=="SBIN":
				df1 = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_2=="INFY":
				df1 = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_2=="ICICIBANK":
				df1 = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_2=="HDFCBANK":
				df1 = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			elif st_2=="BAJFINANCE":
				df1 = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			else:
				message="None is selected"
			df['Year']=df['Date'].dt.year
			df1['Year']=df1['Date'].dt.year
			df_st= df[(df['Year']>=start) & (df['Year']<=end)]
			df1_st1= df1[(df1['Year']>=start) & (df1['Year']<=end)]
			stock1 = df_st[atype]
			stock2 = df1_st1[atype]
			if len(df_st)==0 or len(df1_st1)==0:
				error="YEAR MUST INCLUDE IN BOTH THE STOCKS"
				return render(request,'comprange_2.html',{'error':error})
			else:
				trace1 = go.Scatter(x=df_st['Date'], y=stock1, mode='lines', name=st_1)
				trace2 = go.Scatter(x=df1_st1['Date'], y=stock2, mode='lines', name=st_2)
				title=atype+" price analysis from "+str(start)+" to "+str(end)+" of "+st_1+" and "+st_2
				layout = go.Layout(title=title,
					xaxis=dict(title='Date'),
					yaxis=dict(title=atype))
				fig = go.Figure([trace1, trace2], layout)
				fig.update_layout(
		            plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		            paper_bgcolor='rgba(8, 17, 8, 0.9)',
		            font=dict(color='#00d094'),
		        )
				graph=fig.to_html()
				return render(request,'comprange_2.html',{'graph':graph})

	else:
		return render(request,'comprange_2.html')

def comp_3(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		atype=request.POST.get('atype')
		print(atype)
		st_1=str(request.POST.get('stock1'))
		st_2=str(request.POST.get('stock2'))
		st_3=str(request.POST.get('stock3'))

		if atype=="Select the Price" or st_1=="Select the Stock One" or st_2=="Select the Stock Two" or st_3=="Select the Stock Three":
			msg="Please select all the fields"
			return render(request,'comp_3.html',{'msg':msg})
		else:
			if st_1=="RELIANCE":
				df = pd.read_csv('RELIANCE.csv',parse_dates=['Date'])

			elif st_1=="BAJFINANCE":
				df = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			elif st_1=="TATAMOTORS":
				df = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_1=="ITC":
				df = pd.read_csv('ITC.csv',parse_dates=['Date'])

			elif st_1=="TCS":
				df = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_1=="SUNPHARMA":
				df = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_1=="SBIN":
				df = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_1=="INFY":
				df = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_1=="ICICIBANK":
				df = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_1=="HDFCBANK":
				df = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			else:
				message="None is selected"


			if st_2=="ITC":
				df1 = pd.read_csv('ITC.csv',parse_dates=['Date'])
			elif st_2=="TCS":
				df1 = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_2=="TATAMOTORS":
				df1 = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_2=="SUNPHARMA":
				df1 = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_2=="SBIN":
				df1 = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_2=="INFY":
				df1 = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_2=="ICICIBANK":
				df1 = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_2=="HDFCBANK":
				df1 = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			elif st_2=="BAJFINANCE":
				df1 = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			else:
				message="None is selected"


			if st_3=="ITC":
				df2 = pd.read_csv('ITC.csv',parse_dates=['Date'])
			elif st_3=="TCS":
				df2 = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_3=="TATAMOTORS":
				df2 = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_3=="SUNPHARMA":
				df2 = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_3=="SBIN":
				df2 = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_3=="INFY":
				df2 = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_3=="ICICIBANK":
				df2 = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_3=="HDFCBANK":
				df2 = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			elif st_3=="BAJFINANCE":
				df2 = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])
			else:
				message="None is selected"


			stock = df[atype]
			stock1 = df1[atype]
			stock2 = df2[atype]
			trace1 = go.Scatter(x=df['Date'], y=stock, mode='lines', name=st_1)
			trace2 = go.Scatter(x=df1['Date'], y=stock1, mode='lines', name=st_2)
			trace3 = go.Scatter(x=df2['Date'], y=stock2, mode='lines', name=st_3)
			title=atype+" price analysis of the "+st_1+" , "+st_2+" and "+st_3
			layout = go.Layout(title=title,
				xaxis=dict(title='Date'),
			    yaxis=dict(title=atype))

			fig = go.Figure([trace1, trace2, trace3], layout)
			fig.update_layout(
	            plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
	            paper_bgcolor='rgba(8, 17, 8, 0.9)',
	            font=dict(color='#00d094'),
	        )
			graph=fig.to_html()
			return render(request,'comp_3.html',{'graph':graph})
	else:
		return render(request,'comp_3.html')

def compyear_3(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		atype=request.POST.get('atype')
		st_1=str(request.POST.get('stock1'))
		st_2=str(request.POST.get('stock2'))
		st_3=str(request.POST.get('stock3'))
		year1=request.POST.get('year')
		print(atype)
		if atype=="Select the Price" or st_1=="Select the Stock One" or st_2=="Select the Stock Two" or st_3=="Select the Stock Three" or year1=="Select the Year":
			msg="Please select all the fields"
			return render(request,'compyear_3.html',{'msg':msg})
		else:
			year=int(year1)
			if st_1=="RELIANCE":
				df = pd.read_csv('RELIANCE.csv',parse_dates=['Date'])

			elif st_1=="BAJFINANCE":
				df = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			elif st_1=="TATAMOTORS":
				df = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_1=="ITC":
				df = pd.read_csv('ITC.csv',parse_dates=['Date'])

			elif st_1=="TCS":
				df = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_1=="SUNPHARMA":
				df = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_1=="SBIN":
				df = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_1=="INFY":
				df = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_1=="ICICIBANK":
				df = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_1=="HDFCBANK":
				df = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			else:
				message="None is selected"


			if st_2=="ITC":
				df1 = pd.read_csv('ITC.csv',parse_dates=['Date'])
			elif st_2=="TCS":
				df1 = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_2=="TATAMOTORS":
				df1 = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_2=="SUNPHARMA":
				df1 = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_2=="SBIN":
				df1 = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_2=="INFY":
				df1 = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_2=="ICICIBANK":
				df1 = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_2=="HDFCBANK":
				df1 = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			elif st_2=="BAJFINANCE":
				df1 = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			else:
				message="None is selected"


			if st_3=="ITC":
				df2 = pd.read_csv('ITC.csv',parse_dates=['Date'])
			elif st_3=="TCS":
				df2 = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_3=="TATAMOTORS":
				df2 = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_3=="SUNPHARMA":
				df2 = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_3=="SBIN":
				df2 = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_3=="INFY":
				df2 = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_3=="ICICIBANK":
				df2 = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_3=="HDFCBANK":
				df2 = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			elif st_3=="BAJFINANCE":
				df2 = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])
			else:
				message="None is selected"


			stock1 = df[atype]
			stock2 = df1[atype]
			stock3 = df2[atype]

			df['Year']=df['Date'].dt.year
			df1['Year']=df1['Date'].dt.year
			df2['Year']=df2['Date'].dt.year

			st1=df[df['Year']==year]
			st2=df1[df1['Year']==year]
			st3=df2[df2['Year']==year]
			if len(st1)==0 or len(st2)==0 or len(st3)==0:
				error="YEAR MUST INCLUDE IN ALL THE STOCKS"
				return render(request,'compyear_3.html',{'error':error})

			else:
				trace1 = go.Scatter(x=st1['Date'], y=stock1, mode='lines', name=st_1)
				trace2 = go.Scatter(x=st2['Date'], y=stock2, mode='lines', name=st_2)
				trace3 = go.Scatter(x=st3['Date'], y=stock3, mode='lines', name=st_3)

				title=atype+" price analysis of the year "+str(year)+" of "+st_1+" , "+st_2+" and "+st_3
				layout = go.Layout(title=title,
				    xaxis=dict(title='Date'),
	                yaxis=dict(title=atype))

				fig = go.Figure([trace1, trace2, trace3], layout)
				fig.update_layout(
		            plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		            paper_bgcolor='rgba(8, 17, 8, 0.9)',
		            font=dict(color='#00d094'),
		        )
				graph=fig.to_html()

				return render(request,'compyear_3.html',{'graph':graph})

	else:
		return render(request,'compyear_3.html')

def compmonth_3(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		atype=request.POST.get('atype')
		print(atype)
		st_1=str(request.POST.get('stock1'))
		st_2=str(request.POST.get('stock2'))
		st_3=str(request.POST.get('stock3'))

		year1=request.POST.get('year')
		month1=request.POST.get('month')
		if atype=="Select the Price" or st_1=="Select the Stock One" or st_2=="Select the Stock Two" or st_3=="Select the Stock Three" or year1=="Select the Year" or month1=="Select the Month":
			msg="Please select all the fields"
			return render(request,'compmonth_3.html',{'msg':msg})
		else:
			year=int(year1)
			month=int(month1)
			if st_1=="RELIANCE":
				df = pd.read_csv('RELIANCE.csv',parse_dates=['Date'])

			elif st_1=="BAJFINANCE":
				df = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			elif st_1=="TATAMOTORS":
				df = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_1=="ITC":
				df = pd.read_csv('ITC.csv',parse_dates=['Date'])

			elif st_1=="TCS":
				df = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_1=="SUNPHARMA":
				df = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_1=="SBIN":
				df = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_1=="INFY":
				df = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_1=="ICICIBANK":
				df = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_1=="HDFCBANK":
				df = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			else:
				message="None is selected"


			if st_2=="ITC":
				df1 = pd.read_csv('ITC.csv',parse_dates=['Date'])
			elif st_2=="TCS":
				df1 = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_2=="TATAMOTORS":
				df1 = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_2=="SUNPHARMA":
				df1 = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_2=="SBIN":
				df1 = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_2=="INFY":
				df1 = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_2=="ICICIBANK":
				df1 = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_2=="HDFCBANK":
				df1 = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			elif st_2=="BAJFINANCE":
				df1 = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			else:
				message="None is selected"


			if st_3=="ITC":
				df2 = pd.read_csv('ITC.csv',parse_dates=['Date'])
			elif st_3=="TCS":
				df2 = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_3=="TATAMOTORS":
				df2 = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_3=="SUNPHARMA":
				df2 = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_3=="SBIN":
				df2 = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_3=="INFY":
				df2 = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_3=="ICICIBANK":
				df2 = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_3=="HDFCBANK":
				df2 = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			elif st_3=="BAJFINANCE":
				df2 = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])
			else:
				message="None is selected"

			stock1 = df[atype]
			stock2 = df1[atype]
			stock3 = df2[atype]

					
			df['Year']=df['Date'].dt.year
			df['Month']=df['Date'].dt.month
			df_1=df[df['Year']==year]
			df_2=df_1[df_1['Month']==month]



			df1['Year']=df1['Date'].dt.year
			df1['Month']=df1['Date'].dt.month
			df1_1=df1[df1['Year']==year]
			df1_2=df1_1[df1_1['Month']==month]


			df2['Year']=df2['Date'].dt.year
			df2['Month']=df2['Date'].dt.month
			df2_1=df2[df2['Year']==year]
			df2_2=df2_1[df2_1['Month']==month]

			if len(df_1)==0 or len(df1_1)==0 or len(df2_1)==0:
				error="YEAR MUST INCLUDE IN ALL THE STOCKS"
				return render(request,'compyear_3.html',{'error':error})
			else:

				trace1 = go.Scatter(x=df_2['Date'], y=stock1, mode='lines', name=st_1)
				trace2 = go.Scatter(x=df1_2['Date'], y=stock2, mode='lines', name=st_2)
				trace3 = go.Scatter(x=df2_2['Date'], y=stock3, mode='lines', name=st_3)
				if month==1:
					month="January"
				if month==2:
					month="February"
				if month==3:
					month="March"
				if month==4:
					month="April"
				if month==5:
					month="May"
				if month==6:
					month="June"
				if month==7:
					month="July"
				if month==8:
					month="August"
				if month==9:
					month="September"
				if month==10:
					month="October"
				if month==11:
					month="November"
				if month==12:
					month="December"

				title=atype+" price analysis of "+month+" ( "+str(year)+" ) "+" with "+st_1+" , "+st_2+" and "+st_3
				layout = go.Layout(title=title,
					xaxis=dict(title='Date'),
					yaxis=dict(title=atype))
				fig = go.Figure([trace1, trace2, trace3], layout)
				fig.update_layout(
		            plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		            paper_bgcolor='rgba(8, 17, 8, 0.9)',
		            font=dict(color='#00d094'),
		        )
				graph=fig.to_html()
				return render(request,'compmonth_3.html',{'graph':graph})

	else:
		return render(request,'compmonth_3.html')

def comprange_3(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		atype=request.POST.get('atype')
		st_1=str(request.POST.get('stock1'))
		st_2=str(request.POST.get('stock2'))
		st_3=str(request.POST.get('stock3'))
		start1=request.POST.get('start')
		end1=request.POST.get('end')

		if atype=="Select the Price" or st_1=="Select the Stock One" or st_2=="Select the Stock Two" or st_3=="Select the Stock Three" or start1=="Select Start Year" or end1=="Select End Year":
			msg="Please select all the fields"
			return render(request,'comprange_3.html',{'msg':msg})
		else:
			start=int(start1)
			end=int(end1)
			if st_1=="RELIANCE":
				df = pd.read_csv('RELIANCE.csv',parse_dates=['Date'])

			elif st_1=="BAJFINANCE":
				df = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			elif st_1=="TATAMOTORS":
				df = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_1=="ITC":
				df = pd.read_csv('ITC.csv',parse_dates=['Date'])

			elif st_1=="TCS":
				df = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_1=="SUNPHARMA":
				df = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_1=="SBIN":
				df = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_1=="INFY":
				df = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_1=="ICICIBANK":
				df = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_1=="HDFCBANK":
				df = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			else:
				message="None is selected"


			if st_2=="ITC":
				df1 = pd.read_csv('ITC.csv',parse_dates=['Date'])
			elif st_2=="TCS":
				df1 = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_2=="TATAMOTORS":
				df1 = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_2=="SUNPHARMA":
				df1 = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_2=="SBIN":
				df1 = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_2=="INFY":
				df1 = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_2=="ICICIBANK":
				df1 = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_2=="HDFCBANK":
				df1 = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			elif st_2=="BAJFINANCE":
				df1 = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])

			else:
				message="None is selected"


			if st_3=="ITC":
				df2 = pd.read_csv('ITC.csv',parse_dates=['Date'])
			elif st_3=="TCS":
				df2 = pd.read_csv('TCS.csv',parse_dates=['Date'])

			elif st_3=="TATAMOTORS":
				df2 = pd.read_csv('TATAMOTORS.csv',parse_dates=['Date'])

			elif st_3=="SUNPHARMA":
				df2 = pd.read_csv('SUNPHARMA.csv',parse_dates=['Date'])

			elif st_3=="SBIN":
				df2 = pd.read_csv('SBIN.csv',parse_dates=['Date'])

			elif st_3=="INFY":
				df2 = pd.read_csv('INFY.csv',parse_dates=['Date'])

			elif st_3=="ICICIBANK":
				df2 = pd.read_csv('ICICIBANK.csv',parse_dates=['Date'])

			elif st_3=="HDFCBANK":
				df2 = pd.read_csv('HDFCBANK.csv',parse_dates=['Date'])

			elif st_3=="BAJFINANCE":
				df2 = pd.read_csv('BAJFINANCE.csv',parse_dates=['Date'])
			else:
				message="None is selected"


			df['Year']=df['Date'].dt.year
			df1['Year']=df1['Date'].dt.year
			df2['Year']=df2['Date'].dt.year
			
			df_st= df[(df['Year']>=start) & (df['Year']<=end)]
			df1_st1= df1[(df1['Year']>=start) & (df1['Year']<=end)]
			df2_st2= df2[(df2['Year']>=start) & (df2['Year']<=end)]
			if len(df_st)==0 or len(df1_st1)==0 or len(df2_st2)==0:
				error="YEAR MUST INCLUDE IN ALL THE STOCKS"
				return render(request,'comprange_3.html',{'error':error})
			else:
				stock1 = df_st[atype]
				stock2 = df1_st1[atype]
				stock3 = df2_st2[atype]
				trace1 = go.Scatter(x=df_st['Date'], y=stock1, mode='lines', name=st_1)
				trace2 = go.Scatter(x=df1_st1['Date'], y=stock2, mode='lines', name=st_2)
				trace3 = go.Scatter(x=df2_st2['Date'], y=stock3, mode='lines', name=st_3)

				title=atype+" price analysis from "+str(start)+" to "+str(end)+" with "+st_1+" , "+st_2+" and "+st_3
				layout = go.Layout(title=title,
					xaxis=dict(title='Date'),
				    yaxis=dict(title=atype))

				fig = go.Figure([trace1, trace2, trace3], layout)

				fig.update_layout(
		            plot_bgcolor='rgba(30, 30, 30, 0.5)',  # Plot area background color
		            paper_bgcolor='rgba(8, 17, 8, 0.9)',
		            font=dict(color='#00d094'),
		        )
				graph=fig.to_html()

				return render(request,'comprange_3.html',{'graph':graph})
	else:
		return render(request,'comprange_3.html')




def forgot(request):
	if request.method=='POST':
		email=request.POST.get('email')
		user=userregister.objects.filter(email=email)
		if(len(user)>0):
			password=user[0].password
			subject="Password"
			message="Welcome to cyber security...your password is "+password
			email_from=settings.EMAIL_HOST_USER
			recipient_list=[email,]
			send_mail(subject,message,email_from,recipient_list)
			rest="Your password sent to your respective email account....Please check"
			return render(request,'forgot.html',{'rest':rest})
		else:
			res="This email id is not registered"
			return render(request,'forgot.html',{'res':res})
	else:
		return render(request,'forgot.html')

def login(request):
	if request.method=="POST":
		email=request.POST.get('email')
		password=request.POST.get('password')
		x=userregister.objects.filter(email=email,password=password)
		k=len(x)
		if k>0:
			request.session['email']=email
			return redirect('/dashboard')
		else:
			return render(request,'login.html',{'ms':1})
	else:
		return render(request,'login.html')

def userprofile(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	user=userregister.objects.get(email=request.session['email'])
	return render(request,'userprofile.html',{'user':user})


def register(request):
	if request.method=="POST":
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		email=request.POST.get('email')
		password=request.POST.get('password')
		confirm_password=request.POST.get('confirm_password')
		if userregister.objects.filter(email=email).exists():
			return render(request,'register.html',{'ms':1})
		else:
			if password==confirm_password:
				otp_length = 6
				otp = ''.join(random.choices('0123456789', k=otp_length))
				subject="Verification"
				message="Welcome to Market Maven...your otp is "+otp
				email_from=settings.EMAIL_HOST_USER
				recipient_list=[email,]
				send_mail(subject,message,email_from,recipient_list)
				rest="OTP is sent to your respective email account....Please check"
				'''
				x=userregister()
				x.first_name=request.POST.get('first_name')
				x.last_name=request.POST.get('last_name')
				x.email=request.POST.get('email')
				x.password=request.POST.get('password')
				x.save()
				'''
				return render(request,'otp.html',{'otp':otp,'rest':rest,'first_name':first_name,'last_name':last_name,'email':email,'password':password})
			else:
				return render(request,'register.html',{'ms':3})
	else:
		return render(request,'register.html')		

def otp(request):
    if request.method == 'POST':
    	first_name=request.POST.get('first_name')
    	last_name=request.POST.get('last_name')
    	email=request.POST.get('email')
    	password=request.POST.get('password')
    	otp=request.POST.get('otp')
    	e_otp=request.POST.get('e_otp')
    	if otp==e_otp:
    		x=userregister()
    		x.first_name=request.POST.get('first_name')
    		x.last_name=request.POST.get('last_name')
    		x.email=request.POST.get('email')
    		x.password=request.POST.get('password')
    		x.save()
    		message="REGISTERED SUCCESSFULLY"
    		return render(request,'register.html',{'msg':2})
    	else:
    		message="VERIFICATION FAILED"
    		return render(request,'otp.html',{'msg':message})
    else:
    	return render(request,'otp.html')

        


"""
if request.method=="POST":
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		email=request.POST.get('email')
		password=request.POST.get('password')
		confirm_password=request.POST.get('confirm_password')
		if userregister.objects.filter(email=email).exists():
			return render(request,'register.html',{'ms':1})
		if password != confirm_password:
			return render(request,'register.html',{'ms':3})
		# Generate OTP
		user=User.objects.create_user(username=email,email=email)
		token=default_token_generator.make_token(user)
		uid=urlsafe_base64_encode(force_bytes(user.pk))
		subject='Verification OTP'
		message=f'Your OTP for email verification is: {token}'
		send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
		return render(request, 'otp.html', {'email': email})
	else:
		return render(request,'register.html')
"""

def base(request):
	return render(request,'base.html')

def index(request):
	res=latest_news.objects.all()
	review=myreview.objects.all()
	return render(request,'index.html',{'data':res,'review':review})

def allfaq(request):
	res=faq.objects.all()
	return render(request,'allfaq.html',{'data':res})

def alllatest_news(request):
	res=latest_news.objects.all()
	return render(request,'alllatest_news.html',{'data':res})

def newsdesc(request,id):
	res=latest_news.objects.get(id=id)
	return render(request,'newsdesc.html',{'i':res})

def allblogs(request):
	res=blogs.objects.all()
	return render(request,'allblogs.html',{'data':res})

def blogsdesc(request,id):
	res=blogs.objects.get(id=id)
	return render(request,'blogsdesc.html',{'i':res})

def alltutorials(request):
	res=tutorials.objects.all()
	return render(request,'alltutorials.html',{'data':res})

def allexperts(request):
	res=experts.objects.all()
	return render(request,'allexperts.html',{'data':res})

def expertsdesc(request,id):
	res=experts.objects.get(id=id)
	return render(request,'expertsdesc.html',{'i':res})

def review(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		x=myreview()
		x.title=request.POST.get('title')
		x.message=request.POST.get('message')
		x.save()
		msg="REVIEW ADDED SUCCESSFULLY"
		return render(request,'review.html',{'msg':msg})
	else:
		return render(request,'review.html')

def contact(request):
	if request.method=="POST":
	    x=contact_us() 
	    x.name=request.POST.get('name')
	    x.email=request.POST.get('email')
	    x.message=request.POST.get('message')
	    x.save()
	    return render(request,'contact.html',{'message':1})
	else:
		return render(request,'contact.html')

def sidebar(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	return render(request,'sidebar.html')

def changepass(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		o=request.POST.get('oldpass')
		n=request.POST.get('newpass')
		c=request.POST.get('confirmpass')
		if n==c:
			user=userregister.objects.get(email=request.session['email'])
			p=user.password
			if o==p:
				user.password=n
				user.save()
				msg1="PASSWORD SUCCESSFULLY CHANGED"
				return render(request,'changepass.html',{'msg1':msg1})
			else:
				msg="*INVALID OLD PASSWORD"
				return render(request,'changepass.html',{'msg':msg})
		else:
			msg="*NEW PASSWORD AND CONFIRM PASSWORD DOES NOT MATCH"
			return render(request,'changepass.html',{'msg':msg})
	else:
		return render(request,'changepass.html')
			
			

def help(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		x=helpsupport()
		x.title=request.POST.get('title')
		x.message=request.POST.get('message')
		x.save()
		msg="MESSAGE SUBMITTED SUCCESSFULLY"
		return render(request,'help.html',{'msg':msg})
	else:
		return render(request,'help.html')

def editprofile(request):
	if not request.session.has_key('email'):
	    return redirect('/login')   	
	user=userregister.objects.get(email=request.session['email'])
	if request.method=="POST":
		"""
		if request.method=="POST":
		print("yes")
		user.image=request.FILES['image']
		user.save()
		return render(request,'userprofile.html',{'user':user,'msg':'success'})
		"""
		user.first_name=request.POST.get('first_name')
		user.last_name=request.POST.get('last_name')
		user.birthday=request.POST.get('birthday')
		user.state=request.POST.get('state')
		user.country=request.POST.get('country')
		user.pincode=request.POST.get('pincode')
		user.contact=request.POST.get('contact')
		user.gender=request.POST.get('gender')
		user.age=request.POST.get('age')
		user.address=request.POST.get('address')
		user.gender=request.POST.get('gender')
		if 'image' in request.FILES:
			user.image=request.FILES['image']
    # Process image_file
		else:
			nothing="nothing"
		user.save()
		message="PROFILE EDITED SUCCESSFULLY"
		return render(request,'editprofile.html',{'message':message,'user':user})
	else:
		return render(request,'editprofile.html',{'user':user})

def logout(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	del request.session['email']
	return redirect('/login')

def about(request):
	return render(request,'about.html')



def newstock(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	else:
		return render(request,'newstock.html')


#40f8fa21da67431885edfaec3fa49ac4
#EZZ6G5T7V62SXRIX
"""
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=EZZ6G5T7V62SXRIX'
		r = requests.get(url)
		data = r.json()
		print(data)

"""