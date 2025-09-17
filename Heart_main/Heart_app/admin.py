from django.contrib import admin
from .models import PredictionHistory

@admin.register(PredictionHistory)
class PredictionHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'prediction')
    list_filter = ('date', 'prediction')
    search_fields = ('user__username', 'prediction')
    ordering = ('-date',)
