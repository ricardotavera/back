
from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.api.serializers import PostSerializer
# Create your views here.

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()