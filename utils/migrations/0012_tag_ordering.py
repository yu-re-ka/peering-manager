# Generated by Django 3.2.9 on 2021-12-03 23:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("utils", "0011_auto_20210721_1428")]

    operations = [
        migrations.AlterModelOptions(name="tag", options={"ordering": ["name"]}),
    ]