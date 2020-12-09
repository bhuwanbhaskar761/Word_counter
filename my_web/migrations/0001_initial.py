# Generated by Django 3.1.4 on 2020-12-08 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url1', models.CharField(max_length=500, null=True)),
                ('page', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Scrapped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('frequency', models.CharField(max_length=100)),
                ('weburl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_web.weburl')),
            ],
        ),
    ]
