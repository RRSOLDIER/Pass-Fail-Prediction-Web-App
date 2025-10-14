from django import forms

class StudentForm(forms.Form):
    marks = forms.IntegerField(label='Marks (0–100)', min_value=0, max_value=100)
    attendance = forms.IntegerField(label='Attendance (%)', min_value=0, max_value=100)
    study_hours = forms.FloatField(label='Study Hours per Day', min_value=0)
