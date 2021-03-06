# Generated by Django 3.0.4 on 2020-03-19 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_name', models.CharField(max_length=50)),
                ('comment_text', models.CharField(max_length=200)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Players')),
            ],
        ),
    ]
