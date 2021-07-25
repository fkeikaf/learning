from django.shortcuts import render

# Create your views here.
def showPages(request): 
    path = request.path[1:] + 'index.html'
    return render(request, path)
