# Generated by Django 2.1 on 2018-08-14 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userarticle_view_nums'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userarticle',
            name='title',
            field=models.CharField(max_length=200, verbose_name='标题'),
        ),
    ]
