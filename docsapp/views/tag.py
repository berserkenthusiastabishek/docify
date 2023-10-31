from django.http import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework import status, generics, mixins
from docsapp.models.tag import Tag
from docsapp.serializers.tag import TagSerializer
from docsapp.permissions import IsCreatorPermission


class TagList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes=[SessionAuthentication]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
class TagsByMember(generics.ListCreateAPIView):
    # permissions = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes=[SessionAuthentication]
    serializer_class = TagSerializer
    def get_queryset(self):
        user = self.request.user
        try:
            return Tag.objects.filter(users__user=user)
        except Tag.DoesNotExist:
            return None

class IndividualTagReadOnly(ReadOnlyModelViewSet):
    # permissions = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    authentication_classes=[SessionAuthentication]
    serializer_class = TagSerializer
    def get_queryset(self):
        try:
            return Tag.objects.get(name=self.kwargs['name'])
        except Tag.DoesNotExist:
            return None
    
    
class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    # permissions = [IsAuthenticated]
    # permissions = [IsCreatorPermission]
    permission_classes = [IsAuthenticated]
    authentication_classes=[SessionAuthentication]
    lookup_field = 'id'
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

