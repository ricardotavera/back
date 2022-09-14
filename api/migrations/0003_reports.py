# Generated by Django 4.1.1 on 2022-09-13 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_modalidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('hora', models.TimeField()),
                ('descripcion', models.CharField(max_length=150)),
                ('getLat', models.DecimalField(decimal_places=10, max_digits=10)),
                ('getLng', models.DecimalField(decimal_places=10, max_digits=10)),
                ('modalidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.modalidad')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
    ]
