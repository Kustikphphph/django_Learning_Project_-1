from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import *
# Create your views here.

def index(request):
    return HttpResponse("Index")
def about(request):
    return HttpResponse("About")
def contact(request):
    return HttpResponseRedirect("/about")
def details(request):
    return HttpResponsePermanentRedirect("/")
def m304(request):
    return HttpResponseNotModified()
def m400(request):
    return HttpResponseBadRequest("<h2>Bad Request</h2>")
def m403(request):
    return HttpResponseForbidden ( "<h2>ForЬidden</h2>")
def m404(request):
    return HttpResponseNotFound("<h2>Not Found</h2>")
def m405(request):
    return HttpResponseNotAllowed("<h2>Method is not allowed</h2>")
def m410(request):
    return HttpResponseGone("<h2>Content is no longer here</h2>")
def m500(request):
    return HttpResponseServerError("<h2>Something is wrong</h2>")