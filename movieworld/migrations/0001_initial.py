# Generated by Django 3.0.3 on 2020-02-11 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_name', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('birthday', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no name', max_length=100)),
                ('genre', models.CharField(default='no genre', max_length=100)),
                ('release_date', models.CharField(max_length=200, null=True)),
                ('director_name', models.CharField(max_length=200, null=True)),
                ('stars', models.CharField(max_length=200, null=True)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to='movieworld.Director')),
            ],
        ),
    ]
