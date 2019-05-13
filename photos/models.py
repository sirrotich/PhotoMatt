from django.db import models

# Create your models here.
class Location(models.Model):
    first_name = models.CharField(max_length =25)

    def __str__(self):
        return self.first_name

    def save_location(self):
        self.save()

    class Meta:
        ordering = ['first_name']

class Category(models.Model):
    name = models.CharField(max_length =25)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to ='gallery/')
    image_name = models.CharField(max_length =20)
    image_description = models.TextField(max_length =400)
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    class Meta:
        ordering = ['image_name']

    @classmethod
    def get_image_by_id(cls):
        images = cls.objects.get(pk=id)
        return images
    @classmethod
    def retrive_all_images(cls):
        images = Image.objects.all()
        return images
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(image__icontains=search_term)
        return images