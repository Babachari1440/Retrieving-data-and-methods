from django.shortcuts import render



from app.models import *

# Create your views here

def display_topic(request):
    #topics=Topic.objects.all()

    #above query will give all data from table


    topics=Topic.objects.filter(topic_name='Dance')
    return render(request,'display_topic.html',context={'topics':topics})


#above query will give particular data from table in django's filter method


    #topics=Topic.objects.get(topic_name='Dance')
    #return render(request,'display_topic.html',context={'topics':topics})

 #above query will give particular data from table in django's get method



def display_webpage(request):
    webpages=Webpage.objects.all()
    return render(request,'display_webpage.html',context={'webpages':webpages})

def display_access_records(request):
    access_records=Access_Records.objects.all()
    return render(request,'display_access_records.html',context={'access_records':access_records})
