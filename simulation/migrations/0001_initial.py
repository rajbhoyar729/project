# Generated by Django 4.2 on 2023-05-01 14:08

from django.db import migrations, models
import simulation.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prev_h', models.CharField(blank=True, max_length=64)),
                ('merkle_h', models.CharField(blank=True, max_length=64)),
                ('h', models.CharField(blank=True, max_length=64)),
                ('nonce', models.IntegerField(null=True)),
                ('timestamp', models.FloatField(default=simulation.models.get_timestamp)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('vote', models.IntegerField(default=simulation.models.get_vote)),
                ('timestamp', models.FloatField(default=simulation.models.get_timestamp)),
                ('block_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VoteBackup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('vote', models.IntegerField(default=simulation.models.get_vote)),
                ('timestamp', models.FloatField(default=simulation.models.get_timestamp)),
                ('block_id', models.IntegerField(null=True)),
            ],
        ),
    ]