from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
from .models import Tweet


def home_view(request,*args,**kwargs):
   
    return render(request,'pages/home.html')

def tweet_list_view(request,*arge,**kwargs):
    """
    consume all tweets list 
    """
    data = {

    }
    status = 200 
    try:
        obj = Tweet.objects.all()
        tweets_list = [{"id":x.id,"content":x.content } for x in obj]
        
        data['response']= tweets_list
    except:
        data['message'] = "No Tweets found "
        status = 404 
    return JsonResponse(data,status=status)


def tweet_detail_view(request,tweet_id,*args,**kwargs):
    data = {
        "id" : tweet_id ,
        # "image" : obj.image.url        
    }
    status = 200 
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message']= " Tweet Does Not exists"
        status = 404 
   
    return JsonResponse(data,status=status)
