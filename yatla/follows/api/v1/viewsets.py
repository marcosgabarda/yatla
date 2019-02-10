from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from yatla.follows.api.v1.filters import FollowModelFilter
from yatla.follows.api.v1.serializers import FollowSerializer
from yatla.follows.models import Follow


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer()
    permission_classes = [IsAuthenticated]
    filterset_class = FollowModelFilter

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
