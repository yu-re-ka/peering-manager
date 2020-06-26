# Generated by Django 3.0.7 on 2020-06-26 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Webhook",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, unique=True)),
                (
                    "type_create",
                    models.BooleanField(
                        default=False,
                        help_text="Call this webhook when an object is created.",
                    ),
                ),
                (
                    "type_update",
                    models.BooleanField(
                        default=False,
                        help_text="Call this webhook when an object is updated.",
                    ),
                ),
                (
                    "type_delete",
                    models.BooleanField(
                        default=False,
                        help_text="Call this webhook when an object is deleted.",
                    ),
                ),
                (
                    "url",
                    models.CharField(
                        help_text="A POST will be sent to this URL when the webhook is called.",
                        max_length=512,
                        verbose_name="URL",
                    ),
                ),
                ("enabled", models.BooleanField(default=True)),
                (
                    "http_method",
                    models.CharField(
                        choices=[
                            ("GET", "GET"),
                            ("POST", "POST"),
                            ("PUT", "PUT"),
                            ("PATCH", "PATCH"),
                            ("DELETE", "DELETE"),
                        ],
                        default="POST",
                        max_length=32,
                        verbose_name="HTTP method",
                    ),
                ),
                (
                    "http_content_type",
                    models.CharField(
                        default="application/json",
                        help_text='The complete list of official content types is available <a href="https://www.iana.org/assignments/media-types/media-types.xhtml">here</a>.',
                        max_length=128,
                        verbose_name="HTTP content type",
                    ),
                ),
                (
                    "secret",
                    models.CharField(
                        blank=True,
                        help_text="When provided, the request will include a 'X-Hook-Signature' header containing a HMAC hex digest of the payload body using the secret as the key. The secret is not transmitted in the request.",
                        max_length=255,
                    ),
                ),
                (
                    "ssl_verification",
                    models.BooleanField(
                        default=True,
                        help_text="Enable SSL certificate verification. Disable with caution!",
                        verbose_name="SSL verification",
                    ),
                ),
                (
                    "ca_file_path",
                    models.CharField(
                        blank=True,
                        help_text="CA certificate file to use for SSL verification. Leave blank to use the system defaults.",
                        max_length=4096,
                        null=True,
                        verbose_name="CA File Path",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "unique_together": {
                    ("type_create", "type_update", "type_delete", "url")
                },
            },
        )
    ]
