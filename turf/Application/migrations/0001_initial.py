# Generated by Django 5.0.6 on 2024-09-19 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='turfuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('ucontact', models.CharField(max_length=255)),
                ('umail', models.CharField(max_length=255)),
                ('uaddress', models.CharField(max_length=255)),
            ],
        ),
    ]
