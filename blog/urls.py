from django.urls import path
from .views import BlogDetailsView, BlogListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', BlogListView.as_view(), name='bloglist'),
    path('<int:pk>/', BlogDetailsView.as_view(), name="blogdetails")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
