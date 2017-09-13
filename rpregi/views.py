from django.shortcuts import render
from django.utils import timezone
from .models import Rplist

def homeview(request):
    rpqueryset = Rplist.objects.all().order_by('published_date')
    return render(request, 'rpregi/mainpage.html', {'alllist':rpqueryset})
