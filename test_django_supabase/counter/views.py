from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Counter
from .serializers import CounterSerializer

class CounterView(APIView):
    def get(self, request):
        counter, created = Counter.objects.get_or_create(pk=1)
        counter.value += 1
        counter.save()
        serializer = CounterSerializer(counter)
        return Response(serializer.data)