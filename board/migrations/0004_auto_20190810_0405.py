# Generated by Django 2.2.4 on 2019-08-09 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('공지', '공지'), ('정치', '정치'), ('사회', '사회'), ('경제', '경제'), ('IT', 'IT'), ('과학', '과학')], default='공지', max_length=20),
        ),
    ]