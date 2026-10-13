from rest_framework.views import APIView
from rest_framework.response import Response

from .services import get_github_user_events
from .serializers import GithubEventSerializer

from django.core.cache import cache

# Create your views here.

class GithubUserEventsView(APIView):
    def get(self, request):
        username = request.query_params.get("username")

        if not username:
            return Response({"error": "username is required"},status=400)

        username = username.strip()
        cache_key = f"github_events:{username.lower()}"

        cached_events = cache.get(cache_key)

        if cached_events is not None:
            return Response(cached_events)

        try:
            events = get_github_user_events(username)

        except LookupError:
            return Response({"error": "GitHub user not found"},status=404)

        except TimeoutError:
            return Response({"error": "GitHub API timed out"},status=504)

        except ConnectionError:
            return Response({"error": "Could not connect to GitHub"},status=502)

        except PermissionError:
            return Response({"error": "GitHub API access limit or restriction"},status=503)

        except RuntimeError:
            return Response({"error": "GitHub API error"},status=502,)

        serializer = GithubEventSerializer(events, many=True)

        data = list(serializer.data)

        cache.set(cache_key, data, timeout=300)

        return Response(data)



        