# Generated by Django 4.2.6 on 2023-10-19 14:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('race', models.CharField(max_length=256)),
                ('birthday', models.DateField()),
            ],
        ),
    ]