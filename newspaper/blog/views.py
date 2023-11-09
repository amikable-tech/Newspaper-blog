from django.shortcuts import render
import requests

# Create your views here
from django.shortcuts import render
import requests

def fetch_cricket_news():
    url = "https://newsapi.org/v2/everything?q=Cricket&from=2023-11-08&sortBy=popularity&apiKey=fc1c771ba04d417a9b1d6258d19d3e30"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)
        return response.json().get('articles', [])
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return []

def index(request):
    cricket_news = fetch_cricket_news()

    title = [article.get('title', '') for article in cricket_news]
    desc = [article.get('description', '') for article in cricket_news]
    img = [article.get('urlToImage', '') for article in cricket_news]

    mylist = zip(title, desc, img)
    context = {'mylist': mylist}

    return render(request, 'index.html', context)
