import os
import time

def listdir(path):
	for p in os.listdir(path):
		file_path = os.path.join(path, p)
		if os.path.isdir(file_path):
			for p in listdir(file_path):
				yield p
		elif file_path != __file__ and not file_path.endswith('.sqlite3'):
			yield file_path

def listdir_di(path, list_name):
	for p in os.listdir(path):
		file_path = os.path.join(path, p)
		if os.path.isdir(file_path):
			listdir_di(file_path, list_name)
		elif file_path != __file__ and not file_path.endswith('.sqlite3'):
			list_name.append(file_path)

count = 0
start = time.time()
mylist = []
listdir_di('/home/zhiwen/code/github/django-site/mysite', mylist)
for p in mylist:
	with open(p) as f:
		for i in f:
			if i.strip():
				count = count+1
end = time.time()
print(count, end - start)

count = 0
start = time.time()
for p in listdir('/home/zhiwen/code/github/django-site/mysite'):
	with open(p) as f:
		for i in f:
			if i.strip():
				count = count+1
end = time.time()
print(count, end - start)