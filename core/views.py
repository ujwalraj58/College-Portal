from django.shortcuts import render
from portal.models import Department, Faculty, Notice, Gallery

def index(request):

    departments = Department.objects.all()
    faculty = Faculty.objects.all()
    notices = Notice.objects.all()
    gallery = Gallery.objects.all()

    context = {
        'departments': departments,
        'faculty': faculty,
        'notices': notices,
        'gallery': gallery,
    }

    return render(request, 'index.html', context)