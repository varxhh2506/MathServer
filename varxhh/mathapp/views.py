from django.shortcuts import render

def churn_rate(request):
    i = 0
    l = 0
    churnrate = 0

    if request.method == 'POST':
        i = int(request.POST.get('initial', 0))
        l = int(request.POST.get('lost', 0))

        if i > 0:
            churnrate = (l / i) * 100
    print("i:", i)    
    print("l:" ,l)    
    print("churnrate:",churnrate)
    return render(request, 'mathapp/math.html', {
        'i': i,
        'l': l,
        'churnrate': churnrate
    })
