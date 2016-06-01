from django.db import models

class Category(models.Model):

  title = models.CharField(max_length=200)
  description = models.TextField()
  pub_date = modelDateTimeField('date published')

  def __str__(self):
    return self.title

class Product(models.Model):
  category = models.ForeignKey(Category)
  title = models.CharField(max_length=200)
  description = models.TextField()
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.title