# Generated by Django 2.1.5 on 2019-04-30 10:14

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', markdownx.models.MarkdownxField(help_text='Markdown形式で書いてください。', verbose_name='本文')),
            ],
        ),
    ]
