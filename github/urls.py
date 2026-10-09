from django.urls import path
from .views import GithubUserEventsView

urlpatterns = [
    path('events/', GithubUserEventsView.as_view(), name = 'github_user_events'),
]