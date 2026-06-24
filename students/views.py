from django.shortcuts import render

def home(request):
    return render(request, "home.html",{
         "name": "Muhammad Mansoor",
        "course": "Django"
    })

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")