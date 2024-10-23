from django.http import HttpResponse
from django.shortcuts import render
from .models import Features
def index(request):
    feature1 = Features()
    feature1.id=0
    feature1.name='Fast'
    feature1.details='our service is Blazingly Fast!'

    feature2 = Features()
    feature2.id=1
    feature2.name='Reliable'
    feature2.details='You can rely on our service!'

    feature3 = Features()
    feature3.id=2
    feature3.name='Eficient'
    feature3.details='Our services are very Efficient!'
    
    feature4 = Features()
    feature4.id=3
    feature4.name='Affordable'
    feature4.details='our service are Price Friendly!'

    FeaturesList=[feature1,feature2,feature3,feature4]


    return render(request, 'index.html', {'FeaturesList': FeaturesList})
def polls(request):
    return HttpResponse("Welcome to the Polls page! Everything you will appear here!")
def download(request):
    return HttpResponse("Welcome to Download Page.\n \t Your Download will begin Shortly!")
def counter(request):
    text= request.GET['text']
    amount_of_words=len(text.split())
    return render (request, 'counter.html', {'amount':amount_of_words})

