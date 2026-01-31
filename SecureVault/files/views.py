from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def upload_file(request):
    return render(request, 'uploadfile.html')


def get_file(request):
    return render(request, 'getfile.html')
