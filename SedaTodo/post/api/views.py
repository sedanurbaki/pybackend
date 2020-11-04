from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView,
                                     CreateAPIView, RetrieveUpdateAPIView,
                                     )

from post.api.serializer import PostSerializer
from post.models import Post

@method_decorator(login_required(login_url='admin/'), name='dispatch')
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # slug'a göre detay sayfama gideceğim
    # default olarak lookup_field -> 'PK'
    # lookup_field = 'slug'
    lookup_field = 'pk'


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'



class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # (lookup_field = 'slug' kullanmıyoruz, create işleminde ihtiyaç yok)


