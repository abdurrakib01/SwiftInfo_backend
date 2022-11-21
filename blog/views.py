from rest_framework import generics
from .models import Blog
from .serializer import BlogSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    

# class BlogView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def get(self, request, *args, **kwargs):
#         posts = Blog.objects.all()
#         serializer = BlogSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         posts_serializer = BlogSerializer(data=request.data)
#         if posts_serializer.is_valid():
#             posts_serializer.save()
#             return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print('error', posts_serializer.errors)
#             return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)