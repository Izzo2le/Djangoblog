from blog import views

def hello_blog(request):
    return HttpResponse("Hello, Blog!")
