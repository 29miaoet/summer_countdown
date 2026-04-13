#!/usr/bin/env python3
import matplotlib.pyplot as plt

max_value=10
a=1
b=1
x_values=[1,2]
y_values=[1,1]
for i in range(max_value):
    fib = a + b
    print(fib)
    a,b=b,fib
    x_values.append(i+3)
    y_values.append(fib)
    
plt.bar(x_values,y_values)
plt.show()