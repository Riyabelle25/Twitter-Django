# Generated by Django 3.0.6 on 2020-05-12 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_auto_20200512_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='user_id',
        ),
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to='myapi.User'),
        ),
    ]
