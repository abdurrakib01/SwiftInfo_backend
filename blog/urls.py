from django.urls import path, include
from .views import PostList, PostDetail, SearhBlog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostList.as_view(), name='bloglist'),
    path('<int:pk>/', PostDetail.as_view(), name="blogdetails"),
    path('auth-user/', include('rest_framework.urls')),
    path('search/', SearhBlog.as_view(), name='searchblog'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
