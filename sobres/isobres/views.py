from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homepage(request):
    page = """
    <html>
    <body>
    Bribes management application
    (c) Luis Barcenas, 2017
    </body>
    </html>
    """
    return HttpResponse(page)
