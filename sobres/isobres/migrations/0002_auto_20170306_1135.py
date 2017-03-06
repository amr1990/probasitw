# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('isobres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('twitter', models.TextField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='sobre',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sobre',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sobre',
            name='donor',
            field=models.ForeignKey(default=1, to='isobres.Donor'),
            preserve_default=False,
        ),
    ]
