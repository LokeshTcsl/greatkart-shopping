# Generated by Django 4.2.1 on 2023-05-28 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0017_alter_variation_variation_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reviewrating", old_name="updated_date", new_name="updated_at",
        ),
        migrations.AlterField(
            model_name="reviewrating",
            name="ip",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name="variation",
            name="variation_category",
            field=models.CharField(
                choices=[("color", "color"), ("size", "size")], max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="variation",
            name="variation_value",
            field=models.CharField(max_length=100),
        ),
    ]
