# Generated by Django 4.1 on 2023-04-20 18:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=64)),
                ('education', models.CharField(max_length=64)),
                ('experience', models.TextField(max_length=600)),
                ('details', models.TextField(max_length=600)),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-published_at'],
            },
        ),
    ]
