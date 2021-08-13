import sys
R=0,1,2

# v returns true iif no character beside '0' appears more than once
def v(b):x=list(filter('0'.__ne__,b));return len(x)==len(set(x))

def S(b,n):
 """Given b, a board as a string or list (len(b)==81), and n as the starting point in the board,
 solve the puzzle according to standard Sudoku rules."""
 # If our start character is not 0, it's a given so return the result of
 # trying the next character
 if'0'!=b[n]:return S(b,n+1)

 # make a local copy
 b=list(b)

 # try all digits 1-9
 for t in'123456789':
  b[n]=t

  # validate all rows and columns
  for j in range(9):t=v(b[9*j:9*j+9])and v(b[j::9])and t

  # validate the 9 squares
  for x in R:
   for y in R:u=x*3+y*27;t=v(b[u:u+3]+b[u+9:u+12]+b[u+18:u+21])and t

  # check if the board is not valid, then return None
  # otherweise start filling in the next position if not finished
  # and if the board is valid and no '0's are in it, then we've solved it and exit w/ printing it
  t=t and (S(b,n+1) if'0'in b else exit(''.join(b)))

 # if the loop finishes and we reach here, we've failed and return None

# start solving from the first position
S(sys.argv[1],0)
