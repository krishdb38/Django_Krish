from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse 
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json


from .models import CustomUser, Staffs, Courses, Subjects, Students, SessionYearModel
from .models import Attendance, AttendanceReport, LeaveReportStaff , FeedBackStaffs, StudentResult

def staff_home(request):
    ## Fetching all students under staff
    print(request.user.id)
    subjects = Subjects.objects.filter(staff_id=request.user.staff)
    print(subjects)
    course_id_list = []
    for subject in subjects:
        course = Courses.objects.get(id=subject.course_id.id)
        course_id_list.append(course.id)
        
    final_course = []
    # Removing Duplicate Course ID
    for course_id in course_id_list:
        if course_id not in final_course:
            final_course.append(course_id)
            
    print(final_course)
    students_count = Students.objects.filter(course_id__in = final_course).count()
    subject_count = subjects.count()
    print(subject_count)
    print(students_count)
    
    # Fetch All Attendance Count
    attendance_count = Attendance.objects.filter(subject_id__in = subjects).count()
    
    # Fetch All Approve Leave
    print(request.user.user_type)
    staff = Staffs.objects.get(admin=request.user.id)
    leave_count = LeaveReportStaff.objects.filter(staff_id=staff.id,leave_status=1) # leave = True
    
    ## Fetch Attendance Data By Subjects
    subject_list = []
    attendance_list = []
    for subject in subjects:
        attendance_count1 = Attendance.objects.filter(subject_id = subject.id).count()
        subject_list.append(subject.subject_name)
        attendance_list.append(attendance_count1)
        
    students_attendance = Students.objects.filter(course_id__in = final_course)
    student_list = []
    student_list_attendance_present = []
    student_list_attendance_absent = []
    
    for student in students_attendance:
        attendance_present_count = AttendanceReport.objects.filter(stuatus=True,
                                                                   student_id = student.id).count()
        attendance_absent_count = AttendanceReport.objects.filter(status = False,student_id = student,).count()
        
        student_list.append(student.admin.first_name + " " + student.admin.last_name)
        student_list_attendance_present.append(attendance_present_count)
        student_list_attendance_absent.append(attendance_absent_count)
        
        
        context = {
            "students_count": students_count,
            "attendance_count":attendance_count,
            'leave_count': leave_count,
            "subject_count": subject_count,
            'subject_list': subject_list,
            "attendance_list": attendance_list,
            "student_list": student_list,
            
            'attendance_list':attendance_list,
            'student_list':student_list,
            'attendance_present_list':student_list_attendance_present,
            'attendance_absent_list':student_list_attendance_absent
        }
        return render(request,'staff_template/staff_home_template.html', context)
        
def staff_take_attendance(request):
    subjects = Subjects.objects.filter(staff_id = request.user.id)
    session_years = SessionYearModel.objects.all()
    
    context = {
        "subjects": subjects,
        "session_years": session_years
    }
    return render(request,'staff_template/take_attendance_template.html', context)

def staff_apply_leave(request):
    print(request.user.id)
    staff_obj = Staffs.objects.get(admin=request.user.id)
    leave_data = LeaveReportStaff.objects.filter(staff_id = staff_obj)
    
    context = {
        'leave_data': leave_data,
    }
    return render(request, 'staff_template/staff_apply_leave_template.html', context)

def staff_apply_leave_save(request):
    if request.method != "POST" :
        messages.error(request,'Invalid Method')
        return redirect('staff_apply_leave')
    else:
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        staff_obj = Staffs.objects.get(admin=request.user.id)
        
        try:
            leave_report = LeaveReportStaff(staff_id = staff_obj,
                                            leave_date = leave_date,
                                            leave_message = leave_message,
                                            leave_status = 0)
            leave_report.save()
            messages.success(request, "Applied for Leave")
            return redirect('staff_apply_leave')
        except :
            messages.error(request, "Failed to Apply Leave")
            return redirect('staff_apply_leave')
        
def staff_feedback(request):
    return render(request, 'staff_template/staff_feedback_template.html')

def staff_feedback_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method.")
        return redirect('staff_feedback')
    else:
        feedback = request.POST.get('feedback_message')
        staff_obj = Staffs.objects.get(admin=request.user.id)
        try:
            add_feedback = FeedBackStaffs(staff_id =staff_obj, feedback=feedback, feedback_reply= "")
            add_feedback.save()
            messages.success(request, "Feedback Sent")
            return redirect('staff_feedback')
        except :
            messages.error(request,"Failed to Send Feedback")
            return redirect('staff_feedback')
        
    @csrf_exempt
    def get_students(request):
        subject_id = request.POST.get('subject')
        session_year = request.POST.get('session_year')
        
        # Students enroll to Course, Course has Subjects
        # Getting all data from subject model based on subject_id
        
        subject_model = Subjects.objects.get(id=subject_id)
        session_model = SessionYearModel.objects.get(id=session_year)
        students = Students.objects.filter(course_id = subject_model.course_id, session_year_id = session_model)
        # Only passing Student ID and Student Name Only
        list_data = []
        for student in students:
            data_small = {
                'id':student.admin.admin.id,
                'name':student.admin.first_name + ' ' + student.admin.last_name
            }   
            list_data.append(data_small)
        return redirect(JsonResponse(json.dumps(list_data), content_type = 'application/json', safe=False))
        