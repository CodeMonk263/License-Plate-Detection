# Generated by Django 3.0.5 on 2020-06-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_visitormodel_time_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitormodel',
            name='accepted',
            field=models.CharField(default='NO', max_length=3),
        ),
    ]
