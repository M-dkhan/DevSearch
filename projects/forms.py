from django.forms import ModelForm
from .models import Projects

class AddProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags']

        labels = {
            'title':'Title',
            'description':'Description',
            'demo_link':'Demo Link',
            'source_link':'Source Link',
            'Tags':'Tags'
        }
