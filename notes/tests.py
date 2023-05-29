from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import Note


# Model work Confirmation
class NoteModelTest(TestCase):
    def test_note_creation(self):
        note = Note.objects.create(title="Test Note", note="This is a test note")
        now = timezone.now()

        self.assertEqual(note.title, "Test Note")
        self.assertEqual(note.note, "This is a test note")
        self.assertAlmostEqual(note.pub_date, now, delta=timedelta(seconds=1))
        self.assertAlmostEqual(note.last_modified, now, delta=timedelta(seconds=1))

# was_published_recently() function Confirmation
class WasPublishedTest(TestCase):
    def test_was_published_recently_with_recent_note(self):
        now = timezone.now()
        recent_note = Note(pub_date=now)
        self.assertIs(recent_note.was_published_recently(), True)

    def test_was_published_recently_with_old_note(self):
        old_date = timezone.now() - timedelta(days=2)
        old_note = Note(pub_date=old_date)
        self.assertIs(old_note.was_published_recently(), False)

# last_modified Confirmation
class LastModifiedTest(TestCase):
    def test_last_modified_auto_update(self):
        note = Note.objects.create(title="Test Note", note="This is a test note")
        initial_last_modified = note.last_modified

        # Wait for a second to ensure the last_modified field is updated
        import time
        time.sleep(1)

        note.note = "Updated note"
        note.save()
        updated_last_modified = note.last_modified

        self.assertNotEqual(initial_last_modified, updated_last_modified)