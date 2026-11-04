from django.contrib import admin
from .models import Event, News, Opportunity, Project

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "is_published")
    list_filter = ("is_published", "published_at")
    search_fields = ("title", "summary", "body")
    list_editable = ("is_published",)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "starts_at", "location", "status")
    list_filter = ("status", "starts_at")
    search_fields = ("title", "location", "description")

@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "deadline", "is_published")
    list_filter = ("category", "is_published")
    search_fields = ("title", "description")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "is_published")
    list_filter = ("status", "is_published")
    search_fields = ("title", "summary", "description")
