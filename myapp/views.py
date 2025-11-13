from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Hello Django! My project is working!")