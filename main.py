
first_number = int(input())
second_number = first_number + 1
third_number = first_number + 2
print (first_number)
print (second_number)
print (third_number)

a = int(input())
b = int(input())
c = int(input())

sum = a + b + c

print(sum)

длина_ребра = int(input())
Обьем= длина_ребра ** 3
Площадь_поверхности = 6 * (длина_ребра ** 2)
print("Обьем куба:", Обьем)
print(Площадь_поверхности)

a = int(input ())
b = int(input())
f = 3*(a + b)**3 + 275*b**2 -127*a - 41
print (f)

a = int(input())
f = a+1
n = a-1
print(f"Следущее за числом {a} число: {f}")
print(f"Предыдущее для числа {a} число:{n}")

a = int(input ("Стоимость монитора: "))
b = int(input ("Стоимость системного блока: "))
c = int(input ("Стоимость клавиатур: "))
d = int(input ("Стоимость мыши: "))
sum = int(a+b+c+d)*3
print ("Стоимость трех компьютеров =", sum)

a_1 = int(input())
d = int(input())
n = int(input())
a_n = a_1 + d*(n-1)
print ("Алг. прог.: ", a_n)

x1 = int(input("Введите число: "))
x2 = x1 * 2
x3 = x2 + x1
x4 = x3 + x1
x5 = x4 + x1
print(x1,x2,x3,x4,x5, sep='---')

n = int(input("Кол. школьников: "))
k = int(input("Мандаринки: "))
half = n // k
bask = n % k
print (half)
print (bask)

a=int(input())
print(a//2 + a%2)

m = int(input("Введите число: "))
h = m // 60
s = m % 60
print(m, "мин. это - ", h, "час", s, "минут.")

num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100
print("Сумма чисел =", c + b + a)
print("Произведение чисел =", c * b * a)

n = input()
print('    _~_    ' *int(n))
print('   (o o)   ' *int(n))
print('  /  V  \  ' *int(n))
print(' /(  _  )\ ' *int(n))
print('   ^^ ^^   ' *int(n))

abc = int(input())
x = 1
n = (x // 10 ** k) % 10
print(n)

a = int(input())
h = a % (60 * 24) // 60
m = a % 60
print(h, m)

a = int(input())
print(1 - a)

a = int(input())
print((a//2+1)*2)

v = int(input())
t = int(input())
a = v * t
n = a // 109
print(-(109 * n - a))

a = float(input("1: "))
b = float(input("2: "))
c = float(input("3: "))
print(int(1 + (a - c - 1) / (b - c)))

