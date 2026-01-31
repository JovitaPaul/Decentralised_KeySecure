from django.shortcuts import render


def upload_key(request):
    return render(request, 'uploadkey.html')
