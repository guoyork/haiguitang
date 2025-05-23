# Generated by Django 4.2.21 on 2025-05-15 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user_inputs", "0005_delete_userinput"),
    ]

    operations = [
        migrations.AddField(
            model_name="rating",
            name="question",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="user_inputs.questions",
            ),
        ),
        migrations.AlterField(
            model_name="questions",
            name="title",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
