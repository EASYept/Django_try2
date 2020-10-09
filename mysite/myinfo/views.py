from django.shortcuts import render


def main_screen(request):
    return render(request, 'myinfo/base.html')  # this is basicly 'myinfo/templates/myinfo/base.html'


def about_me(request):
    return render(request, 'myinfo/about_me.html')


def my_jobs(request):
    return render(request, 'myinfo/my_jobs.html')


def my_contacts(request):
    return render(request, 'myinfo/contacts.html')
