# Generated by Django 4.2.7 on 2024-06-24 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("model_provider_mgmt", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="embedprovider",
            name="embed_model_type",
            field=models.CharField(choices=[("lang-serve", "LangServe")], max_length=255, verbose_name="嵌入模型"),
        ),
    ]