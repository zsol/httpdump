from django import http
import debug_toolbar.models

def home(request):
    return http.HttpResponse('<html><body>Hello World from django !</body></html>')
