from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.pay.models import Transaction
from products.models import Product
from api.v1.serializers.transaction_serializer import TransactionSerializer
from users.models import CustomUser
from users.user_balance.models import UserBalance
from users.user_subscriptions.models import UserSubscription

@api_view(['POST'])
def pay(request):
    user_id = request.data.get('user_id')
    product_id = request.data.get('product_id')

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product не найден'}, status=status.HTTP_404_NOT_FOUND)

    try:
        user = CustomUser.objects.get(id=user_id)
    except Product.DoesNotExist:
        return Response({'error': 'CustomUser не найден'}, status=status.HTTP_404_NOT_FOUND)

    try:
        user_balance = UserBalance.objects.get(user=user)
    except Product.DoesNotExist:
        return Response({'error': 'UserBalance не найден'}, status=status.HTTP_404_NOT_FOUND)

    if user_balance.balance_value < product.price:
        return Response({'error': 'Недостаточно средств'}, status=status.HTTP_400_BAD_REQUEST)

    user_subscription = UserSubscription.objects.get(user=user)

    for prod in user_subscription.products.all():
        if prod.id == product.id:
            return Response({'error': 'У Вас уже куплен данный продукт'}, status=status.HTTP_400_BAD_REQUEST)

    user_balance.balance_value -= product.price
    user_balance.save()

    user_subscription.products.add(product)

    transaction = Transaction.objects.create(
        product = product,
        user = user,
        transaction_value = product.price
    )

    return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)