x="awesome"

def myfunc():
    print("Python is "+x)
myfunc()



print("STOP")



x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)



print("STOP")



def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)



print("STOP")



x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)