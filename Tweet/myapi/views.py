
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TweetsSerializer, UsersSerializer
from .models import Tweet , User

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        
        name = request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        serializer = UsersSerializer(users , many=True)
        return Response({"users": serializer.data})

class TweetView(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
         # the many param informs the serializer that it will be serializing more than a single article.
        
        serializer = TweetsSerializer(tweets, many=True)
        return Response({"tweets": serializer.data})
        
    def post(self, request):
        myapi = request.data.get('myapi')

        # Create an article from the above data
        serializer = TweetsSerializer(data=myapi)
        if serializer.is_valid(raise_exception=True):
            tweet_saved = serializer.save()
        return Response({"success": "Tweet '{}' created successfully".format(tweet_saved.tweet)})

    def put(self, request, pk):
        tweet_saved = get_object_or_404(Tweet.objects.all(), pk=pk)
        data = request.data.get('myapi')
        serializer = TweetsSerializer(instance=tweet_saved, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            tweet_saved = serializer.save()
        return Response({"success": "Tweet '{}' updated successfully".format(tweet_saved.tweet)})

    def delete(self, request, pk):
    # Get object with this pk
        myapi = get_object_or_404(Tweet.objects.all(), pk=pk)
        myapi.delete()
        return Response({"message": "Tweet with id `{}` has been deleted.".format(pk)},status=204)


