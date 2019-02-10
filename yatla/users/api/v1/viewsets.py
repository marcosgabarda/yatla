from rest_framework import viewsets

from yatla.users.api.v1.permissions import IsAuthenticatedOnRetrieve, NoDeletes
from yatla.users.api.v1.serializers import UserSerializer
from yatla.users.models import User


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOnRetrieve, NoDeletes]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.request.user.pk)  # Only list current user

    def get_object(self):
        if self.kwargs.get("pk", None) == "me":
            self.kwargs["pk"] = self.request.user.id
        return super().get_object()


me = UserViewSet.as_view({"get": "retrieve", "patch": "partial_update"})
