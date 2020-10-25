from django.db import models


class Services(models.Model):

    service_name = models.CharField(max_length=200)
    service_discription = models.CharField(max_length=300)
    date = models.DateTimeField(auto_created=True,auto_now_add=True)
    contact_email = models.CharField(max_length=200)
    service_provider_id = models.CharField(max_length=200)

    def __str__(self):
        return self.service_name
