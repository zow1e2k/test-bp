from rest_framework import generics, permissions
from products.models import Product
from api.v1.serializers.product_serializer import ProductSerializer
from users.user_products.models import UserProducts


class AvailableProductsListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        purchased_products = UserProducts.objects.filter(user=user).values_list('products', flat=True)
        return Product.objects.exclude(id__in=purchased_products)