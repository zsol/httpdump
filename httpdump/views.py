from django import http

def home(request):
    return http.HttpResponse('<html><body>Hello World from django !</body></html>')
