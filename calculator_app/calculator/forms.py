from django import forms


class CalculatorForm(forms.Form):
    num1 = forms.DecimalField(label='Число 1')
    num2 = forms.DecimalField(label='Число 2')
    operation = forms.ChoiceField(label='Операция', choices=[
        ('+', '+'),
        ('-', '-'),
        ('*', '*'),
        (':', ':'),
    ])
