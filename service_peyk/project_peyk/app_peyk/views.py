from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers, models
from django.db import connection


@api_view(['POST'])
def subscribe_coin(request) -> Response:
    serializer = serializers.AlertSubscriptionSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'message': serializer.errors}, status.HTTP_400_BAD_REQUEST)

    all_coin_names = [coin.coin_name for coin in models.Coin.objects.all()]
    if serializer.validated_data['coin_name'] not in all_coin_names:
        return Response({'message': 'this coin is not valid'}, status.HTTP_400_BAD_REQUEST)

    try:
        alert_subscription = models.AlertSubscriptions(
            email = serializer.validated_data['email'],
            coin_name = serializer.validated_data['coin_name'],
            difference_percentage = serializer.validated_data['difference_percentage']
        )
        alert_subscription.save()
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_400_BAD_REQUEST)

    return Response({'message': alert_subscription.__str__()}, status.HTTP_200_OK)

@api_view(['POST'])
def get_price_history(request) -> Response:
    serializer = serializers.CoinSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'message': serializer.errors}, status.HTTP_400_BAD_REQUEST)

    all_coin_names = [coin.coin_name for coin in models.Coin.objects.all()]
    if serializer.validated_data['coin_name'] not in all_coin_names:
        return Response({'message': 'this coin is not valid'}, status.HTTP_400_BAD_REQUEST)

    try:
        query = f"select * from Prices where coin_name='{serializer.validated_data['coin_name']}'"
        cursor = connection.cursor()
        cursor.execute(query)
        
        all_prices = [
            {
                'coin_name': price[0],
                'time_stamp': price[1],
                'price': price[2]
            }
            for price in cursor.fetchall()
        ]
    except Exception as e:
        return Response({'message': str(e)}, status.HTTP_400_BAD_REQUEST)   

    return Response({'message':  all_prices}, status.HTTP_200_OK)
