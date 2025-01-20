

n, m = map(int,input().split())

#top
for i in range(n//2):
  j = (2*i)+1
  print(('.|.'*j).center(m,'-'))
  
#center
print(('WELCOME').center(m,'-'))

#bottom
for i in reversed(range(n//2)):
  j = (2*i)+1
  print(('.|.'*j).center(m,'-'))
