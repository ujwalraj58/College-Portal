from django.shortcuts import render, redirect
from portal.models import Notice
from .models import Student


def login_view(request):

    if request.method == 'POST':

        roll_no = request.POST['roll_no']
        password = request.POST['password']

        try:

            student = Student.objects.get(
                roll_no=roll_no,
                password=password
            )

            request.session['student_id'] = student.id

            return redirect('dashboard')

        except Student.DoesNotExist:

            return render(
                request,
                'login.html',
                {
                    'error':
                    'Invalid Roll Number or Password'
                }
            )

    return render(request, 'login.html')

def dashboard(request):

    student_id = request.session.get(
        'student_id'
    )

    if not student_id:

        return redirect('login')

    student = Student.objects.get(
        id=student_id
    )

    notices = Notice.objects.order_by(
        '-date_posted'
    )[:3]

    return render(
        request,
        'dashboard.html',
        {
            'student': student,
            'notices': notices
        }
    )

def logout_view(request):

    request.session.flush()

    return redirect('login')