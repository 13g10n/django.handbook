from django.contrib import admin

from .models import Manual, Tag, Step, Topic, Rating, Like, UserRate, StepAttachment, Comment

admin.site.register(Manual)
admin.site.register(Step)
admin.site.register(Topic)
admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(Rating)
admin.site.register(UserRate)
admin.site.register(StepAttachment)
admin.site.register(Comment)
