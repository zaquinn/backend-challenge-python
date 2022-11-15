# Generated by Django 4.1.2 on 2022-11-15 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="transaction_type",
            field=models.CharField(
                choices=[
                    ("Entrada", "Entrada"),
                    ("Saída", "Saida"),
                    ("Não Informado", "Nao Informado"),
                ],
                default="Não Informado",
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="description",
            field=models.CharField(
                choices=[
                    ("Débito", "Debito"),
                    ("Boleto", "Boleto"),
                    ("Financiamento", "Financiamento"),
                    ("Crédito", "Credito"),
                    ("Recebimento Empréstimo", "Recebimento Emprestimo"),
                    ("Vendas", "Vendas"),
                    ("Recebimento TED", "Recebimento Ted"),
                    ("Recebimento DOC", "Recebimento Doc"),
                    ("Aluguel", "Aluguel"),
                ],
                max_length=25,
            ),
        ),
    ]
