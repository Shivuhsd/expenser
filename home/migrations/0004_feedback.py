# Generated by Django 4.2.3 on 2023-07-04 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=200, null=True)),
                ('message', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]