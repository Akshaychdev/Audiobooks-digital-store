# Generated by Django 3.1.2 on 2020-11-20 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('price', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('file', models.FileField(null=True, upload_to='uploads/files')),
                ('thumbnail', models.ImageField(upload_to='uploads/thumbnails')),
                ('link', models.CharField(max_length=500, null=True)),
                ('fileSize', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='uploads/image')),
                ('book', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bookshop.book')),
            ],
        ),
    ]
