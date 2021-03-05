#https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9
#No good -- needs to work unsorted
t = int(input())

class parent:
  def __init__(self, name):
    self.busy = False
    self.name = name
    self.busyUntil = 0
for case in range(1, t+1):
  s = int(input())
  j = parent("J")
  c = parent("C")

  times = []

  result = ""
  for n in range(0, s):
    times.append([int(n) for n in input().split(" ")])
  times.sort()
  times.append([1442, 1444])
  print(times)
  next = 0

  for time in range(0, 1441):
    if(j.busyUntil==time):
      j.busyUntil=0
      j.busy = False
    if(c.busyUntil==time):
      c.busyUntil=0
      c.busy = False
    if(time!=times[next][0]):
      pass
    else:
      if(not j.busy):
        j.busy = True
        j.busyUntil = times[next][1]
        next+=1
        result+="J"
      elif(not c.busy):
        c.busy = True
        c.busyUntil = times[next][1]
        next+=1
        result+="C"
      else:
        result="IMPOSSIBLE"
        break
  print(result)


