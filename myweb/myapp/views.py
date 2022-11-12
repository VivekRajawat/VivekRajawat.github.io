from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'myapp/homepage.html')

def signin(request):
    if request.method == 'POST':
        return render(request,'myapp/contact.html')
    return render(request,'myapp/signin.html')

def signup(request):
    if request.method == 'POST':
        return render(request,'myapp/contact.html')
    return render(request,'myapp/signup.html')

def contact(request):
    if request.method == 'POST':
        return render(request,'myapp/contact.html')
    return render(request,'myapp/contact.html')