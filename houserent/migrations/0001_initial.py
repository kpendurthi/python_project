# Generated by Django 3.0.5 on 2020-04-08 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('amt', models.TextField()),
                ('image_url', models.TextField(default='https://wp-tid.zillowstatic.com/7/buy-vs-rent-215f3b.jpg')),
                ('description', models.TextField(default='Beautifull home')),
                ('cover', models.ImageField(null=True, upload_to='images/')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='houserent.City')),
            ],
        ),
    ]
