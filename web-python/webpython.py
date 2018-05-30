import os
import sys
# import commands
import subprocess


# obj = subprocess.run(['python3'],shell=True,universal_newlines=True,stdin=open('test.py'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # obj = subprocess.Popen('python', shell=True, stdin=open('test.py'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(obj.returncode)
# # out_error_list = obj.communicate()
# print(obj.stdout)
# print(obj.stderr)
# a = subprocess.Popen('python test.py',shell=True, cwd=os.getcwd(), stdout=subprocess.PIPE)
# print(a.stdout.read())
class WebPython(object):
	"""docstring for WebPython"""
	def __init__(self, py='python3', sudo=False, content = None):
		self.py = py
		self.sudo = sudo
		self.obj = None
		self.content = content
		self.init()

	def init(self):
		with open('test.py','w') as f:
			f.write(self.content)
		self.obj = subprocess.run(['python3'],shell=True, \
			universal_newlines=True,stdin=open('test.py'), \
			stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	def response(self):
		return self.obj.stdout or self.obj.stderr

test = WebPython(py='python3', content = 'import xixi\nprint("hello")')
# test.init()
print(test.response())


# print(commands.getstatusoutput('python test.py')[1])
# print(commands.getstatusoutput('ls /home/zhiwen/code/github/django-site/mysite/board')[1])
# print(os.walk('/home/zhiwen/code/github/django-site/mysite/board'))
# print(os.getcwd())
# print(os.system('ls'))
# print(sys.argv)
