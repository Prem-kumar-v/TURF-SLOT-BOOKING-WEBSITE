# Generated by Django 5.0.6 on 2024-09-21 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0005_cricket1'),
    ]

    operations = [
        migrations.CreateModel(
            name='basketball',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdate', models.DateField()),
                ('FIVEAM', models.CharField(default='green', max_length=255)),
                ('SIXAM', models.CharField(default='green', max_length=255)),
                ('SEVENAM', models.CharField(default='green', max_length=255)),
                ('EIGHTAM', models.CharField(default='green', max_length=255)),
                ('NINEAM', models.CharField(default='green', max_length=255)),
                ('TENAM', models.CharField(default='green', max_length=255)),
                ('ELEAM', models.CharField(default='green', max_length=255)),
                ('TWEPM', models.CharField(default='green', max_length=255)),
                ('ONEPM', models.CharField(default='green', max_length=255)),
                ('TWOPM', models.CharField(default='green', max_length=255)),
                ('THREEPM', models.CharField(default='green', max_length=255)),
                ('FOURPM', models.CharField(default='green', max_length=255)),
                ('FIVEPM', models.CharField(default='green', max_length=255)),
                ('SIXPM', models.CharField(default='green', max_length=255)),
                ('SEVENPM', models.CharField(default='green', max_length=255)),
                ('EIGHTPM', models.CharField(default='green', max_length=255)),
                ('NINEPM', models.CharField(default='green', max_length=255)),
                ('TENPM', models.CharField(default='green', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='basketball1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdate', models.DateField()),
                ('FIVEAM', models.CharField(default='show', max_length=255)),
                ('SIXAM', models.CharField(default='show', max_length=255)),
                ('SEVENAM', models.CharField(default='show', max_length=255)),
                ('EIGHTAM', models.CharField(default='show', max_length=255)),
                ('NINEAM', models.CharField(default='show', max_length=255)),
                ('TENAM', models.CharField(default='show', max_length=255)),
                ('ELEAM', models.CharField(default='show', max_length=255)),
                ('TWEPM', models.CharField(default='show', max_length=255)),
                ('ONEPM', models.CharField(default='show', max_length=255)),
                ('TWOPM', models.CharField(default='show', max_length=255)),
                ('THREEPM', models.CharField(default='show', max_length=255)),
                ('FOURPM', models.CharField(default='show', max_length=255)),
                ('FIVEPM', models.CharField(default='show', max_length=255)),
                ('SIXPM', models.CharField(default='show', max_length=255)),
                ('SEVENPM', models.CharField(default='show', max_length=255)),
                ('EIGHTPM', models.CharField(default='show', max_length=255)),
                ('NINEPM', models.CharField(default='show', max_length=255)),
                ('TENPM', models.CharField(default='show', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='football',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdate', models.DateField()),
                ('FIVEAM', models.CharField(default='green', max_length=255)),
                ('SIXAM', models.CharField(default='green', max_length=255)),
                ('SEVENAM', models.CharField(default='green', max_length=255)),
                ('EIGHTAM', models.CharField(default='green', max_length=255)),
                ('NINEAM', models.CharField(default='green', max_length=255)),
                ('TENAM', models.CharField(default='green', max_length=255)),
                ('ELEAM', models.CharField(default='green', max_length=255)),
                ('TWEPM', models.CharField(default='green', max_length=255)),
                ('ONEPM', models.CharField(default='green', max_length=255)),
                ('TWOPM', models.CharField(default='green', max_length=255)),
                ('THREEPM', models.CharField(default='green', max_length=255)),
                ('FOURPM', models.CharField(default='green', max_length=255)),
                ('FIVEPM', models.CharField(default='green', max_length=255)),
                ('SIXPM', models.CharField(default='green', max_length=255)),
                ('SEVENPM', models.CharField(default='green', max_length=255)),
                ('EIGHTPM', models.CharField(default='green', max_length=255)),
                ('NINEPM', models.CharField(default='green', max_length=255)),
                ('TENPM', models.CharField(default='green', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='football1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdate', models.DateField()),
                ('FIVEAM', models.CharField(default='show', max_length=255)),
                ('SIXAM', models.CharField(default='show', max_length=255)),
                ('SEVENAM', models.CharField(default='show', max_length=255)),
                ('EIGHTAM', models.CharField(default='show', max_length=255)),
                ('NINEAM', models.CharField(default='show', max_length=255)),
                ('TENAM', models.CharField(default='show', max_length=255)),
                ('ELEAM', models.CharField(default='show', max_length=255)),
                ('TWEPM', models.CharField(default='show', max_length=255)),
                ('ONEPM', models.CharField(default='show', max_length=255)),
                ('TWOPM', models.CharField(default='show', max_length=255)),
                ('THREEPM', models.CharField(default='show', max_length=255)),
                ('FOURPM', models.CharField(default='show', max_length=255)),
                ('FIVEPM', models.CharField(default='show', max_length=255)),
                ('SIXPM', models.CharField(default='show', max_length=255)),
                ('SEVENPM', models.CharField(default='show', max_length=255)),
                ('EIGHTPM', models.CharField(default='show', max_length=255)),
                ('NINEPM', models.CharField(default='show', max_length=255)),
                ('TENPM', models.CharField(default='show', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='handball',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdate', models.DateField()),
                ('FIVEAM', models.CharField(default='green', max_length=255)),
                ('SIXAM', models.CharField(default='green', max_length=255)),
                ('SEVENAM', models.CharField(default='green', max_length=255)),
                ('EIGHTAM', models.CharField(default='green', max_length=255)),
                ('NINEAM', models.CharField(default='green', max_length=255)),
                ('TENAM', models.CharField(default='green', max_length=255)),
                ('ELEAM', models.CharField(default='green', max_length=255)),
                ('TWEPM', models.CharField(default='green', max_length=255)),
                ('ONEPM', models.CharField(default='green', max_length=255)),
                ('TWOPM', models.CharField(default='green', max_length=255)),
                ('THREEPM', models.CharField(default='green', max_length=255)),
                ('FOURPM', models.CharField(default='green', max_length=255)),
                ('FIVEPM', models.CharField(default='green', max_length=255)),
                ('SIXPM', models.CharField(default='green', max_length=255)),
                ('SEVENPM', models.CharField(default='green', max_length=255)),
                ('EIGHTPM', models.CharField(default='green', max_length=255)),
                ('NINEPM', models.CharField(default='green', max_length=255)),
                ('TENPM', models.CharField(default='green', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='handball1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdate', models.DateField()),
                ('FIVEAM', models.CharField(default='show', max_length=255)),
                ('SIXAM', models.CharField(default='show', max_length=255)),
                ('SEVENAM', models.CharField(default='show', max_length=255)),
                ('EIGHTAM', models.CharField(default='show', max_length=255)),
                ('NINEAM', models.CharField(default='show', max_length=255)),
                ('TENAM', models.CharField(default='show', max_length=255)),
                ('ELEAM', models.CharField(default='show', max_length=255)),
                ('TWEPM', models.CharField(default='show', max_length=255)),
                ('ONEPM', models.CharField(default='show', max_length=255)),
                ('TWOPM', models.CharField(default='show', max_length=255)),
                ('THREEPM', models.CharField(default='show', max_length=255)),
                ('FOURPM', models.CharField(default='show', max_length=255)),
                ('FIVEPM', models.CharField(default='show', max_length=255)),
                ('SIXPM', models.CharField(default='show', max_length=255)),
                ('SEVENPM', models.CharField(default='show', max_length=255)),
                ('EIGHTPM', models.CharField(default='show', max_length=255)),
                ('NINEPM', models.CharField(default='show', max_length=255)),
                ('TENPM', models.CharField(default='show', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='kabaddi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdate', models.DateField()),
                ('FIVEAM', models.CharField(default='green', max_length=255)),
                ('SIXAM', models.CharField(default='green', max_length=255)),
                ('SEVENAM', models.CharField(default='green', max_length=255)),
                ('EIGHTAM', models.CharField(default='green', max_length=255)),
                ('NINEAM', models.CharField(default='green', max_length=255)),
                ('TENAM', models.CharField(default='green', max_length=255)),
                ('ELEAM', models.CharField(default='green', max_length=255)),
                ('TWEPM', models.CharField(default='green', max_length=255)),
                ('ONEPM', models.CharField(default='green', max_length=255)),
                ('TWOPM', models.CharField(default='green', max_length=255)),
                ('THREEPM', models.CharField(default='green', max_length=255)),
                ('FOURPM', models.CharField(default='green', max_length=255)),
                ('FIVEPM', models.CharField(default='green', max_length=255)),
                ('SIXPM', models.CharField(default='green', max_length=255)),
                ('SEVENPM', models.CharField(default='green', max_length=255)),
                ('EIGHTPM', models.CharField(default='green', max_length=255)),
                ('NINEPM', models.CharField(default='green', max_length=255)),
                ('TENPM', models.CharField(default='green', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='kabaddi1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdate', models.DateField()),
                ('FIVEAM', models.CharField(default='show', max_length=255)),
                ('SIXAM', models.CharField(default='show', max_length=255)),
                ('SEVENAM', models.CharField(default='show', max_length=255)),
                ('EIGHTAM', models.CharField(default='show', max_length=255)),
                ('NINEAM', models.CharField(default='show', max_length=255)),
                ('TENAM', models.CharField(default='show', max_length=255)),
                ('ELEAM', models.CharField(default='show', max_length=255)),
                ('TWEPM', models.CharField(default='show', max_length=255)),
                ('ONEPM', models.CharField(default='show', max_length=255)),
                ('TWOPM', models.CharField(default='show', max_length=255)),
                ('THREEPM', models.CharField(default='show', max_length=255)),
                ('FOURPM', models.CharField(default='show', max_length=255)),
                ('FIVEPM', models.CharField(default='show', max_length=255)),
                ('SIXPM', models.CharField(default='show', max_length=255)),
                ('SEVENPM', models.CharField(default='show', max_length=255)),
                ('EIGHTPM', models.CharField(default='show', max_length=255)),
                ('NINEPM', models.CharField(default='show', max_length=255)),
                ('TENPM', models.CharField(default='show', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='volleyball',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdate', models.DateField()),
                ('FIVEAM', models.CharField(default='green', max_length=255)),
                ('SIXAM', models.CharField(default='green', max_length=255)),
                ('SEVENAM', models.CharField(default='green', max_length=255)),
                ('EIGHTAM', models.CharField(default='green', max_length=255)),
                ('NINEAM', models.CharField(default='green', max_length=255)),
                ('TENAM', models.CharField(default='green', max_length=255)),
                ('ELEAM', models.CharField(default='green', max_length=255)),
                ('TWEPM', models.CharField(default='green', max_length=255)),
                ('ONEPM', models.CharField(default='green', max_length=255)),
                ('TWOPM', models.CharField(default='green', max_length=255)),
                ('THREEPM', models.CharField(default='green', max_length=255)),
                ('FOURPM', models.CharField(default='green', max_length=255)),
                ('FIVEPM', models.CharField(default='green', max_length=255)),
                ('SIXPM', models.CharField(default='green', max_length=255)),
                ('SEVENPM', models.CharField(default='green', max_length=255)),
                ('EIGHTPM', models.CharField(default='green', max_length=255)),
                ('NINEPM', models.CharField(default='green', max_length=255)),
                ('TENPM', models.CharField(default='green', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='volleyball1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdate', models.DateField()),
                ('FIVEAM', models.CharField(default='show', max_length=255)),
                ('SIXAM', models.CharField(default='show', max_length=255)),
                ('SEVENAM', models.CharField(default='show', max_length=255)),
                ('EIGHTAM', models.CharField(default='show', max_length=255)),
                ('NINEAM', models.CharField(default='show', max_length=255)),
                ('TENAM', models.CharField(default='show', max_length=255)),
                ('ELEAM', models.CharField(default='show', max_length=255)),
                ('TWEPM', models.CharField(default='show', max_length=255)),
                ('ONEPM', models.CharField(default='show', max_length=255)),
                ('TWOPM', models.CharField(default='show', max_length=255)),
                ('THREEPM', models.CharField(default='show', max_length=255)),
                ('FOURPM', models.CharField(default='show', max_length=255)),
                ('FIVEPM', models.CharField(default='show', max_length=255)),
                ('SIXPM', models.CharField(default='show', max_length=255)),
                ('SEVENPM', models.CharField(default='show', max_length=255)),
                ('EIGHTPM', models.CharField(default='show', max_length=255)),
                ('NINEPM', models.CharField(default='show', max_length=255)),
                ('TENPM', models.CharField(default='show', max_length=255)),
            ],
        ),
    ]
