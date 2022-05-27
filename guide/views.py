from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'Home.html')

def careers(request):
    return render(request, 'careers.html')


def career(request, pk):
    return render(request, 'career.html')

def about(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'Contact.html')        