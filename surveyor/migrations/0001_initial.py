# Generated by Django 4.1.1 on 2022-10-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Surveyor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('sales_region', models.CharField(choices=[('SC', 'Scotland'), ('NI', 'Northern Ireland'), ('NE', 'North East'), ('NW', 'North West'), ('EM', 'East Midlands'), ('WM', 'West Midlands'), ('WA', 'Wales'), ('SW', 'South West'), ('SE', 'South East'), ('GL', 'Greater London')], default='GL', max_length=2)),
                ('telephone_no', models.CharField(max_length=20)),
                ('mobile_no', models.CharField(blank=True, max_length=20)),
                ('alt_telephone_no', models.CharField(blank=True, max_length=20)),
                ('email_address', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
