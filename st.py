def revnum(m):
  rev=0
  while m>0:
    rem=m%10
    rev=(rev*10)+rem
    m=m//10
  return rev

a=int(input())
rev=revnum(a)
print(rev,end=" ")
