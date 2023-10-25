from django.contrib import admin
from .models import Question, Event, Response, EventResponse, Profile, QuestionImage
# Register your models here.

admin.site.register(Question)
admin.site.register(Event)
admin.site.register(Response)
admin.site.register(EventResponse)
admin.site.register(Profile)
admin.site.register(QuestionImage)
