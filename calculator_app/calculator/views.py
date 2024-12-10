from django.shortcuts import render
from .forms import CalculatorForm


def calculator(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            operation = form.cleaned_data['operation']

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == ':':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = 'Ошибка: деление на ноль'
            else:
                result = 'Ошибка: неизвестная операция'

            return render(request, 'calculator/result.html', {'result': result})
    else:
        form = CalculatorForm()

    return render(request, 'calculator/form.html', {'form': form})
