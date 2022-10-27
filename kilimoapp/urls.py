from django.urls import re_path
from . import views


urlpatterns = [
    re_path('^$', views.home, name='home'),
    re_path('^student/(?P<student_id>[0-9]{1,2})/details$', views.student_edit, name='studentDetails'),    
    re_path('^stream/(?P<stream_id>[0-9]{1,2})/details$', views.stream_view, name='streamView'),    
    re_path('^add/student$', views.new_student, name='new_student'),
]