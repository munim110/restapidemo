from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.


class addProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'price']

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': 'success'})
        return Response({'result': 'failure'})
    
    def delete(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response({'result': 'success'})
        return Response({'result': 'failure'})

    def put(self, request, pk):
        serializer = ProductSerializer(data=request.data)
        instance = Product.objects.get(pk=pk)
        if serializer.is_valid():
            serializer.update(instance=instance, validated_data=request.data)
            return Response({'result': 'success'})
        return Response({'result': 'failure'})
    