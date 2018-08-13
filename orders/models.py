import json

from django.conf import settings
from django.db import models

# Create your models here.
from core.models import BaseModel
from users.models import User


class Order(BaseModel):
    SUCCESSFUL = 'S'
    PENDING = 'P'
    FAILED = 'F'
    STATUS_TYPE = (
        (SUCCESSFUL, 'Successful'),
        (PENDING, 'Pending'),
        (FAILED, 'Failed'),
    )
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    json_received = models.TextField(null=True, blank=True)  # order_id, vendor_id etc
    status = models.CharField(choices=STATUS_TYPE, default=PENDING, max_length=2)
    is_fulfilled = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    @classmethod
    def create_order_schema(cls, items):
        return {
            "order": {
                "line_items": [{"variant_id": item.get('id'), "quantity": item.get('quanitiy')} for item in items]
            }
        }

    # def addItems(self, text_response):
    #     response = json.loads(text_response)
    #     if 'line_items' in response:
    #         for item in response['line_items']:
    #             OrderItem.objects.create(order=self,json_received=json.dumps(item), title="")


class OrderItem(BaseModel):  # not Used right now
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    variant_id = models.CharField(max_length=255)  # sort of cache
    json_received = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)

    def __str__(self):
        return "Item - {}".format(self.variant_id)
