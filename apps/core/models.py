from django.db import models


class AuditModel(models.Model):
    owner = models.CharField("Creado por:", max_length=100, blank=True, null=True)
    update_by = models.CharField("Actualizado por:", max_length=100, blank=True, null=True)
    created_at = models.DateTimeField("Creación del Registro:", auto_now_add=True)
    updated_at = models.DateTimeField("Modificación del Registro:", auto_now=True)

    class Meta:
        abstract = True
