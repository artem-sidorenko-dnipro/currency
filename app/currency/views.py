from django.http import HttpResponse
from currency.utils import generate_password as gp


def hello_world(request):
    return HttpResponse('Hello World')


def gen_password(request):
    password = gp()
    return HttpResponse(password)

def foo():
    pass