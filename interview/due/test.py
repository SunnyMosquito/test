test =  [{'country_to': 2, 'win': 5, 'lost': 5}, 
		 {'country_to': 3, 'win': 2, 'lost': 1}]

# fixture
# 1 vs 2 2:4
# 1 vs 3 1:2
# 1 vs 4 3:1
# 2 vs 3 3:1
# 2 vs 4 3:1
# 3 vs 4 3:1

hehe = [{'country_from': 1, 'win': 3, 'lost': 6}, 
		{'country_from': 3, 'win': 3, 'lost': 1}]
mylist = []
mydict = {}
for item in test+hehe:
	# mydict = {}
	if item.get('country_from'):
		if item.get('country_from') not in mydict:
			mydict[item.get('country_from')] = item['win'] - item['lost']
		else:
			mydict[item.get('country_from')] += item['win'] - item['lost']
	elif item.get('country_to'):
		if item.get('country_to') not in mydict:
			mydict[item.get('country_to')] = item['win'] - item['lost']
		else:
			mydict[item.get('country_to')] += item['win'] - item['lost']


	# mylist.append(mydict)

# for key,value in mydict.items():
# 	mylist.append({'country':key,'score':value})

# from django.db.models import F

# User.objects.annotate(nick=F('coreuserwxprofile__nickname')).values('id', 'nick')


print(mydict)
print(mylist)
# mylist = []

# for item in test:
# 	newdict = {}
# 	for j in hehe:
# 		if item['country_to'] == j['country_from']:
# 			newdict['country'] = item['country_to']
# 			newdict['win'] = item['win'] + j['win']
# 			newdict['lost'] = item['lost'] + j['lost']
# 		else:
# 			newdict = j
# 		mylist.append(newdict)

# print(mylist)



























# from singleton import singletion

# singletion.test()

# class Singletion(object):
#     def __new__(cls,*args,**kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super(Singletion,cls).__new__(cls, *args, **kwargs)
#         return cls._instance

# class MySingle(Singletion):
#     def test(self):
#         print('test')

# singletion1 = MySingle()
# singletion2 = MySingle()

# print(singletion1)
# print(singletion2)


# from functools import wraps
# def singletion(cls):
#     _instance = {}
#     @wraps(cls)
#     def wrap(*args, **kwargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args, **kwargs)
#         return _instance[cls]
#     return wrap

# @singletion
# class MySingle(object):
#     def test(self):
#         print('test')


# singletion1 = MySingle()
# singletion2 = MySingle()

# print(singletion1)
# print(singletion2)


# class Singleton(type):
#     def __call__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instance


# class MySingle(metaclass=Singleton):
#    print('my')

# singletion1 = MySingle()
# singletion2 = MySingle()

# print(singletion1)
# print(singletion2)