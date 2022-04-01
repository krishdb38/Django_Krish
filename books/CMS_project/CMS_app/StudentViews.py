from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
import datetime

from .models import CustomUser, Staffs, Course, Subjects, Students, Attendance, AttendanceReport, LeaveReportStudent
from .models import FeedbackStudent, StudentResult


def student_home(request):
    student_obj = Student.objects.get(admin = request.user.id) # id 
    total_attendance = Attendance.objects.filter(student_id = student_obj)
    attendance_present = Attendance.objects.filter(student_id = student_obj, status = True).count()
    attendance_absent = Attendance.objects.filter(student_id = student_obj, status = False).count()
    course_obj = Course.objects.get(id = student_obj.course_id.id)
    total_subjects = Subjects.objects.filter(course_id= course_obj).count()
    
    subject_name = []
    data_present = []
    data_absent = []
    subject_data = Subjects.objects.filter(course_id = course_obj).count()
    
    for subject in subject_data:
        attendance = Attendance.objects.filter(subject_id = subject.id)
        attendance_present_count = AttendanceReport.objects.filter(attendance_id__in = attendance,
                                                                   status=True, 
                                                                   student_id = student_obj.id.count())
        attendance_absent_count = AttendanceReport.objects.filter(attendance_id__in = attendance, 
                                                                  status = False, 
                                                                  student_id = student_obj.id).count()
        subject_name.append(subject.subject_name)
        data_present.append(attendance_present_count)
        data_absent.append(attendance_absent_count)
        
        context = {
            "total_attendance": total_attendance,
            'attendance_present': attendance_present, 
            'attendance_absent':attendance_absent_count,
            "total_subjects" : total_subjects, 
            'subject_name': subject_name, 
            'data_present':data_present, 
            'data_absent':data_absent
        }
        return render(request,'student_tamplate/student_home_template.html')
        
    

def student_view_attendance(request):
    ## Getting Logged in Student Data
    student = Student.objects.get(admin=request.user.id)
    
    # Getting Course Enrolled of LoggedIn Studennts
    course = student.course_id
    
    # Getting the Subjects of Course Enrolled
    subjects = Subjects.objects.filter(course_id = course)
    context = {
        'subjects': subjects,
    }
    return render(request,'student_template/student_view_attendance.html', context)


def student_view_attendance_post(request):
    if request.method != "POST":
        messages.error(request, 'Invalid Method')
        return redirect('student_view_attendance')
    else:
        # getting all the input data from form
        subject_id = request.POST.get('subject')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        ## parsing the dae in to Python object
        start_date_parse = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        print('Student views student view attendance post line 77 ', start_date_parse)
        end_date_parse = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        
        ## Getting all the Subject 
        subject_obj = Subjects.objects.get(id=subject_id)
        
        # Getting logged in user data
        user_obj = CustomUser.objects.get(id=request.user.id)
        
        # getting all the subject data based on selected subject
        subject_obj = Subjects.objects.get(id = subject_id)
        
        # getting Logged In User Data
        user_obj = CustomUser.objects.get(id=request.user.id)
        
        # Getting student Data Based on Logged in Data
        stud_obj = Students.objects.get(admin=user_obj)
        
        ## Now Accessing Attendance Data based on the Range of Date
        attendance = Attendance.objects.filter(attendance_date__range = (start_date_parse,end_date_parse), subject_id=subject_obj)
        
        ## Getting attendance Report based on the attendance
        # details obtained above
        attendance_reports = AttendanceReport.objects.filter(attendance_id__in = attendance, student_id = stud_obj)
        
        context = {
            'subject_obj': subject_obj,
            'attendance_reports': attendance_reports
        }
        return render(request, 'student_template/student_attendance_data.html', context)
    
def student_apply_leave(request):
    student_obj = Students.objects.get(admin=request.user.id)
    leave_data = LeaveReportStudent.objects.filter(student_id = student_obj)
    
    context = {
        "leave_data":leave_data
    }
    return render(request,'student_template/student_apply_leave.html', context)
    
    
def student_feedback_save(request):
    if request.method != 'POST':
        messages.error(request,"Invalid method")
        return redirect('student_feedback')
    else:
        feedback = request.POST.get('feedback_message')
        student_obj = Students.objects.get(admin=request.user.id)
        
        try:
            add_feedback = FeedbackStudent(student_id = student_obj,
                                           feedback=feedback,
                                           feedback_reply = '')
            add_feedback.save()
            messages.success(request, "Feed back sent")
            
        except :
            messages.error(request,"Failed to Send feedback")
            return redirect("student_feedback")
        
def student_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    student = Students.objects.get(admin=user)
    
    context = {
        'user' : user,
        'student':student
    }
    return render(request, 'stuent_template/student_profile.html', context)

def student_profile_update(request):
    if request.method != 'POST':
        messages.error(request,"Invalid method")
        return redirect('student_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        address = request.POST.get('address')
        
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            
            if password != None and password != '':
                customuser.set_password(password)
            customuser.save()
            messages.success(request,"Profile Updated successfully")
        except :
            messages.error(request,"Failed to update profile")
            return redirect('student_profile')
        
def student_view_result(request):
    student = Students.objects.get(admin=request.user.id)
    student_result = StudentResult.objects.filter(student_id = student.id)
    context = {
        'student_result' : student_result
    }
    return render(request, 'student_template/student_view_result.html', context)
