from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from instructors.models import Instructor, Coursename, CourseApply
from django import forms
from django.contrib import messages


class Coefficient(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.value_int = None
        self.error_message = None
    
    def is_valid(self):
        if not self.value:
            self.error_message = "коэффициент не определен"
            return False

        try:
            self.value_int = int(self.value)
        except ValueError:
            self.error_message = "коэффициент не целое число"
            return False

        if self.name == 'a' and self.value_int == 0:
            self.error_message = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
            return False

        return True


def get_discr(a, b, c):
    d = b**2 - 4*a*c
    return d


def get_eq_root(a, b, d, order=1):
    if order == 1:
        x = (-b + d**(1/2.0)) / 2*a
    else:
        x = (-b - d**(1/2.0)) / 2*a
    return x


class QuadraticForm(forms.Form):
    a = forms.CharField(max_length=10)
    b = forms.CharField(max_length=10)
    c = forms.CharField(max_length=10)


def quadratic_results(request):
    form = QuadraticForm()
    context = {'error': False}
    context['form'] = form
    for name_value in ['a', 'b', 'c']:
        coefficient = Coefficient(name_value, request.GET.get(name_value, ''))
        if coefficient.is_valid():
            context[name_value] = coefficient.value_int
        else:
            context['error'] = True
            context[name_value + '_error'] = coefficient.error_message
            context[name_value] = coefficient.value
    if not context['error']:
        a = context['a']
        b = context['b']
        c = context['c']
        d = get_discr(a, b, c)
        if d < 0:
            result_message = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        elif d == 0:
            x = get_eq_root(a, b, d)
            result_message = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}".format(x)
        else:
            x1 = get_eq_root(a, b, d)
            x2 = get_eq_root(a, b, d, order=2)
            result_message = "Квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}".format(x1, x2)

        context.update({'d': d, 'result_message': result_message})
    return render(request, 'python.html', context)



# Create your views here.

def hello(request):
    all_courses = Coursename.objects.all()
    context = {'var1': 'Hello world!'}
    context['var2'] = {'some_str': 'Hello python!'}
    instructors = Instructor.objects.all()
    context['all_instructors'] = instructors
    context['var3'] = ['a', 'b', 'c']
    context['courses'] = all_courses

    return render(request, 'index.html', context)

def instructors_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructors.html', {'instructors_list': instructors})

def http(request):
    response = render(request, 'http.html')
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


class CourseApplyForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(label='Mail', required=False)  # (required=False)
    package = forms.ChoiceField(choices=(
        ('standart', 'Standart'), ('gold', 'Gold'), ('vip', 'Vip')),
        widget=forms.RadioSelect)
    news_subscribe = forms.BooleanField(required=False, help_text='help text')
    # (required=None)


class ModelCourseApplyForm(forms.ModelForm):
    class Meta:
        model = CourseApply
        exclude = ['date_apply', 'is_active', 'comment']
        widgets = {'package': forms.RadioSelect}
        labels = {'email': 'Mail'}


def course_apply(request):
    # model_form = ModelCourseApplyForm(initial={'package': 'gold', 'news_subscribe': True})
    if request.method == 'POST':
        # form = CourseApplyForm(request.POST)
        form = ModelCourseApplyForm(request.POST)
        if form.is_valid():
            
            instance = form.save()

            '''
            data = form.cleaned_data
            course_apply = CourseApply()
            course_apply.name = data['name']
            course_apply.email = data['email']
            course_apply.package = data['package']
            course_apply.news_subscribe = data['news_subscribe']
            course_apply.save()
            '''

            messages.success(request, 'Saved!')

            # print(request.POST)
            # print(form.cleaned_data)
            # print('Do logic')
            return redirect('/apply/')
    else:
        # form = CourseApplyForm(initial={'package': 'gold', 'news_subscribe': True})
        form = ModelCourseApplyForm(initial={'package': 'gold', 'news_subscribe': True})
    return render(request, 'apply.html', {'form': form}) # {'model_form': model_form}


def courseapply_edit(request, pk):
    courseapply = CourseApply.objects.get(id=pk)
    if request.method == 'POST':
        form = ModelCourseApplyForm(request.POST, instance=courseapply)
        if form.is_valid():
            courseapply = form.save()
            messages.success(request, 'Saved!')
            return redirect('/apply/')
    else:
        form = ModelCourseApplyForm(instance=courseapply)
    return render(request, 'courseapply_edit.html', {'form': form})


def courseapply_delete(request, pk):
    courseapply = CourseApply.objects.get(id=pk)
    if request.method == 'POST':
        courseapply.delete()
        messages.success(request, 'Deleted!')
        return redirect('/apply/')
    return render(request, 'courseapply_delete.html', {'courseapply': courseapply})
