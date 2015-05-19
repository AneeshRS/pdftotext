from django.db import models

class PdfText(models.Model):
    pdf = models.FileField(upload_to="pdftotext/pdf")
    text = models.FileField(upload_to="pdftotext/text", blank=True, null=True)

    def __unicode__(self):
        return self.image.url
