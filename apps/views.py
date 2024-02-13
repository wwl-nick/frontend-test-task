from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from apps.models import Platform, App
from apps.permissions import OnlyAuthor
from apps.serializers import PlatformSerializer, AppSerializer


class PlatformViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = (IsAuthenticated,)


class AppViewSet(viewsets.ModelViewSet):
    serializer_class = AppSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('name',)
    filterset_fields = ('platform',)
    permission_classes = (IsAuthenticated, OnlyAuthor)

    def get_queryset(self):
        return App.objects.filter(author__id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
