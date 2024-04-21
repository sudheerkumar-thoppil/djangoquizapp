from django.contrib import admin
from .import models
admin.site.register(models.QuizCategory)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display=['question','level']
admin.site.register(models.QuizQuestions)


# Register your models here.
