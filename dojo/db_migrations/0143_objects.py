# Generated by Django 3.2.9 on 2021-12-14 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0142_environment_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='system_settings',
            name='enable_product_tracking_files',
            field=models.BooleanField(default=True, help_text='With this setting turned off, the product tracking files will be disabled in the user interface.', verbose_name='Enable Product Tracking Files'),
        ),
        migrations.DeleteModel(
            name='Objects_Engagement',
        ),
    ]