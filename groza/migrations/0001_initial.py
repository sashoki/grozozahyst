# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-07-12 13:22
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='groza.Category', verbose_name='\u0420\u041e\u0414\u0418\u0422\u0415\u041b\u042c\u0421\u041a\u0418\u0419 \u043a\u043b\u0430\u0441\u0441')),
            ],
            options={
                'ordering': ('tree_id', 'level'),
                'db_table': 'category',
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u0457',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_title', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u043e\u0431\u0454\u043a\u0442\u0443')),
                ('port_img', models.ImageField(upload_to='portfolio/', verbose_name='\u0417\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f')),
                ('port_text', ckeditor.fields.RichTextField()),
                ('port_video', embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='\u0412\u0456\u0434\u0435\u043e')),
                ('port_data', models.DateTimeField()),
                ('port_client', models.CharField(max_length=200, verbose_name='\u0406\u043c\u044f \u043a\u043b\u0456\u0454\u043d\u0442\u0430')),
                ('category', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='groza.Category')),
            ],
            options={
                'ordering': ['-port_data'],
                'db_table': 'Portfolio',
                'verbose_name': '\u041f\u043e\u0440\u0442\u0444\u043e\u043b\u0456\u043e',
                'verbose_name_plural': '\u041f\u043e\u0440\u0442\u0444\u043e\u043b\u0456\u043e',
            },
        ),
    ]
