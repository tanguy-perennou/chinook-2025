from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(
        label="With album title or artist/track name containing:",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "..."}),
    )
