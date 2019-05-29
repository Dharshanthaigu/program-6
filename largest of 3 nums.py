def max_num(x,y):
  if x>y:
    return x
  else:
    return y
def max_num_three(x,y,z):
  return max_num(x,max_num(y,z))
l,m,n=input().split()
a=int(l)
b=int(m)
c=int(n)
print(max_num_thre,b,c))




  
