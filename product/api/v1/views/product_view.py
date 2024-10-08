from rest_framework import generics, permissions
from products.models import Product
from api.v1.serializers.product_serializer import ProductSerializer
from users.user_subscriptions.models import UserSubscription


class AvailableProductsListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        purchased_products = UserSubscription.objects.filter(user=user).values_list('products', flat=True)
        return Product.objects.exclude(id__in=purchased_products)