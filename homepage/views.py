from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    # return HttpResponse("Hello World!")
    name = "Gang Hun Jeong"
    return render(request, 'index.html' , {"my_name": name})