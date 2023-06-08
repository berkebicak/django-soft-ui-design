import config
import requests

from .forms import GeneralForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):

    # Page from the theme
    return render(request, 'pages/index.html')


@ login_required(login_url='login')
def summarize(request):
    form = GeneralForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        text = form.cleaned_data.get('text')
        try:
            response = requests.post("http://127.0.0.1:51000/summarize",
                                     json={"text": text, "token": config.TOKEN},
                                     headers={"Authorization": f"Bearer {config.TOKEN}"})
            response.raise_for_status()
            context["predict"] = response.json()
        except (requests.exceptions.RequestException, KeyError):
            context["error"] = "Unable to summarize text. Please try again later."
    return render(request, 'summarize.html', context)


@ login_required(login_url='login')
def stemmer(request):
    form = GeneralForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        text = form.cleaned_data.get('text')
        try:
            response = requests.post("http://127.0.0.1:51000/stemmer",
                                     json={"text": text, "token": config.TOKEN},
                                     headers={"Authorization": f"Bearer {config.TOKEN}"})
            response.raise_for_status()
            context["predict"] = response.json()
        except (requests.exceptions.RequestException, KeyError):
            context["error"] = "Unable to stemming text. Please try again later."
    return render(request, 'stemmer.html', context)


@ login_required(login_url='login')
def lemmatizer(request):
    form = GeneralForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        text = form.cleaned_data.get('text')
        try:
            response = requests.post("http://127.0.0.1:51000/lemmatizer",
                                     json={"text": text, "token": config.TOKEN},
                                     headers={"Authorization": f"Bearer {config.TOKEN}"})
            response.raise_for_status()
            context["predict"] = response.json()
        except (requests.exceptions.RequestException, KeyError):
            context["error"] = "Unable to lemmatizing text. Please try again later."
    return render(request, 'lemmatizer.html', context)


@ login_required(login_url='login')
def stopwordremove(request):
    form = GeneralForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        text = form.cleaned_data.get('text')
        try:
            response = requests.post("http://127.0.0.1:51000/stopword",
                                     json={"text": text, "token": config.TOKEN},
                                     headers={"Authorization": f"Bearer {config.TOKEN}"})
            response.raise_for_status()
            context["predict"] = response.json()
            context["res"] = text
        except (requests.exceptions.RequestException, KeyError):
            context["error"] = "Unable to stop-word text. Please try again later."
    return render(request, 'stopwordremove.html', context)
