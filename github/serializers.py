from rest_framework import serializers

from datetime import datetime

class GithubEventSerializer(serializers.Serializer):
    id = serializers.CharField()
    type = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    repo_name = serializers.SerializerMethodField()

    def get_type(self, obj):
        event_type = obj['type']

        if event_type.endswith('Event'):
            return event_type[:-5]
        
        return event_type

    def get_created_at(self, obj):
        created_at = datetime.fromisoformat(obj['created_at'].replace("Z", "+00:00"))

        return created_at.strftime("%m/%d — %I:%M %p")
    
    def get_repo_name(self, obj):
        return obj['repo']['name']
