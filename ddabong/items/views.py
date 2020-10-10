from django.shortcuts import render, get_object_or_404

# Create your views here.
def items(request):
    return render(request, 'items.html')