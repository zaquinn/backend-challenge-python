from rest_framework import serializers
from .models import Cnab
from transactions.serializers import TransactionSerializer
from transactions.models import Transaction

class CnabSerializer(serializers.ModelSerializer):
    transaction = TransactionSerializer(required=False)
    class Meta:
        model = Cnab
        fields = ["id","date", "value","cpf", "card", "hour", "owner", "store_name", "transaction"]