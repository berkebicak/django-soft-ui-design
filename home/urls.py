from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tools/', views.tools, name='tools'),
    path('summarize/', views.summarize, name='summarize'),
    path('stemmer/', views.stemmer, name='stemmer'),
    path('lemmatizer/', views.lemmatizer, name='lemmatizer'),
    path('stopwordremove/', views.stopwordremove, name='stopwordremove'),
]
