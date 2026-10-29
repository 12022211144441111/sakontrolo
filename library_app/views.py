from django.shortcuts import render

def base(request):
    return render(request, "base.html")

def home(request):
    return render(request, "home.html")

def books(request):
    books = {"HarryPotter": 350,
               "The Hobbit": 280,
               "Atomic Habits": 320,
               "1984" : 250}
    
    return render(request, "books.html", {"books": books})