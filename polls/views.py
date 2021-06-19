from django.http import HttpResponse
# Create your views here.
def index(request): #the function I'll map to the '' url
    return HttpResponse("Hello, world. You're at the polls index.")

def secretPage(request):
    return HttpResponse("<i>hohoho looks like we have ourselves a HACKERMAN over here!</i>")

