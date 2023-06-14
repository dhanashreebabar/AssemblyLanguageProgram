from django.db import models

class AssemblyProgram(models.Model):
    program_id = models.IntegerField()
    program_text = models.TextField()
    success = models.BooleanField(default=False)
    result = models.IntegerField(null=True, blank=True)