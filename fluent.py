class Fluent:

  def __init__(self, count=0, cache=None):
    self._count = count

    # done because [] as a method/function default value is
    # evaluated at class declaration and shared forever afterward,
    # which is generally not what you want
    self._cache = cache or []

  def _(self, name):
    return Fluent(self._count+1, self._cache+[name])

  def method(self, final_value):
    print self._cache
    print final_value
    # TODO: anything even slightly state-modifying should return a new Fluent, not self
    return self
  
  def __getattr__(self, name):
    return self._(name)

  def __del__(self):
    print "Deleting myself"

client = Fluent()
url = client.test.hello
url.method("we")
url.method("are")
url = url.world
url.method("here")

print
print '-' * 50
print

# testing pathological (but not unusual or uncommon) case
client = Fluent()
x = client.a.b
y = client.b.a
print x._cache
print y._cache