from unittest.mock import patch
import pytest
from django.forms import ValidationError
from django.core.files.base import ContentFile
from mailinglist.admin_forms import SubmissionModelForm


class TestSubmissionModelForm:
    def test_init_new(self, message):
        form = SubmissionModelForm()
        assert list(form.fields["message"].queryset) == [message]

    def test_init_no_messages(self, message, submission):
        form = SubmissionModelForm()
        assert list(form.fields["message"].queryset) == []

    def test_init_with_submission(self, message, submission, subscription):
        form = SubmissionModelForm(instance=submission)
        assert list(form.fields["message"].queryset) == [message]
        assert list(form.fields["exclude"].queryset) == [subscription]
