# Generated by Django 3.0.7 on 2020-06-25 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Weblog', '0003_delete_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField()),
                ('date', models.DateTimeField()),
                ('rating', models.IntegerField()),
                ('authors', models.ManyToManyField(to='Weblog.Author')),
            ],
        ),
    ]
