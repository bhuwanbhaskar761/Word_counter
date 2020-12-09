from django.shortcuts import render,redirect
from bs4 import BeautifulSoup
from urllib.request import urlopen
from .models import *
from django.contrib import messages
import pandas as pd
import nltk
from collections import Counter
from nltk import word_tokenize
from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))


def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if not word in stop_words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

    return counts


def frequency(request):
    urlget=""
    if request.method == "POST":
        u = request.POST['url']
        try:
            urlget = WebUrl.objects.get(url1__icontains=u)
        except:
            pass
        if urlget:
            messages.success(request,'Data fetched from Database')
            return redirect('result',urlget.id)
        else:
            url = u
            page = urlopen(url)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            li = soup.get_text()
            web1 = WebUrl.objects.create(url1=u)
            result = word_count(li.lower())
            result = sorted(result.items(), key=lambda x: x[1], reverse=True)
            count = 1
            for i, j in result:
                try:
                    i = int(i)
                except:
                    pass
                if type(i) != int and not len(i) <= 2 and count < 11:
                    count += 1
                    Scrapped.objects.create(weburl=web1,word=i,frequency=j)
                    if count == 11:
                        break
            messages.success(request,'Data fetched from Unique Url')
            return redirect('result',web1.id)
    return render(request,'frequency.html')

def result(request,pid):
    data = WebUrl.objects.get(id=pid)
    word = Scrapped.objects.filter(weburl=data)
    d = {'word':word}
    return render(request,'result.html',d)

