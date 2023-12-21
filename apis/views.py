from rest_framework import generics
from post.models import Post
from .serializers import PostSerializer
class BookAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
