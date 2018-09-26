# Generated by Django 2.1 on 2018-09-16 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='focus.Comment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]