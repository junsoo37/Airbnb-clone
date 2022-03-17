from django.contrib import admin
from conversations import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    pass
