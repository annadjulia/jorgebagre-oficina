# Generated by Django 4.2.7 on 2023-12-04 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_delete_veiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
    ]