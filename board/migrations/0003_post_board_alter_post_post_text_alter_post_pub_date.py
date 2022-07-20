# Generated by Django 4.0.6 on 2022-07-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_remove_post_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='board',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]
