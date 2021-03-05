#https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56
t = int(input())

for line in range(1, t+1):
  n, B = [int(n) for n in input().split(" ")]
  inp = [int(n) for n in input().split(" ")]

  inp.sort()
  spent = 0
  number = 0

  for home in inp:
    spent += home
    if(spent>B):
      break
    number +=1

  

  print("Case #"+str(line)+": "+str(number))


