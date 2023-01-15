from rest_framework import generics
from .models import Blog
from .serializer import PostSerializer
from .api.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
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