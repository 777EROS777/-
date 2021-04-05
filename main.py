# def f(n):
# 	a = 0
# 	b = 1
# 	if n == 1:
# 		print(a)
# 	else:
# 		print(a)
# 		print(b)
# 		for i in range(2, n):
# 			c = a + b
# 			a = b
# 			b = c

#цикл фибоначче < 100
a = 0
b = 1
fibo = [a, b]

while b < 100:
	a, b = b, a + b
	fibo.append(b)
print(fibo)
#список четных чисел из списка фибоначче 
i = []
for item in fibo:
	if item % 2 == 0:
		i.append(item)
print(i)		
#создаем функцию вывода n - кол. четных чисел
def f(n):
	print(i[:n])

f(4)	

	  

		
		
  
		
