"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from django.http import HttpResponse, HttpResponseNotFound
# from django.shortcuts import render
from instructors.views import hello, hello_python, http, sum_two, instructors_list, quadratic_results, course_apply, courseapply_edit, courseapply_delete

"""
def hello(request):
    print(dir(request))
    print(request.path)
    print(request.method)
    print(request.GET)
    print(request.POST)
    # print(request.META)
    return render(request, 'index.html')

def http(request):
    # print(dir(request))
    print(request.path)
    print(request.method)
    print(request.GET)
    print(request.POST)
    # print(request.POST['some'])
    response = render(request, 'http.html')
    print(response)
    print(dir(response))
    print(response['Content-Type'])
    response['Age'] = 2000
    response.status_code = 404
    # return response
    return HttpResponseNotFound('404')


def hello_python(request):
    return render(request, 'python.html')

def sum_two(request, a, b):
    s = int(a) + int(b)
    # print('Hello!')
    # print(a, b)
    return HttpResponse(s)
"""

urlpatterns = [
    url(r'^$', hello),
    # url(r'^python/$', hello_python),
    # url(r'^python/$', include('hello.urls', namespace='quadratic')),
    url(r'^python/$', quadratic_results),
    url(r'^apply/$', course_apply),
    url(r'^courseapply/(?P<pk>\d+)/edit/$', courseapply_edit),
    url(r'^courseapply/(?P<pk>\d+)/delete/$', courseapply_delete),
    url(r'^instructors/$', instructors_list),
    url(r'^http/$', http),
    # url(r'^python/(?P<some>\w+)/$', hello_python),
    url(r'^sum/(?P<a>\d+)/(?P<b>\d+)/$', sum_two),
    url(r'^admin/', admin.site.urls),
]

# \d - любое число
# \d+ - любой паттерн, набор чисел
# [12]+ - любой набор чисел с 1 или 2
# (\d+) - позиционная переменная, нужен будет второй аргумент у функции
# \w+ - не только числа, но и буквы