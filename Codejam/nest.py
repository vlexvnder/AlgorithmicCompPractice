#https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f
#Works only for 1's and 0's, not 1-9
t = int(input())

for case in range(1, t+1):
  s = input()
  
  out = ""
  prev = "0"
  for i,c in enumerate(s):
    end = False
    try:
      next = s[i+1]
    except:
      end = True

    if(c=="0"):
      out+=c

    else:
      if(prev=="0"):
        out+="("+"1"
      if(next=="0" or end == True):
        out+=")"
      elif(next=="1"):
        out+=c
      else:
        out+=c+")"
    prev = c
  print("Case #"+str(case)+": "+out)
    

