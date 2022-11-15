from django.db import models



class TransactionDescriptions(models.TextChoices):
    DEBITO = "Débito"
    BOLETO = "Boleto"
    FINANCIAMENTO = "Financiamento"
    CREDITO = "Crédito"
    RECEBIMENTO_EMPRESTIMO = "Recebimento Empréstimo"
    VENDAS = "Vendas"
    RECEBIMENTO_TED = "Recebimento TED"
    RECEBIMENTO_DOC = "Recebimento DOC"
    ALUGUEL = "Aluguel"

class TransactionTypes(models.TextChoices):
    ENTRADA = "Entrada"
    SAIDA = "Saída"
    NAO_INFORMADO = "Não Informado"

# Create your models here.
class Transaction(models.Model):
    description = models.CharField(max_length=25, choices=TransactionDescriptions.choices, unique=True)
    transaction_type = models.CharField(max_length=25, choices=TransactionTypes.choices, default=TransactionTypes.NAO_INFORMADO)