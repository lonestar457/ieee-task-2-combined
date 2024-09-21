from django.shortcuts import render
from django.http import HttpResponse

movies=[
    {
        'name':'ironman1',
    "story":" awesome",
    "date":"oct 30"
    },
    {
        'name' : 'cap the first',
    "story" : "history",
    "date" : "oct 31"
    }
]

def home (request):
    context={'movies': movies}
    return render(request,'myshk/home.html', context)
def about (request):
    return render(request,'myshk/about.html',{"title":"about"})