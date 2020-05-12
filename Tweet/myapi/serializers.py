# serializers.py

from rest_framework import serializers

    

class TweetsSerializer(serializers.Serializer):
    tweet = serializers.CharField(max_length=120)
    user = serializers.CharField(max_length=120)
    user_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return Tweet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tweet = validated_data.get('tweet', instance.tweet)
        instance.user_id = validated_data.get('user_id', instance.user_id)

        instance.save()
        return instance

    
class UsersSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    