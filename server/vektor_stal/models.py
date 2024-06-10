from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return f"{self.name}"


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    steel_mark = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images", null=True, blank=True)


class MetalCircleSizes(models.Model):
    size = models.IntegerField()

    class Meta:
        ordering = ('size',)
        verbose_name_plural = 'metal circle sizes'

    def __str__(self):
        return f"{self.size}"
    

class MetalCircle(Product):
    sizes = models.ManyToManyField(MetalCircleSizes, related_name="metal_circles")

    class Meta:
        ordering = ("steel_mark", )

    def __str__(self):
        return f"{self.name}"


class MetalSheetsSizes(models.Model):
    size = models.IntegerField()

    class Meta:
        ordering = ("size", )
        verbose_name_plural = 'metal sheets sizes'

    def __str__(self):
        return f"{self.size}"


class MetalSheet(Product):
    sizes = models.ManyToManyField(MetalSheetsSizes, related_name="metal_sheets")

    class Meta:
        ordering = ("steel_mark", )

    def __str__(self):
        return f"{self.name}"


class MetalPipeSizes(models.Model):
    size = models.IntegerField()

    class Meta:
        ordering = ("size", )
        verbose_name_plural = 'metal pipes sizes'

    def __str__(self):
        return f"{self.size}"


class MetalPipe(Product):
    sizes = models.ManyToManyField(MetalPipeSizes, related_name="metal_pipes")

    class Meta:
        ordering = ("steel_mark", )

    def __str__(self):
        return f"{self.name}"
