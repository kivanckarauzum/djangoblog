# Generated by Django 3.0.6 on 2020-06-16 19:09

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200613_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=20, verbose_name='yazar')),
                ('comment_content', ckeditor.fields.RichTextField()),
                ('comment_created_date', models.DateTimeField(auto_now_add=True, verbose_name='eklenme tarihi')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article', verbose_name='makale')),
            ],
        ),
    ]
