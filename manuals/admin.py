from django.contrib import admin

from .models import Manual, Tag, Step, Topic, Rating, Like, UserRate

admin.site.register(Manual)
admin.site.register(Step)
admin.site.register(Topic)
admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(Rating)
admin.site.register(UserRate)
