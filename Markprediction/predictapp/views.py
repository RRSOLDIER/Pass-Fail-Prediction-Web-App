from django.shortcuts import render
from .forms import StudentForm
from .mlmodel import predict_result

def home(request):
    result = None
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            marks = form.cleaned_data['marks']
            attendance = form.cleaned_data['attendance']
            study_hours = form.cleaned_data['study_hours']
            result = predict_result(marks, attendance, study_hours)
    else:
        form = StudentForm()
    return render(request, 'predict.html', {'form': form, 'result': result})

