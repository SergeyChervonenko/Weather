from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>"Hello world</h1>')


def test(request):
    return HttpResponse('<h1>"Test Page</h1>')


