import sys
R=0,1,2
def v(b):x=list(filter('0'.__ne__,b));return len(x)==len(set(x))
def S(b,n):
 if'0'!=b[n]:return S(b,n+1)
 b=list(b)
 for t in'123456789':
  b[n]=t
  for j in range(9):t=v(b[9*j:9*j+9])and v(b[j::9])and t
  for x in R:
   for y in R:u=x*3+y*27;t=v(b[u:u+3]+b[u+9:u+12]+b[u+18:u+21])and t
  if t:
   if'0'not in b:return b
   t=S(b,n+1)
  if t:return t
print(''.join(S(sys.argv[1],0)))
