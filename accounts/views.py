from .serializers import (
    UserRegistrationSerializer, 
    UserLoginSerializer,
    SendPasswordResetSerializer,
    UserPasswordResetSerializer, 
    UserProfileSerializer)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .renderers import UserRenderer
from .models import UserInformation
from .serializers import UserInfoSerializer
from rest_framework import generics
from rest_framework import permissions
from blog.api.permissions import IsOwnerOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import Http404
# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
class UserRegistraionView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token,'msg':'Registration Successful'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token, 'msg':'Login Successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'non_field_errors':['email or password is not valid']},
                status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendPasswordResetView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = SendPasswordResetSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Link Send. Please check your email'},
            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data,
        context = {'uid':uid, 'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Successfully'},
            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserInformationList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        userinfo = UserInformation.objects.all()
        serializer = UserInfoSerializer(userinfo, many=True, context={'request':request})
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserInformationDetails(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return UserInformation.objects.get(pk=pk)
        except UserInformation.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        userinfo = self.get_object(pk)
        serializer = UserInfoSerializer(userinfo, context={'request':request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        userinfo = self.get_object(pk)
        serializer = UserInfoSerializer(userinfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        userinfo = self.get_object(pk)
        data = request.data 
        userinfo.profile_image = data.get('profile_image', userinfo.profile_image)
        userinfo.bio = data.get('bio', userinfo.bio)
        userinfo.save()
        serializer = UserInfoSerializer(userinfo)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        userinfo = self.get_object(pk)
        userinfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
