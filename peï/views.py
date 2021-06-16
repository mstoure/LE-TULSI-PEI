from django.shortcuts import render

# Create your views here.

def onepage(request):
    return render(request, 'peï/onepage.html', {})