from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    """Listar o conteúdo e limpar depois """
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pass

class  PostDetail(generics.RetrieveDestroyAPIView):
    """Detalhres de cada item do POST e limpar depois """
    pass