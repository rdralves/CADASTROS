# Generated by Django 4.2 on 2023-04-20 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroCliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='bairro',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cep',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cidade',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.IntegerField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nro',
            field=models.IntegerField(null=True),
        ),
    ]
