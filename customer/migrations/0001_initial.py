# Generated by Django 4.1.1 on 2022-10-08 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(blank=True, max_length=100)),
                ('address3', models.CharField(blank=True, max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100)),
                ('post_code', models.CharField(max_length=12)),
                ('contact_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(blank=True, max_length=254)),
                ('telephone_no', models.CharField(max_length=20)),
                ('mobile_no', models.CharField(blank=True, max_length=20)),
                ('alt_telephone_no', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
