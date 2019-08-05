# Generated by Django 2.2.3 on 2019-07-31 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=100)),
                ('lastname', models.CharField(blank=True, max_length=100)),
                ('contact_num', models.IntegerField(blank=True)),
                ('contact_email', models.EmailField(blank=True, max_length=70)),
            ],
        ),
    ]