from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from todos.models import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'detail', 'status')


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        self.queryset.objects.filter(user=self.request.user)
