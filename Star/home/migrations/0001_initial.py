# Generated by Django 4.1.7 on 2023-04-24 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('podcastname', models.CharField(max_length=200)),
                ('podcast_des', models.TextField(max_length=200)),
                ('podcast_speaker', models.TextField(max_length=200)),
                ('podcast_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='audio_pod/')),
                ('file1', models.FileField(upload_to='uploads/')),
                ('file2', models.FileField(upload_to='video_pod')),
            ],
        ),
        migrations.CreateModel(
            name='UserLikedAudio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('audio', models.CharField(default='', max_length=10000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
