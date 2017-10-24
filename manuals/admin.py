from django.contrib import admin

from .models import Manual, Tag, Step, Topic

admin.site.register(Manual)
admin.site.register(Step)
admin.site.register(Topic)
admin.site.register(Tag)
