# Generated by Django 2.1.1 on 2018-12-27 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0006_auto_20181117_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='de_ferias',
            field=models.BooleanField(default=False),
        ),
    ]
