from django.urls import path, include
from attendance import views
# from attendance.views import schema_view
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import include, re_path


urlpatterns = [
    path('students/', views.StudentList.as_view()),
    path('students/<int:pk>/', views.StudentDetail.as_view()),
    path('attendance/', views.RegisterList.as_view()),
    path('attendance/<int:pk>/', views.ResgisterDetail.as_view()),
]