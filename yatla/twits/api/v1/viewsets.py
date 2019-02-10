from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from yatla.twits.api.v1.filters import TwitModelFilter
from yatla.twits.api.v1.permissions import (
    IsAuthenticatedOnCreate,
    IsAuthenticatedOnTimeLine,
)
from yatla.twits.api.v1.serializers import TwitSerializer
from yatla.twits.models import Twit


class TwitViewSet(viewsets.ModelViewSet):
    queryset = Twit.objects.all()
    serializer_class = TwitSerializer
    permission_classes = [IsAuthenticatedOnCreate, IsAuthenticatedOnTimeLine]
    filterset_class = TwitModelFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=["get"], detail=False)
    def timeline(self, request, *args, **kwargs):
        queryset = self.get_queryset().timeline(user=self.request.user)
        page = self.paginate_queryset(queryset)
        context = self.get_serializer_context()
        if page is not None:
            serializer = self.serializer_class(page, context=context, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(queryset, context=context, many=True)
        return Response(serializer.data)
