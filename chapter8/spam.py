a = 37

def foo():
  print("I'm foo and a is %s" % a)

def bar():
  print("I'm bar and I'm calling foo")
  foo()

class Spam(object):
  def grok(self):
    print("I'm Spam.grok")

print("I'm spam!")
