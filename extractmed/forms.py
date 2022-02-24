from django import forms

class MedicineDetailsFrom(forms.Form):
    text = forms.CharField(widget=forms.Textarea)