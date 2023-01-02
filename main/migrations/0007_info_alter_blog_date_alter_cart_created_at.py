# Generated by Django 4.0.4 on 2022-12-29 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_about_member_alter_blog_date_alter_cart_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('description', models.TextField(blank=True)),
                ('logo', models.ImageField(blank=True, upload_to='upload')),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 12, 29, 12, 21, 16, 200856)),
        ),
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 29, 12, 21, 16, 200856)),
        ),
    ]
