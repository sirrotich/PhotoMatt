from django.test import TestCase
from .models import Location,Image,Category

# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.nairobi= Location(first_name = 'Nairobi')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

     # Testing Save Method
    def test_save_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def delete_save_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)


class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.fashion= Category(name = 'Fashion')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.fashion,Category))

     # Testing Save Method
    def test_save_method(self):
        self.fashion.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def delete_save_method(self):
        self.fashion.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)


class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        nairobi = Location(first_name='nairobi')
        nairobi.save()
        fashion= Category(name = 'Fashion')
        fashion.save()

        self.image= Image(image = 'jpg', image_name= 'image', image_description= 'hotels', image_location= nairobi,image_category=fashion)
        self.image.save()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

     # Testing Save Method
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)


    def delete_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)


    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    def test_retrieve_all_images(self):
        images = Image.objects.all()
        self.assertTrue(len(images) ==1)

class ModalTestClass(TestCase):
    def setUp(self):
        self.image = Category(image = 'image_name')

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

     # Testing Save Method
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

