#https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c
t = int(input())

def trace(square):
  i = 0
  sum = 0
  for line in square:
    sum += int(line[i])
    i+=1
  return sum

def col(square, size):
  n = 0
  for c in range(0, size):
    column = []
    for line in square:
      column.append(line[c])
    if(len(set(column)) != len(column)):
      n+=1
  return n

def row(square, size):
  n = 0
  for line in square:
    if(len(set(line))!=len(line)):
      n+=1
  return n


for case in range(1, t+1):
  N = int(input())

  square = []

  for line in range(0, N):
    l = [int(x) for x in input().split(" ")]
    square.append(l)

  print("Case #"+str(case)+": "+str(trace(square)) + " " + str(row(square, N))+ " " + str(col(square, N)))



