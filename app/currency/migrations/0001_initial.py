# Generated by Django 3.2.4 on 2021-06-14 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=5)),
                ('sale', models.DecimalField(decimal_places=2, max_digits=5)),
                ('buy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
