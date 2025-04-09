from django.contrib import admin

from .models import Album, Artist, Track

# Register disks models
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Track)
