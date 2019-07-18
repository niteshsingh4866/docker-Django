from django.shortcuts import render
from django.core.cache import cache
from .models import Post
CACHE_TTL = 60*60*4

def index(request):
    fib=None
    n=None
    # cache=None
    db=None
    if request.method == 'POST':
        n = request.POST.get('number')
        num = int(n)
        db=Post.objects.all()
        cacheValues={}
        if db is not None:
            for rows in db:
                if rows.number in cache:
                    cacheValues[rows.number]=cache.get(rows.number)
            if num in cache:
                return render(request, 'pages/index.html', {'output':cache.get(num), 'number': num,'args': cacheValues, 'source': 'from cache'})
            for rows in db:
                if rows.number == num:
                    cache.set(rows.number, rows.result, timeout=CACHE_TTL)
                    return render(request, 'pages/index.html', {'output': rows.result, 'number': num, 'args': cacheValues, 'source': 'from DB'})
            fib = Fibonacci(int(n))
            form = Post(number=num, result=fib)
            form.save()
            db = Post.objects.all()
            source = 'by calulating'
            cache.set(num, fib, timeout=CACHE_TTL)
            return render(request, 'pages/index.html',{'output': fib, 'number': num, 'args': cacheValues, 'source': source})
        else:
            fib = Fibonacci(int(n))
            form = Post(number=num, result=fib)
            form.save()
            db=Post.objects.all()
            source = 'by calulating'
            cache.set(num, fib, timeout=CACHE_TTL)
            return render(request, 'pages/index.html', {'output': fib, 'number': n, 'args': cacheValues, 'source': source})
    else:
        return render(request, 'pages/index.html', {'output':'None','number':'None','args':'None'})


def Fibonacci(n):
    count=0
    first=0
    second=1
    fib=0
    if n < 0:
        return "Incorrect input"
        # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        while count <= n:
            fib=first+second
            first=second
            second=fib
            count=count+1
        print('fibonacci of ',n,' is ',fib)   
        return fib



