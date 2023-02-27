import numpy as np
import pandas as pd
import math as math
import operator
import sys

def main():
  if(len(sys.argv)!=5):
    print("Wrong arguments")
    exit(0)

  df=pd.read_csv(sys.argv[1])
  wt=[float(w) for w in sys.argv[2].split(',')]
  bt=[i for i in sys.argv[3].split(',')]

  if(len(wt)!=df.shape[1]-1):
    print("enter weights again")
    exit(0)
  
  if(len(bt)!=df.shape[1]-1):
    print("enter impact again")
    exit(0)


  df1=df.iloc[:,1:].values
  try:
    wt=[w/sum(wt) for w in wt]
  except:
    print("exception 1 raised")

  for i in range(df1.shape[1]):
    dmn=math.sqrt(sum(df1[:,i]**2))
    for j in range(df1.shape[0]):
      try:
        df1[j][i]= (df1[j][i])/dmn
      except:
        print("exception 2 raised")

  for i in range(df1.shape[1]):
    df1[:,i]=df1[:,i]*wt[i]

  idealbest=[]
  idealworst=[]
  for i in range(len(bt)):
    if(bt[i]=='+'):
      idealbest.append(max(df1[:,i]))
      idealworst.append(min(df1[:,i]))
    else:
      idealbest.append(min(df1[:,i]))
      idealworst.append(max(df1[:,i]))

  s_positive=[]
  s_negative=[]
  for i in range(df1.shape[0]):
    sum1=0
    sum2=0
    for j in range(df1.shape[1]):
      sum1=sum1+ (df1[i][j]-idealbest[j])**2
      sum1=math.sqrt(sum1)
      sum2=sum2+ (df1[i][j]-idealworst[j])**2
      sum2=math.sqrt(sum2)


    s_positive.append(sum1)
    s_negative.append(sum2)

  performance=[]
  for i in range(len(s_positive)):
    try:
      performance.append(s_negative[i]/(s_negative[i]+s_positive[i]))
    except:
      print("exception 3 raised")

  var=[]
  for i in range(len(performance)):
    var.append([i+1, df.iloc[i,0], performance[i],0])

  var.sort(key=operator.itemgetter(2))

  for i in range(len(var)):
    var[i][3]=len(var)-i

  var.sort(key=operator.itemgetter(0))

  df['Performance']=performance

  rank=[]
  for i in range(len(var)):
    rank.append(var[i][3])

  df['Rank']=rank
  of=sys.argv[4]
  df.to_csv(of)
  print("DONE")

if __name__=="__main__":
  main()