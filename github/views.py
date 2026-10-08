from rest_framework.views import APIView
from rest_framework.response import Response

from .services import get_github_user_events

# Create your views here.

class GithubUserEventsView(APIView):
    def get(self, requests, username):
        events = get_github_user_events(username)
        return Response(events)