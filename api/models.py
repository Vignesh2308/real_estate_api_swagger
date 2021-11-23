from django.db import models

# Create your models here.
class Agent(models.Model):
    agent_id = models.AutoField(primary_key=True)
    agent_email = models.EmailField(max_length=254)
    agent_contact = models.IntegerField()
    agent_name = models.CharField(max_length=255)
    customer_id = models.IntegerField()

    def __str__(self):
        return self.first_name