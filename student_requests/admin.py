from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.snippets.models import register_snippet
from .models import Evaluation
from django.contrib import messages

class EvaluationViewSet(SnippetViewSet):
    model = Evaluation
    menu_label = 'Evaluations'
    menu_icon = 'user'
    list_display = ['student', 'trainer', 'status', 'assigned_level', 'notes']
    list_filter = ['status']
    search_fields = ['student__name', 'trainer__name']
    actions = ['mark_as_completed', 'mark_as_cancelled']

    def mark_as_completed(self, request, queryset):
        updated = queryset.filter(status=Evaluation.Status.PENDING).update(status=Evaluation.Status.COMPLETED)
        self.message_user(request, f"{updated} request(s) marked as completed.")
    mark_as_completed.short_description = "Mark selected requests as completed"

    def mark_as_cancelled(self, request, queryset):
        updated = queryset.filter(status=Evaluation.Status.PENDING).update(status=Evaluation.Status.CANCELLED)
        self.message_user(request, f"{updated} request(s) marked as cancelled.")
    mark_as_cancelled.short_description = "Mark selected requests as cancelled"

register_snippet(EvaluationViewSet)