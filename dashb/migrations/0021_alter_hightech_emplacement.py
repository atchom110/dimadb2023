# Generated by Django 4.2 on 2023-06-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashb', '0020_laptop_sortie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hightech',
            name='emplacement',
            field=models.CharField(choices=[('SALLE SPORT', 'SALLE SPORT'), ('SALLE SERVEUR', 'SALLE SERVEUR'), ('CENTRE TRANSIT', 'CENTRE TRANSIT'), ('CARTON DIMA', 'CARTON DIMA'), ('SAC KAKI', 'SAC KAKI'), ('MINAWAO', 'MINAWAO'), ('COFFRE BABA', 'COFFRE BABA'), ('KOUSSERI', 'KOUSSERI'), ('CARTON NEUF', 'CARTON NEUF'), ('AIRD', 'AIRD')], max_length=25),
        ),
    ]