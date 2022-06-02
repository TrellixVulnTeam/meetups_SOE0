# Generated by Django 3.2.8 on 2022-06-02 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0008_auto_20220602_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default='2021-02-02'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(default='test.com', max_length=254),
            preserve_default=False,
        ),
    ]
