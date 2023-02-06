from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def code(request):
    #return HttpResponse("Hello, world. You're at the scyffyy index.")
    #return render(request, "Hello.html")
    #return HttpResponse(code2())

    response = urllib.request.urlopen('https://www.gandhinagaruni.ac.in')
    soup = BeautifulSoup(response, 'html.parser', from_encoding=response.info().get_param('charset'))
    #return HttpResponse(soup)

    if soup.findAll("meta", {"name":"description"}):
        output = (soup.find("meta", attrs={"name":"description"}).get('content'))
        return render(request, "Hello.html", {"output": output})
    else:
        print("Error")

    # if soup.findAll("title"):
    #     return HttpResponse(soup.find("title").string)
    # else:
    #     print("Error")

    