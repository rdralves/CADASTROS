# Generated by Django 4.2 on 2023-04-24 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroCliente', '0005_alter_cliente_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profissao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
