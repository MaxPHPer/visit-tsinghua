# Generated by Django 3.2.3 on 2021-06-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('level', models.IntegerField(default=1)),
                ('createTime', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'TestUser',
            },
        ),
    ]
