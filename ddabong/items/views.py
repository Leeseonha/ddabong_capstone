from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
# Create your views here.
def items(request):
    return render(request, 'items.html')

def keyboard(request):
    return JsonResponse(
        {
            'type':'buttons',
            'buttons':['내주변헌혈','공여자정보요청','수혜자정보요청']
        }
    )