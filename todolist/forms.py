from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(
        max_length = 45,
        widget = forms.TextInput(
            attrs={'class': 's12 m6', 'placeholder': 'Enter a task', 'type':'text'}
        )
    )