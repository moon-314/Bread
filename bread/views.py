from django.shortcuts import render
# Create your views here.

# html 경로 지정
def home(request):
    return render(request, 'bread/home.html')

def info(request):
    return render(request, 'bread/info.html')

def gallery(request):
    return render(request, 'bread/gallery.html')
    
