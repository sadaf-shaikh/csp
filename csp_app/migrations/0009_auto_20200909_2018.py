# Generated by Django 3.1.1 on 2020-09-09 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csp_app', '0008_auto_20200909_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master_candidate',
            name='created_date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
