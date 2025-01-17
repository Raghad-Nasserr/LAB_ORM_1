# Generated by Django 4.1.6 on 2023-02-05 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=2000)),
                ('Content', models.TextField()),
                ('is_published', models.BooleanField()),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
