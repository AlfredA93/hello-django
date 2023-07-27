"Libraries"
from django.test import TestCase
from .models import Item

# Create your tests here.

class TestModels(TestCase):
    "Model Test"

    def test_done_faults_to_false(self):
        "done by default"
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)
