# Generated by Django 4.2.3 on 2023-07-28 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0006_alter_sitesetup_favicon'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetup',
            name='footer_link',
            field=models.CharField(default=None, max_length=2048, null=True),
        ),
    ]
