from rest_framework import serializers

class CoinSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    coin_name = serializers.CharField(max_length=100)

class AlertSubscriptionSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    email = serializers.EmailField(max_length=100)
    coin_name = serializers.CharField(max_length=100)
    difference_percentage = serializers.IntegerField(min_value=0, max_value=100)
