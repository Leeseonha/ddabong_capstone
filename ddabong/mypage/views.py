from django.shortcuts import render, get_object_or_404
# Create your views here.
def mypage(request):
    return render(request, 'mypage.html')

def speakers(request):
    return render(request, 'speakers.html')

def faq(request):
    return render(request, 'faq.html')

def supporters(request):
    return render(request, 'supporters.html')