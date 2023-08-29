from django.urls import path,include
from .views import home,body,studentView,student_addView,StudentAddView,StudentListView,StudentDetailView,StudentUpdateView
urlpatterns = [
    path('', body),
    path('home', home),
    path('student', studentView, name='list'),
    #!2908 forms
    #!2908 FBV
    # path('add', student_addView)
    #!2908 CBV
    path('add', StudentAddView.as_view() , name='add' ),
    path('list', StudentListView.as_view() , name='list2' ),
    path('student-detail/<int:pk>', StudentDetailView.as_view() , name='detail' ),
    path('student-update/<int:pk>', StudentUpdateView.as_view() , name='update' ),
]
