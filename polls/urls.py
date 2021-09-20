from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.PollView.as_view(), name='poll'),
    path('<int:pk>/question/<int:question_id>/', views.QuestionView.as_view(), name='question'),
    path('<int:pk>/question/<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:pk>/question/<int:question_id>/results/', views.ResultsView.as_view(), name='results')
]