
from django.urls import path
from . import views
from .views import StandardListView, SubjectListView, LessonListView, LessonDetailView



app_name = 'curriculum'


urlpatterns = [
    path('', StandardListView.as_view(), name='standard_list'),
    path('<slug:slug>/subjects/', SubjectListView.as_view(), name='subject_list'),
    path('lesson/<slug:slug>/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/<slug:slug>/detail/', LessonDetailView.as_view(), name='lesson_detail'),

  

]