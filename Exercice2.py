def maxProfit(prix):
  m=0
  if len(prix)==1:
    m=prix[0]
  elif len(prix)!=0:
    for i in prix:
      if i < len(prix)-1 and prix[i] < prix[i+1]:
          m=prix[i+1]

  return m