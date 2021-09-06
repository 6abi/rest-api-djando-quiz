from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    """Listar o conteúdo e limpar depois """
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class  PostDetail(generics.RetrieveDestroyAPIView):
    """Detalhes de cada item do POST e limpar depois """
    queryset =  Post.objects.all()
    serializer_class =  PostSerializer