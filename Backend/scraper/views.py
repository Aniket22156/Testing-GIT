from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

def scrape(request):
    if request.method == 'POST':
        url = request.POST['url']

        # Send a request to the website to grab the HTML content
        response = requests.get(url)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the metadata using BeautifulSoup methods
        title = (soup.find("meta", attrs={"name": "description"}).get('content'))

        context = {
            'title': title,
        }

        return render(request, 'scraper/index.html', context)

    return render(request, 'scraper/index.html')