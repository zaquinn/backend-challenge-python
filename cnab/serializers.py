from rest_framework import serializers
from .models import Cnab
from transactions.serializers import TransactionSerializer

class CnabSerializer(serializers.ModelSerializer):
    transaction = TransactionSerializer(read_only=True)
    class Meta:
        model = Cnab
        fields = ["date", "value","cpf", "card", "hour", "owner", "store_name", "transaction"]