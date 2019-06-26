# Generated by Django 2.1.7 on 2019-05-01 00:05

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
            name='Dialog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textLastMessage', models.TextField()),
                ('dateLastMessage', models.DateTimeField()),
                ('idLastMessage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DialogOwners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dialog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owners', to='api.Dialog')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dialogsID', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL)),
                ('ownerDialog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='api.Dialog')),
            ],
        ),
    ]