# Generated by Django 4.0.8 on 2023-03-23 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stammdaten', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kunden',
            fields=[
                ('kundeid', models.AutoField(primary_key=True, serialize=False)),
                ('titel', models.CharField(blank=True, max_length=155, null=True)),
                ('name', models.CharField(blank=True, max_length=755, null=True)),
                ('vorname', models.CharField(blank=True, max_length=255, null=True)),
                ('nachname', models.CharField(blank=True, max_length=255, null=True)),
                ('geburtsdatum', models.DateField(blank=True, null=True)),
                ('kdkdnr', models.CharField(blank=True, max_length=155, null=True)),
                ('strasse', models.CharField(blank=True, max_length=755, null=True)),
                ('plz', models.CharField(blank=True, max_length=25, null=True)),
                ('ort', models.CharField(blank=True, max_length=155, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('telefon', models.CharField(blank=True, max_length=255, null=True)),
                ('telefon_mobil', models.CharField(blank=True, max_length=255, null=True)),
                ('dsgvo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stammdaten.dsgvo')),
                ('herkunft', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stammdaten.herkunft')),
                ('mandant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stammdaten.mandant')),
            ],
            options={
                'verbose_name': 'Kunde',
                'verbose_name_plural': 'Kunden',
                'db_table': 'kuKunden',
            },
        ),
        migrations.CreateModel(
            name='Kommunikation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kommunikationswert', models.CharField(blank=True, max_length=755, null=True)),
                ('kommunikationsart', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stammdaten.kommunikationsart')),
                ('kundeid', models.ForeignKey(db_column='kundeid', on_delete=django.db.models.deletion.CASCADE, related_name='kommunikation', to='cdr.kunden')),
            ],
            options={
                'verbose_name': 'Kommunikation',
                'verbose_name_plural': 'Kommunikation',
                'db_table': 'kuKommunikation',
            },
        ),
    ]
