import json
from datetime import time

#import pygal as pygal
#from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
#from django.http import HttpResponseRedirect, HttpResponse

#from helpdesk import task
from .models import Topic
from .models import Tikets
from helpdesk import task



# Create your views here.from pygal.style import Style


def main(request):
    #return HttpResponseRedirect("/")
    return render(request, "tikets/main.html")

#@login_required(login_url='/accounts/login/')
def index(request):
    topic = Topic.objects.all()
    #task.bot_run('')

    return render(request, "tikets/index.html", {"topic_list":topic})

#@login_required(login_url='/accounts/login/')
def create(request):
    print("ddddddd")
    if request.method == "POST":
        tiket = Tikets()
        tiket.tikets_PIP = request.POST.get("tikets_PIP")
        print()
        print("qqqqqqqq",tiket.tikets_PIP)
        tiket.tikets_email = request.POST.get("tikets_email")
        tiket.tikets_Phone = request.POST.get("tikets_Phone")
        tiket.tikets_Location = request.POST.get("tikets_Location")
        tiket.tikets_text = request.POST.get("tikets_text")
        tikets_id = request.POST.get("tikets_Topic")
        tik = Topic.objects.get(id=tikets_id)
        tiket.tikets_Topic = tik
        #tiket.tikets_Topic = tikets_id
        print(tik)
        print(tikets_id)
        tiket.save()
    #return HttpResponseRedirect("/")
    return render(request, "tikets/index.html")


#@login_required(login_url='/accounts/login/')
def tiketsList(request):
    return render(request, "tikets/tiketsList.html")

def start_bot(request):
    #task.bot_run.delay("Start bot")
    task.tel_bot_start.delay('tel_bot start')
    return render(request, "tikets/index.html")

def stop_bot(request):
    task.bot_stop.delay()
    task.tel_bot_stop.delay()
    return render(request, "tikets/index.html")




