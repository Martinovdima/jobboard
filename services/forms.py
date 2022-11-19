from django.forms import ModelForm, TextInput, FileInput

from services.models import Transcrib

class TranscribForm(ModelForm):
    class Meta:
        model = Transcrib
        fields = ['id', 'name', 'audio', 'text']

        widgets = {
            'name': TextInput(attrs={
                'id': 'name',
                'name': 'name'
            }),
            'audio': FileInput(attrs={
                'id': 'audio_file',
                'name': 'audio_file',
                'class': 'custom-file-input',
                'aria-describedby': 'audio'
            })
        }


