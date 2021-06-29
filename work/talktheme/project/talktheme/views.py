from django.shortcuts import render

# Create your views here.
def main(request): 
    # content = {
    #     'message': 'Hello world'
    # }
    # return render(request, 'index.html', content)
    return render(request, 'index.html')