from django.shortcuts import render
from rest_framework import generics
from todo.models import Todos
from django.views.generic import View

from todo.serializers import TodosSerializer


class TodosView(generics.ListCreateAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

class TodosDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
