from django.db import models

class Document(models.Model):

    label = models.TextField()
    title = models.TextField()
    file = models.FileField(upload_to='uploads/')
    DOCUMENT_TYPE_CHOICES = [
        ('org_doc', 'Документ организации'), 
        ('org_activity', 'Деятельность организации'), 
        ('template', 'Шаблоны документов') 
    ]
    type = models.CharField(max_length=100, choices=DOCUMENT_TYPE_CHOICES)

