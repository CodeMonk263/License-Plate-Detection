# Generated by Django 3.0.5 on 2020-06-25 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_visitormodel_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitormodel',
            name='accepted',
            field=models.CharField(default='N/A', max_length=3),
        ),
    ]
