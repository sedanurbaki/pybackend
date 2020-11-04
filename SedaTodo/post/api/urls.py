from django.urls import path

from django.contrib import admin
from post.api.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api-auth/', include('rest_framework.urls')),
    path('list', PostListAPIView.as_view(), name='list'),
    path('detail/<int:pk>', PostDetailAPIView.as_view(), name='detail'),
    path('delete/<int:pk>', PostDeleteAPIView.as_view(), name='delete'),
    path('update/<int:pk>', PostUpdateAPIView.as_view(), name='update'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
]