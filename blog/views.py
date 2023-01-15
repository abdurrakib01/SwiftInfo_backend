from rest_framework import generics
from .models import Blog
from .serializer import PostSerializer
from .api.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
# Create your views here.
 

class PostList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class SearhBlog(APIView):

    def post(self, request, format=None):
        data = self.request.data
        str = data['str']
        q = (Q(title__icontains = str))
        queryset = Blog.objects.all()
        queryset = queryset.filter(q)
        serializer = PostSerializer(queryset, many=True)
        return Response (serializer.data)
