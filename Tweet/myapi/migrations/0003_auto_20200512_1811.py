# Generated by Django 3.0.6 on 2020-05-12 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20200512_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='user_id',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet',
            field=models.CharField(max_length=120),
        ),
    ]
