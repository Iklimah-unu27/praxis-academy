def fib(n):    
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
#output

#Input and Output
u = 'hee'
print (u)
repr(u)
str(1/7)
'0.14285714285714285'
x = 10 * 3.25
y = 200 * 200
u = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print('u')

#contoh string
tumbuhan = 'anggrek'
print(f'aku sangat suka {tumbuhan}')

#con metode string format ()
print('kita sangat {} dia sanaget"{}!"'.format('rajin', 'pandai'))

print('cerintanya si {0}, {1}, and {other}.'.format('ina', 'ini', other='itu'))

