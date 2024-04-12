from random import random, choice

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .serializers import ProductSerializer
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    # If you need different serializers for actions.
    # def get_serializer_class(self):
    #     if self.action in ('retrieve', 'update', 'destroy'):
    #         return ProductDetailSerializer
    #     return ProductSerializer

    # Option 2: Override get_queryset() method (more flexible)
    def get_queryset(self):
        queryset = Product.objects.all()
        pk = self.request.query_params.get('pk', None)
        if pk:
            queryset = queryset.filter(pk=pk)
        return queryset

    def list(self, request):
        product_list = self.serializer_class(self.queryset, many=True)
        return Response(product_list.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        try:
            product = queryset.get(pk=pk)  # Use get() to retrieve a single product
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)  # Handle product not found

        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = self.get_queryset()
        try:
            product = queryset.get(pk=pk)  # Use get() to retrieve a single product
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)  # Handle product not found

        serializer = self.serializer_class(instance=product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        try:
            product = queryset.get(pk=pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = choice(users)
        return Response({'id': user.id}, status=status.HTTP_200_OK)
