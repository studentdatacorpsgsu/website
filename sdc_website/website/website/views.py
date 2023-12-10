from django.http import render,HttpResponse



def hometest(request):
    return HttpResponse("Sup brah")