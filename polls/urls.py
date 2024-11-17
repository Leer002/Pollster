from django.urls import path

from .views import IndexView, DetailView, ResultsView, VoteView

app_name = 'polls'

urlpatterns = [
    path('polls/', IndexView.as_view(), name='index'),
    path('<int:question_id>/', DetailView.as_view(), name='detail'),
    path('<int:question_id>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', VoteView.as_view(), name='vote'),
]