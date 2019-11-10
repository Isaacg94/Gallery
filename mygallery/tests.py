from django.test import TestCase
from .models import Editor,Category,Location,Image

# Create your tests here.
class EditorTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.isaac= Editor(editor_name = 'Isaac', email = '7248zack@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.isaac,Editor))

     # Testing Save Method
    def test_save_method(self):
        self.isaac.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)


class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(editor_name = 'James', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new category and saving it
        self.new_category = Category(name = 'Travel')
        self.new_category.save()

        # Creating a new location and saving it
        self.new_location = Location(name = 'Nairobi')
        self.new_location.save()

        self.new_image= Image(img_name = 'testimage',img_description = 'This is a random test image',editor = self.james, category = self.new_category, location = self.new_location)
        self.new_image.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def tearDown(self):
        Editor.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()
