from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    url=requests.get("https://inshortsapi.vercel.app/news?category=all")
    all_data=url.json()
    context={
        'data':all_data['data']
    }
    return render(request,'index.html',context)

def politics(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=politics")
    politics_data = url.json()
    context = {
        'data': politics_data['data']
    }
    return render(request,'politics.html',context)

def sports(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=sports")
    sports_data = url.json()
    context = {
        'data': sports_data['data']
    }
    return render(request,'sports.html',context)

def tech(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=technology")
    tech_data = url.json()
    context = {
        'data': tech_data['data']
    }
    return render(request,'technology.html',context)

def world(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=world")
    world_data = url.json()
    context = {
        'data': world_data['data']
    }
    return render(request,'world.html',context)

def local(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=hatke")
    local_data = url.json()
    context = {
        'data': local_data['data']
    }
    return render(request,'local.html',context)

def search(request):
    query=request.POST.get('query')
    header=request.POST.get('query')
    url = requests.get("https://inshortsapi.vercel.app/news?category="+query)
    data = url.json()
    context = {
        'data': data['data'],
        'header':header
    }
    return render(request,'search.html',context)