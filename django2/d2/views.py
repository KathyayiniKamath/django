from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
def d2(request):

    time=datetime.now()
    newtime=timedelta(hours=+4)
    html='<html><body><b>Current date and time value is:</b>%s</body></html>' %newtime
    return  HttpResponse(html)
    
# Create your views here.
