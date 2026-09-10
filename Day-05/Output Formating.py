# int float str list tuple set dict
x = input()
bdfnbknibn
x
'bdfnbknibn'
name = input()
cherry
name
'cherry'
name = input("Enter your name:")
Enter your name:ganesh
name
'ganesh'
age=input("Enter the age")
Enter the age:23
age
':23'
age = int(input("Enter your age:"))
Enter your age:25
age
25
type(age)
<class 'int'>
price=input("Enter the price:")
Enter the price:99.99
price
'99.99'
price=float(input("Enter the price:"))
Enter the price:99.99
price
99.99
type(price)
<class 'float'>
names = input("Enter the name:")
Enter the name:ganesh,cherry,viswa
names
'ganesh,cherry,viswa'
names.split()
['ganesh,cherry,viswa']
names = input("Enter the names:").split()
Enter the names: ganesh,cherry,viswa
names
['ganesh,cherry,viswa']
names = input("Enter the names:").split()
Enter the names:1 2 3 4 56 6
names
['1', '2', '3', '4', '56', '6']
map(int,names)
<map object at 0x000001ACD54ADAB0>
list(map(int,names))
[1, 2, 3, 4, 56, 6]
values=list(map(int,input().split()))
1 2 3 4 56 6
values
[1, 2, 3, 4, 56, 6]
values=list(map(float,input().split()))
1 2 666 789 4578
values
[1.0, 2.0, 666.0, 789.0, 4578.0]
names=tuple(input("Enter the names: ").split())
Enter the names: ghani viswa cherry
names
('ghani', 'viswa', 'cherry')
values=tuple(map(int,input().split()))
1 2 3 4
values
(1, 2, 3, 4)
values=tuple(map(float,input().split()))
555 677 788
values
(555.0, 677.0, 788.0)
names=set(input().split())
fhsfu vdnbdu bng
names
{'fhsfu', 'bng', 'vdnbdu'}
values=set(map(int,input().split()))
1 2 3 4
values
{1, 2, 3, 4}
values=set(map(float,input().split()))
1 2 44 99
values
{1.0, 2.0, 99.0, 44.0}
a,b = [1,2]
a
1
b
2
a,b = (1,2)
a
1
b
2
email,password = input("Enter the email and password: ").split()
Enter the email and password: byreddiganesh@gmail.com 567238901
email
'byreddiganesh@gmail.com'
password
'567238901'
a,b,c = list(map(int,input().split()))
1 2 3
a
1
b
2
c
3
name,marks = input().split()
cherry 99
name
'cherry'
marks
'99'
int(marks)
99

#Eval function
e = eval(input())
1
e
1
e = eval(input())
1234.14
e
1234.14
e = eval(input())
"ganesh"
e
'ganesh'
e = eval(input())
[1,2,3,4,4,5]
e
[1, 2, 3, 4, 4, 5]
e = eval(input())
[1,12.4,'str',[1,2,3]]
e
[1, 12.4, 'str', [1, 2, 3]]
e = eval(input())
(1,2,4,3)
e
(1, 2, 4, 3)
e = eval(input())
{1,2,3,4,5}
e
{1, 2, 3, 4, 5}
e = eval(input())
{1:1,2:2,3:3}
e
{1: 1, 2: 2, 3: 3}
e = eval(input())
True
e
True
e = eval(input())
2+3*4+5*8
e
54
#String
#concatenation
s=''
s
''
s='codegnan'
s
'codegnan'
'codegnan'+'PFS'
'codegnanPFS'
'codegnan'*10
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
' * '*20
' *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * '
'*'*20
'********************'
s = 'codegnan'
s[4]
'g'
s[-1]
'n'
s[1]
'o'
s[-2]
'a'
names = 'cherry viswa satyarao krishna'
names[0]
'c'
names[6]
' '
names[-1]
'a'
#s[start:end+1:step]=>s[0:len:1]
names[0:5]
'cherr'
names[0:6]
'cherry'
names[:6]
'cherry'
names
'cherry viswa satyarao krishna'
names[7:12]
'viswa'
names[13:21]
'satyarao'
names[22:]
'krishna'
names[-9:-18:-1]
'oaraytas '
names[::-1]
'anhsirk oaraytas awsiv yrrehc'
names[::2]
'cer iw ayrokiha'
names
'cherry viswa satyarao krishna'
'cherry ' in names
True
'satyarao' in names
True
'anil' in names
False
'karthik' not in names
True



    
