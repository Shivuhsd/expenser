# Generated by Django 4.2.2 on 2023-07-02 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='user_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
