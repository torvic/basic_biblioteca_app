# Generated by Django 3.1.7 on 2021-04-03 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0005_auto_20210402_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor_id',
            field=models.ManyToManyField(related_name='groups', to='libro.Autor'),
        ),
    ]
