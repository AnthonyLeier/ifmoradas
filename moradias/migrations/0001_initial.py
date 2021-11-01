# Generated by Django 3.2.6 on 2021-10-31 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moradia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=500)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imagem1', models.CharField(max_length=500)),
                ('imagem2', models.CharField(max_length=500)),
                ('imagem3', models.CharField(max_length=500)),
            ],
        ),
    ]
