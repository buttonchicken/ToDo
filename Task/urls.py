from django.urls import path
from .views import *

urlpatterns = [
    path('add', AddTask.as_view()),
    path('mark_complete', MarkCompleted.as_view()),
    path('delete',DeleteTask.as_view()),
    path('show',ShowAllTask.as_view()),
]
