# Generated by Django 4.2.13 on 2024-07-14 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("college", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject_name", models.CharField(max_length=100)),
                ("subject_code", models.CharField(max_length=100)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subjects",
                        to="college.department",
                    ),
                ),
            ],
            options={
                "ordering": ["subject_name"],
            },
        ),
        migrations.AlterField(
            model_name="student",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="students",
                to="college.department",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="student_id",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="student",
                to="college.studentid",
            ),
        ),
        migrations.CreateModel(
            name="SubjectMark",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mark", models.IntegerField(default=0)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subject_marks",
                        to="college.student",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="marks",
                        to="college.subject",
                    ),
                ),
            ],
            options={
                "unique_together": {("student", "subject")},
            },
        ),
    ]