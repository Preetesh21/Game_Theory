import math
# I=(1,2,3)
# J=(0,I)

def corresponding_user(n1,n2,n3,i):
  total=(n1+n2+n3)
  if(i==1):
    return n1/total
  elif(i==2):
    return n2/total
  else:
    return n3/total

def check_if_feasible(h1,h2,h3,a0):
  if(h1+h2+h3-a0>=0):
    return 1
  else:
    return 0

def average_filter(a1,a2,a3):
  return (a1+a2+a3)/3
def minimum_trust_to_achieve(h1,h2,h3,n1,n2,n3,i,a0):
  total=n1*h1+n2*h2+n3*h3
  if(i==1):
    return n1*h1*a0/total
  if(i==2):
    return n2*h2*a0/total
  if(i==3):
    return n3*h3*a0/total
def price(p1,p2,p3):
  return (p1+p2+p3)/3

def tax_pltform(p0,h1,p12,a1,p21,a2,p31,a3,p13):
  return -p0*h1-p12*a1-p13*a1+p21*a2+p31*a3

def budget_balaced(t0,t1,t2,t3):
  sum=t0+t1+t2+t3
  sum=round(sum,1)
  if(sum==0):
    return 1
  else:
    return 0

def tax_government(p0,a0):
  return p0*a0

def lets_see(message0,message1,message2,message3):
    n1=corresponding_user(0.3,0.3,0.3,1)
    n2=corresponding_user(0.3,0.3,0.3,2)
    n3=corresponding_user(0.3,0.3,0.3,3)
    a1_=average_filter(message1[4],message2[4],message3[4])
    a2_=average_filter(message1[5],message2[5],message3[5])
    a3_=average_filter(message1[6],message2[6],message3[6])
    a0_=(0.4+average_filter(message1[7],message2[7],message3[7]))/2
    h1=minimum_trust_to_achieve(message1[0],message2[0],message3[0],n1,n2,n3,1,a0_)
    h2=minimum_trust_to_achieve(message1[0],message2[0],message3[0],n1,n2,n3,2,a0_)
    h3=minimum_trust_to_achieve(message1[0],message2[0],message3[0],n1,n2,n3,3,a0_)
    p0=(message1[3]+message1[3]+message1[3])/3
    t0=tax_government(p0,a0_)
    t1=tax_pltform(p0,h1,message3[1],a1_,message3[1],a3_,message2[1],a2_,message2[1])
    t2=tax_pltform(p0,h2,message3[2],a2_,message3[2],a3_,message1[1],a1_,message1[1])
    t3=tax_pltform(p0,h3,message1[2],a3_,message1[2],a1_,message2[2],a2_,message2[2])
    return (round(a1_,3),round(a2_,3),round(a3_,3),round(a0_,3),round(h1,3),round(h2,3),round(h3,3),t0,round(t1,3),round(t2,3),round(t3,3),budget_balaced(t0,t1,t2,t3),check_if_feasible(h1,h2,h3,a0_))