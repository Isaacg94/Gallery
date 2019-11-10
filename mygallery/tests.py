from django.test import TestCase
from .models import Editor,Category,Location,Image

# Create your tests here.
class EditorTestCase(TestCase):

    #Set up method
    def setUp(self):
        self.isaac= Editor(editor_name = 'Isaac', email = '7248zack@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.isaac,Editor))