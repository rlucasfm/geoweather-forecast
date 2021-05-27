# Generated by Django 3.2.3 on 2021-05-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=150)),
                ('temperatura', models.DecimalField(decimal_places=2, max_digits=12)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
