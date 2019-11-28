# Generated by Django 2.2.4 on 2019-09-21 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('secondname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('hobbies', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('photo', models.FileField(upload_to='pics/')),
                ('text', models.CharField(max_length=20)),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appmhn.Age')),
            ],
        ),
    ]
