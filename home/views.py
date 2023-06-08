import config
import requests

from .models import TextAnalysisResult

from .forms import GeneralForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user


# Create your views here.


def index(request):

    # Page from the theme
    return render(request, 'pages/index.html')


def tools(request):

    # Page from the theme
    return render(request, 'pages/tools.html')


@ login_required(login_url='login')
def dashboard(request):
    user = get_user(request)
    analysis_results = TextAnalysisResult.objects.filter(
        user=user).order_by('-created_at')

    context = {'analysis_results': analysis_results}
    return render(request, 'pages/dashboard.html', context)


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
            response.raise_for_status()  # Raise an exception for non-successful responses
            analysis_result = response.json()
            context["predict"] = analysis_result

            # Save the analysis result to the database
            TextAnalysisResult.objects.create(
                user=request.user,
                text=text,
                analysis_type='Özet',
                result=analysis_result
            )
        except (requests.RequestException, KeyError):
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
            analysis_result = response.json()
            context["predict"] = analysis_result

            # Save the analysis result to the database
            TextAnalysisResult.objects.create(
                user=request.user,
                text=text,
                analysis_type='Kelime Normalleştirme',
                result=analysis_result
            )
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
            analysis_result = response.json()
            context["predict"] = analysis_result

            text = text.split("\n")
            joined_text = ", ".join(text)
            # Save the analysis result to the database
            TextAnalysisResult.objects.create(
                user=request.user,
                text=joined_text,
                analysis_type='Kök Bulma',
                result=analysis_result
            )

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
            analysis_result = response.json()
            context["predict"] = analysis_result

            # Save the analysis result to the database
            TextAnalysisResult.objects.create(
                user=request.user,
                text=text,
                analysis_type='Stop-Word',
                result=analysis_result
            )

        except (requests.exceptions.RequestException, KeyError):
            context["error"] = "Unable to stop-word text. Please try again later."
    return render(request, 'stopwordremove.html', context)
