# Generated migration for adding humidity field to Temperature model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperature',
            name='humidity',
            field=models.FloatField(blank=True, null=True, verbose_name='Humidity (%)'),
        ),
    ]