'''greater = lambda a,b: a if a>b else b
print(greater(13,16))
print(greater(60,46))
print(greater(34,27))
print(greater(50,30))
wish = lambda name: f'Welcome to the course {name}'
print(wish("Ganesh"))
print(wish("Viswa"))
print(wish("Cherry"))
iseven = lambda n: "Even" if n%2==0 else "Odd"
print(iseven(67))
print(iseven(80))
print(iseven(78))
avg = lambda a,b,c: (a+b+c)/3
print(avg(4,5,6))
print(avg(45,68,17))'''



'''domain = lambda mail: (mail.split('@')[-1]).split('.')[0]
print(domain('viswa@gmail.com'))
print(domain('viswa@codegnan.com'))
print(domain('viswa@outlook.com'))
print(domain('viswa@yahoo.com'))'''



'''gst = lambda price : price + price*0.18
print(gst(1000))
print(gst(8000))
print(gst(6000))'''




'''prices = [8758,8095,2949,176,897,5600,7000]
res = list(map(lambda price : price + price*0.18, prices))
print(res)'''




'''names = ['cherry','viswa','ghani','santhu','kiran','naga']
res = list(map(lambda name: name.title(),names))
print(res)'''



'''rices = [8758,8095,2949,176,897,5600,7000]
res = list(map(lambda price: price - price*0.3, prices))
print(res)'''



'''prices = [8758,8095,2949,176,897,5600,7000]
res = list(filter(lambda price: price>100, prices))
print(res)'''




'''prices = [8758,8095,2949,176,897,5600,7000]
res = list(filter(lambda price: price%2!=0, prices))
print(res)'''



'''names = ['cherry','viswa','ghani','santhu','kiran','naga']
res = list(filter(lambda name: len(name)>5, names))
print(res)'''


'''from functools import reduce
l = [5,56,79,8969,456,24]
res = reduce(lambda sum,i:sum+i,l)
print(res)
names = ['cherry','viswa','ghani','santhu','kiran','naga']
res = reduce(lambda res,i: res+' '+i, names)
print(res)'''




'''products = {'sugar':70,
            'salt':50,
            'cooking oil':170,
            'bread':35
            }
print(dict(sorted(products.items())))
print(dict(sorted(products.items(),reverse=True)))
print(dict(sorted(products.items(),key = lambda i:i[1])))
print(dict(sorted(products.items(),key = lambda i:i[1],reverse=True)))'''



