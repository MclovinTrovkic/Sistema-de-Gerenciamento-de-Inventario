from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from .models import InventoryItem

class InventoryItemTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.item = InventoryItem.objects.create(name='Test Item', description='Test Description', quantity=10, user=self.user)

    def test_item_creation(self):
        self.assertEqual(self.item.name, 'Test Item')
        self.assertEqual(self.item.user.username, 'testuser')

    def test_item_list_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/')
        self.assertContains(response, 'Test Item')

