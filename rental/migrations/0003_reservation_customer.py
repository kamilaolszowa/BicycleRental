# Generated by Django 3.2 on 2022-01-08 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='rental.customer'),
            preserve_default=False,
        ),
    ]
