def max_num(x,y):
  if x>y:
    return x
  else:
    return y
def max_num_three(x,y,z):
  return max_num(x,max_num(y,z))
a=int(input())
b=int(input())
c=int(input())
print(max_num_three(a,b,c))




  
