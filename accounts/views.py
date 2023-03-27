from django.http import HttpResponseGone

# Create your views here.

def index(request):
    return HttpResponseGone("Accounts site")