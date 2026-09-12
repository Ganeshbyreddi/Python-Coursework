data = {'name':'viswa','batch':'63','course':'PFS'}
data
{'name': 'viswa', 'batch': '63', 'course': 'PFS'}
data['name']
'viswa'
data['course']
'PFS'
data.get('age','key is not present')
'key is not present'
data.get('course','key is not present')
'PFS'
data['batch']=64
data
{'name': 'viswa', 'batch': 64, 'course': 'PFS'}
data['skills'] = ['python','mysql','flask']
data
{'name': 'viswa', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask']}
data.update({'phno':5838840802,'emai':'viswa@gmail.com'})
data
{'name': 'viswa', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 5838840802, 'emai': 'viswa@gmail.com'}
data.pop('skills')
['python', 'mysql', 'flask']
data
{'name': 'viswa', 'batch': 64, 'course': 'PFS', 'phno': 5838840802, 'emai': 'viswa@gmail.com'}
del data['name']
data
{'batch': 64, 'course': 'PFS', 'phno': 5838840802, 'emai': 'viswa@gmail.com'}
data.popitem()
('emai', 'viswa@gmail.com')
data
{'batch': 64, 'course': 'PFS', 'phno': 5838840802}
data.popitem()
('phno', 5838840802)
data
{'batch': 64, 'course': 'PFS'}
data.clear()
data
{}
data = {'name': 'viswa', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 5838840802, 'emai': 'viswa@gmail.com'}
data
{'name': 'viswa', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 5838840802, 'emai': 'viswa@gmail.com'}
data.keys()
dict_keys(['name', 'batch', 'course', 'skills', 'phno', 'emai'])
data.values()
dict_values(['viswa', 64, 'PFS', ['python', 'mysql', 'flask'], 5838840802, 'viswa@gmail.com'])
data.items()
dict_items([('name', 'viswa'), ('batch', 64), ('course', 'PFS'), ('skills', ['python', 'mysql', 'flask']), ('phno', 5838840802), ('emai', 'viswa@gmail.com')])
sorted(data)
['batch', 'course', 'emai', 'name', 'phno', 'skills']
sorted(data,reverse=True)
['skills', 'phno', 'name', 'emai', 'course', 'batch']
max(data)
'skills'
min(data)
'batch'
data
{'name': 'viswa', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 5838840802, 'emai': 'viswa@gmail.com'}
data.get('age')
data
{'name': 'viswa', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 5838840802, 'emai': 'viswa@gmail.com'}
data.setdefault('age',0)
0
data
{'name': 'viswa', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 5838840802, 'emai': 'viswa@gmail.com', 'age': 0}
data.setdefault('name','')
'viswa'
data
{'name': 'viswa', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 5838840802, 'emai': 'viswa@gmail.com', 'age': 0}
len(data)
7
all(data)
True
data
{'name': 'viswa', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 5838840802, 'emai': 'viswa@gmail.com', 'age': 0}
a={1:1,2:2}
b=a
b[3]=3
a
{1: 1, 2: 2, 3: 3}
b
{1: 1, 2: 2, 3: 3}
c=a.copy()
c[4]=4
c
{1: 1, 2: 2, 3: 3, 4: 4}
a
{1: 1, 2: 2, 3: 3}
d = dict.fromkeys(["a","b"],0)
d
{'a': 0, 'b': 0}
