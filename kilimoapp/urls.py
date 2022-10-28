from django.urls import re_path
from . import views


urlpatterns = [
    re_path('^$', views.home, name='home'),
    re_path('^student/(?P<student_id>[0-9]{1,2})/details$', views.student_edit, name='studentDetails'),    
    re_path('^student/(?P<student_id>[0-9]{1,2})/update$', views.update_student, name='studentDetailsUpdate'),    
    re_path('^student/(?P<student_id>[0-9]{1,2})/delete$', views.delete_student, name='studentDetailsDelete'),    
    re_path('^stream/(?P<stream_id>[0-9]{1,2})/details$', views.stream_view, name='streamView'),    
    re_path('^new-student$', views.new_student, name='new_student'),
    re_path('^add/student$', views.add_student, name='add_student'),
]
