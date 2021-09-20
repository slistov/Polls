from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:poll_id>/', views.poll, name='poll'),
    # ex: /polls/1/question/2
    path('<int:poll_id>/question/<int:question_id>/', views.question, name='question'),
    # ex: /polls/1/question/2/vote/
    path('<int:poll_id>/question/<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /polls/1/question/5/results/
    path('<int:poll_id>/question/<int:question_id>/results/', views.results, name='results')
]