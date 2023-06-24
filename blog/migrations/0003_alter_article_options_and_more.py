# Generated by Django 4.2.1 on 2023-06-24 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published']},
        ),
        migrations.RemoveIndex(
            model_name='article',
            name='blog_articl_publish_308f23_idx',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='published_at',
            new_name='published',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='updated_at',
            new_name='updated',
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['-published'], name='blog_articl_publish_f03bae_idx'),
        ),
    ]
