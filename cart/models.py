from django.db import models
from courses.models import Course
from django.conf import settings


class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    session_key = models.CharField(
        max_length=40, blank=True, null=True
    )

    def __str__(self):
        if self.user:
            return f"Cart (User: {self.user.email})"
        return f"Cart (Session: {self.session_key})"

    def get_total_price(self):
        return sum(item.course.price for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
