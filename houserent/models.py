from django.db import models

# Create your models here.
class City(models.Model):
    name= models.TextField(null = True)
   
    def __str__(self):
        return self.name

class Houses(models.Model):
    name = models.TextField()
    address = models.TextField()
    amt = models.TextField()
    image_url = models.TextField(default='https://wp-tid.zillowstatic.com/7/buy-vs-rent-215f3b.jpg')
    description = models.TextField(default='Beautifull home')
    city = models.ForeignKey(City , on_delete=models.CASCADE, related_name='houses')


    def __str__(self):
        return self.name