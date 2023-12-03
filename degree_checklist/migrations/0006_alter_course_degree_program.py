# Generated by Django 4.2.7 on 2023-11-26 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("degree_checklist", "0005_alter_course_degree_program"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="degree_program",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="courses",
                to="degree_checklist.degreeprogram",
            ),
        ),
    ]