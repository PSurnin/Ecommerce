from django.test import TestCase

from .models import Item, ItemCategory


class ItemCategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.item_category = ItemCategory.objects.create(
            category_name='Furniture',
        )

    def test_model_content(self):
        self.assertEqual(self.item_category.category_name, 'Furniture')
        self.assertEqual(str(self.item_category), 'Furniture')


class ItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.item_category = ItemCategory.objects.create(
            category_name='Furniture',
        )

        cls.item = Item.objects.create(
            item_name='Bed',
            description='Nice bed',
            category_id_id=1,
            price=250,
            quantity=10
        )


    def test_model_content(self):
        self.assertEqual(self.item.item_name, 'Bed')
        self.assertEqual(self.item.description, 'Nice bed')
        self.assertEqual(self.item.price, 250)
        self.assertEqual(self.item.quantity, 10)
        self.assertEqual(str(self.item), 'Bed')
