from django.db import models
from django.conf import settings


class ItemCategory(models.Model):
    category_name = models.CharField(max_length=100)    # Category choices?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


def get_default_item_category():
    return ItemCategory.objects.get_or_create(name="Other")[0]


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(blank=True)
    category = models.ForeignKey(
        ItemCategory,
        related_name='item_category',
        on_delete=models.SET(get_default_item_category))
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name


class Order(models.Model):
    IN_PROGRESS = 'P'
    DONE = 'D'
    STATUS_CHOICES = [
        (IN_PROGRESS, 'in_progress'),
        (DONE, 'done'),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICES,
                              default=DONE)
    created_at = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return f'{self.owner.username},  {self.status}'


class OrderItem(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item.item_name

