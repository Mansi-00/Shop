from django.shortcuts import render

# Create your views here.


def Demo(request):
    return render(request, 'index.html')


def Demo2(request):
    return render(request, 'common.html')



