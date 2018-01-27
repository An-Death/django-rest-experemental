# Generated by Django 2.0.1 on 2018-01-27 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('ref', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=200, unique=True)),
                ('users', models.ManyToManyField(related_name='words', to='django_rest.User')),
            ],
        ),
        migrations.AddField(
            model_name='vacancies',
            name='words',
            field=models.ManyToManyField(related_name='vacancies', to='django_rest.Word'),
        ),
    ]
