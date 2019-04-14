from django.http import HttpResponse

def Index(request):
    return HttpResponse("<h1>Привет! С Вами говорит Джанго-релизнутый</h1>")

def fun(request):
    return HttpResponse("<h1>Секретный раздел</h1>")

def extrafun(request):
    return HttpResponse("<h>Очень секретный раздел, который секретнее предыдущего.</h1>")
# Create your views here.
