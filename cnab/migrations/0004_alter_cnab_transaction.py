# Generated by Django 4.1.2 on 2022-11-15 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0003_alter_transaction_description"),
        ("cnab", "0003_alter_cnab_cpf_alter_cnab_transaction"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cnab",
            name="transaction",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cnab",
                to="transactions.transaction",
            ),
        ),
    ]
