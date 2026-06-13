from django.utils import timezone
from users.models import Note, ActivityLog


def get_notes(user):
    return Note.objects.filter(user=user, deleted_at__isnull=True)


def get_deleted_notes(user):
    return Note.objects.filter(user=user, deleted_at__isnull=False)


def get_note_by_id(pk, user):
    try:
        return Note.objects.get(pk=pk, user=user, deleted_at__isnull=True)
    except Note.DoesNotExist:
        return None


def get_deleted_note_by_id(pk, user):
    try:
        return Note.objects.get(pk=pk, user=user, deleted_at__isnull=False)
    except Note.DoesNotExist:
        return None


def create_note(user, serializer):
    note = serializer.save(user=user)
    ActivityLog.objects.create(user=user, action='created', note_title=note.title)
    return note


def update_note(note, serializer):
    was_done = note.done
    updated = serializer.save()
    if updated.done != was_done:
        action = 'completed' if updated.done else 'uncompleted'
    else:
        action = 'updated'
    ActivityLog.objects.create(user=note.user, action=action, note_title=updated.title)
    return updated


def delete_note(note):
    note.deleted_at = timezone.now()
    note.save()
    ActivityLog.objects.create(user=note.user, action='deleted', note_title=note.title)


def restore_note(note):
    note.deleted_at = None
    note.save()
    ActivityLog.objects.create(user=note.user, action='restored', note_title=note.title)
