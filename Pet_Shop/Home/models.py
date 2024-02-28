from django.db import models
from PIL import Image


class ResizableImageField(models.ImageField):
    def save(self, *args, **kwargs):
        image = super().save(*args, **kwargs)
        img = Image.open(image.path)

        # Set the desired size (1500x600)
        desired_size = (1500, 600)

        # Resize the image to fit within the desired dimensions without distorting the aspect ratio
        img.thumbnail(desired_size, Image.ANTIALIAS)

        # Save the resized image
        img.save(image.path)


class Products(models.Model):
    # Other fields you already have
    name = models.CharField(max_length=300, null=True)
    price = models.FloatField()
    description = models.TextField()
    digital = models.BooleanField(default=True, null=True, blank=False)
    image = ResizableImageField(null=True, blank=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.CharField(max_length=100, null=True, blank=True)
    life_expectancy = models.CharField(max_length=100, null=True, blank=True)

    # Add a 'category' field to distinguish between dogs and cats
    CATEGORY_CHOICES = (
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Rabbit', 'Rabbit'),
        ('Birds', 'Birds'),
        ('Fish', 'Fish'),
        ('Accessory', 'Accessory')
        # Add more categories if needed
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,
                                default='Dog')  # Set 'Dog' as the default value

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(null=True)


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)