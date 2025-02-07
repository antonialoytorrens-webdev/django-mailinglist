from django import forms
from django.db.models import Q

from mailinglist.models import MailingList, Message, Submission


class SubmissionModelForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        submission = kwargs.get("instance")
        if submission is not None:
            self.fields[
                "exclude"
            ].queryset = submission.message.mailing_list.subscriptions.all()
            self.fields["message"].queryset = Message.objects.filter(
                Q(submission__isnull=True) | Q(submission=submission)
            )
        else:
            self.fields["message"].queryset = Message.objects.filter(
                submission__isnull=True
            )
