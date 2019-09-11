from django.shortcuts import render
from .models import Fib
import time

def fib_cal(num):
    if num < 2:
        return 1
    else:
        num_seq_1 = 1
        num_seq_2 = 1
        for i in range(2, num):
            temp = num_seq_1 + num_seq_2
            num_seq_1 = num_seq_2
            num_seq_2 = temp
        return num_seq_2

def fib_number(request):
    num = 0
    result = 0
    time_taken = 0

    if request.GET.get('number'):
        start_time = time.time()
        number = request.GET.get('number')
        num = int(number)
        result = fib_cal(num)
        end_time = time.time() - start_time
        time_taken = str(end_time)[0:4]

        obj = Fib.objects.create(
            number=num, result=result, time_taken=time_taken)
        obj.save()        

    return render(request, 'app/Fib_list.html', {'number': num, 'result': result, 'time_taken': time_taken,})