from rest_framework import serializers
from todo.models import Todos


class TodosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todos
        fields = ['id', 'title', 'completed', 'order']
