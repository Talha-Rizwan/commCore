from django.db import models
from users.models import Student, Instructor
from utils.constants import Levels

class Evaluation(models.Model):
    class Status(models.TextChoices):
        PENDING = 'Pending'
        COMPLETED = 'Completed'
        CANCELLED = 'Cancelled'

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    assigned_level = models.CharField(
        max_length=20,
        choices=Levels,
        default=None,
        null=True,
        blank=True,
    )
    evaluation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        student_name = self.student.user.get_full_name() or self.student.user.username
        level = self.assigned_level if self.assigned_level else "Pending"
        return f"Evaluation for {student_name} - {level}"
