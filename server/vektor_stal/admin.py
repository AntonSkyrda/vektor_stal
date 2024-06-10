from django.contrib import admin

from .models import (
    Category,
    SubCategory,
    MetalCircleSizes,
    MetalCircle,
    MetalSheetsSizes,
    MetalSheet,
    MetalPipeSizes,
    MetalPipe
)

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(MetalCircleSizes)
admin.site.register(MetalCircle)
admin.site.register(MetalSheetsSizes)
admin.site.register(MetalSheet)
admin.site.register(MetalPipe)
