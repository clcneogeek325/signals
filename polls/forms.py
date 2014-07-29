from django import forms
from polls.models import Poll

class PollForm(forms.ModelForm):
	class Meta:
		model = Poll
