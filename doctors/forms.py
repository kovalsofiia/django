from django import forms

from doctors.models import Doctor


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ["full_name", "specialization", "experience_years"]

    def clean_experience_years(self):
        experience_years = self.cleaned_data["experience_years"]
        if experience_years > 60:
            raise forms.ValidationError("Стаж не може перевищувати 60 років.")
        return experience_years

