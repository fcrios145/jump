from django.shortcuts import render_to_response

# Create your views here.

def index(request):
    data = {'data'}
    return render_to_response('noticias/home.html', {'data': data})
