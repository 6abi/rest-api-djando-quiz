from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissions


class PostUserWritePermission(BasePermission):
    """ Permissões de Edição dos Posts, somente é editável pelo autor """
    message = "Edições em uma publicação somente podem ser feitas pelos próprios autores"

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class PostList(generics.ListCreateAPIView):
    """Listar o conteúdo e limpar depois """
    permission_classes = [DjangoModelPermissions]
    #IsAdminUser
    #DjangoModelPermissionsOrAnonReadOnly
    #DjangoModelPermissions
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class  PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    """Detalhes de cada item do POST (cada JSON) e limpar depois """
    permission_classes = [PostUserWritePermission]
    queryset =  Post.objects.all()
    serializer_class =  PostSerializer