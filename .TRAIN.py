l=[]
l3=[]
out=[]
In=[]
In1=[]
In2=[]
In3=[]
t=0
p=[]
aifile3=[]
results=[]
movements=[]
resultstotal=[]
resultsaverage=0
printvalue=''
ba=0
t=int(input('how many evolutions are we doing? '))
import random
import json
import time
def DNAs(scores):
    global file1
    global file2
    global In4
    global In5
    dnalist=[]
    newdna=[]
    Number=[0,1]
    t=0
    In4=[]
    In5=[]
    highest=[scores[0],scores[1]]
    for number in range(len(scores)):
        if number>highest[0]:
            highest[0]=scores[number]
            Number[0]=number
        elif number>highest[1]:
            highest[1]=scores[number]
            Number[1]=number
    file1='ACESbraincells%a.json'% (Number[0]+1)
    file2='ACESbraincells%a.json'% (Number[1]+1)
    with open(file1,'r') as f:
        In4=[round(x,1) for x in json.load(f)]
    with open(file2,'r') as f:
        In5=[round(x,1) for x in json.load(f)]
    i1=random.randrange(0,128)
    dnalist.append(i1)
    for DNAs1 in range(63):
        while dnalist[DNAs1]==i1:
            i1=random.randrange(0,128)
        dnalist.append(i1)
    i2=0
    for i in range(128):
        if i2<=1:
            if dnalist[i2]==i:
                newdna.append(In4[i])
                i2+=1
            else:
                newdna.append(In5[i])
        else:
            newdna.append(In5[i])
    return newdna
def evolve(DNA):
    global In4
    global In5
    for a in range(10):
        i=a+1
        file='ACESbraincells%a.json'% i
        if i==1:
            with open(file,'w') as f:
                json.dump(In4,f)
        if i==2:
            with open(file,'w') as f:
                json.dump(In5,f)
        if i>2:
            with open(file,'w') as f:
                i2=[round(x,1) for x in mutate(DNA)]
                json.dump(i2,f)
def mutate(DNA):
    global results
    global printvalue
    global average
    printvalue=str(round(sum(results)/len(results),1))
    for i in range(8):
        DNA1=list(DNA)
        a=i+3
        file='ACESbraincells%a.json'% a
        average=sum(results)/len(results)
        average=round(average,1)
        s=10-average
        s=s*2
        s=int(s)
        for i1 in range(s):
            s2=random.randrange(0,128)
            s1=round(float(random.randrange(-5,5)/5))
            s1=s1/10
            DNA1[s2]=round(float(DNA1[s2])+float(s1),1)
            while DNA1[s2]>0.9:
                DNA1[s2]-=0.1
            while DNA1[s2]<0.1:
                DNA1[s2]+=0.1
    return DNA1
def train():
    global l
    global l3
    l=[]
    l3=[]
    for num in range(4):
        p1=random.randrange(0,20)
        l.append(p1)
    for num in range(2):
        l2=random.randrange(-21,20)
        if l2<0:
            l.append(l2)
            l3.append(l2)
        if l2>=0:
            l.append(l2)
            l3.append(l2)
    if l3[0]>=0:
        if l3[0]>l[0]:
            l3[0]=l[0]
    if l3[0]<0:
        if (0-l3[0])>l[2]:
            l3[0]=(0-l[2])
    if l3[1]>=0:
        if l3[1]>l[1]:
            l3[1]=l[1]
    if l3[1]<0:
        if (0-l3[1])>l[3]:
            l3[1]=(0-l[3])
def start(file):
    global l
    global out
    global In
    global In1
    global In2
    global In3
    global val
    out=[]
    In=[]
    In1=[]
    In2=[]
    In3=[]
    In4=[]
    with open(file,'r') as f:
        nodes = json.load(f)
        nodes=list(nodes)
    In = nodes[0:32]
    In1 = nodes[32:64]
    In2 = nodes[64:96]
    In3 = nodes[96:128]
    n1=0
    for n in l:
        val=0
        for i in range(32):
            val+=(In[i]*l[0])
            val+=(In1[i]*l[1])
            val+=(In2[i]*l[2])
            val+=(In3[i]*l[3])
            val+=(In2[i]*l[4])
            val+=(In3[i]*l[5])
        val=int(round(val,0))
        while val > n and n!=0 and n!=l[4] and n!=l[5]:
            val-=n
        if n==0:
            val=0
        while val < 0:
            val=0
        out.append(val)
for one in range(1):
    for loop in range(t):
        train()
        results=[]
        for ainum0 in range(10):
            ainum=ainum0+1
            aifile='ACESbraincells%a.json'% ainum
            start(aifile)
            og_dist=abs(l3[0])+abs(l3[1])
            up=out[0]-out[2]
            up=l3[0]-up
            right=out[1]-out[2]
            right=l3[1]-right
            result=abs(up)+abs(right)
            if result>og_dist:
                result=0.0
            elif og_dist!=0:
                result=og_dist-result
                result=result/og_dist
            else:
                result=0.25
            result=max(0.0,min(1.0,result))
            result=(round(result,1))*10
            result=int(result)
            results.append(result)
            for john in range(4):
                movements.append(str(out[john]))
            for josh in range(4):
                movements.append(str(l[josh]))
            for james in range(2):
                movements.append(str(l3[james]))
        DNA=list(DNAs(results))
        evolve(DNA)
        resultstotal.append(average)
        resultsaverage=float(sum(resultstotal)/len(resultstotal))
        if average>=ba:
            ba=average
        print(results)
        print('total average: ', str(round(resultsaverage,1)))
        print('batch average: ', str(average))
        print('best batch average: ', str(ba))
        print(len(resultstotal),'/',t)
        print('\n')
bf=0
with open('ACESbraincells1.json','r') as f:
    bf1=json.load(f)
for ainum1 in range(10):
            ainum=ainum1+1
            train()
            aifile='ACESbraincells%a.json'% ainum
            with open(aifile,'r') as f:
                if str(json.load(f))=='':
                    bf=1
            if bf==1:
                with open(aifile,'w') as f:
                    json.dump(bf1,f)
            bf=0
time.sleep(3)

