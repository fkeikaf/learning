from django.shortcuts import render

# Create your views here.
def home(request): 
    # content = {
    #     'message': 'Hello world'
    # }
    # return render(request, 'index.html', content)
    return render(request, 'index.html')

def product(request): 
    return render(request, 'product/index.html')