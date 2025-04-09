from django.urls import path
from student import views
from django.contrib.auth.views import LoginView

urlpatterns = [
path('studentclick', views.studentclick_view),
path('studentlogin', LoginView.as_view(template_name='student/studentlogin.html'),name='studentlogin'),
path('studentsignup', views.student_signup_view,name='studentsignup'),
path('student-dashboard', views.student_dashboard_view,name='student-dashboard'),
path('student-exam', views.student_exam_view,name='student-exam'),
path('take-exam/<int:pk>', views.take_exam_view,name='take-exam'),
path('check-exam/<int:pk>', views.check_test,name='check-exam'),
path('check-exam/cm/<int:pk>', views.check,name='cm'),

path('start-exam/<int:pk>', views.start_exam_view,name='start-exam'),
path('calculate-marks', views.calculate_marks_view,name='calculate-marks'),
path('view-result', views.view_result_view,name='view-result'),
path('check-marks/<int:pk>', views.check_marks_view,name='check-marks'),
path('exam-submitted/<int:pk>', views.check_exam_submitted,name='exam-submitted'),
path('student-marks', views.student_marks_view,name='student-marks'),
path('count_people', views.count_people, name='count_people'),
    path('save_image', views.save_image, name='save_image'),

]