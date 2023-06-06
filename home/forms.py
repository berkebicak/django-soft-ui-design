from django import forms


class GeneralForm(forms.Form):
    text = forms.CharField(max_length=512, label="Text", widget=forms.Textarea)

    def clean(self):
        text = self.cleaned_data.get("text")
        values = {
            "text": text,
        }
        return values
