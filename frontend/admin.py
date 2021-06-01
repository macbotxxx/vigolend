from django.contrib import admin
from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'facebook', 'twitter')
    list_display_links = ('name', 'designation', 'facebook', 'twitter')
