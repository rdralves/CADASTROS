# Generated by Django 4.2 on 2023-04-20 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroCliente', '0002_cliente_bairro_cliente_cep_cliente_cidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
