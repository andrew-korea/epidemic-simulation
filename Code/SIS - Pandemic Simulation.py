#!/usr/bin/env python
# coding: utf-8

# In[1]:


import snap
import random
import os
import csv
from csv import reader
#import pandas as pd
import matplotlib.pyplot as plt
from random import randrange

no_susc = 0


def create_graph(no_susc):
    i = 0
    with open(totalpath,"r") as f:
        csv_reader = reader(f)
        header = next(csv_reader)

        #read file with header
        if header != None:
            for row in csv_reader:
                src = int(row[0])
                tgt = int(row[1])

                if src not in nodesList:
                    nodesList.append(src)
                    G.AddNode(src)
                    no_susc +=1
                if tgt not in nodesList:
                    nodesList.append(tgt)
                    G.AddNode(tgt)
                    no_susc+=1

                G.AddEdge(src,tgt)                
                print("adding...")
            print("DONE")
        return no_susc


# In[42]:


def init_tlist(t):
    #initial adopter
    for node in G.Nodes():
        t_list.append(0)
    #t_list[0] = t

    initial_adopters = []
    #initial_nodes.append(0)
    count = 0
    while count < 1:
        n = randrange(7126)
        
        while n in initial_adopters:
            n = randrange(7126)
        
        t_list[n] = t        
        initial_adopters.append(n)
        count +=1
        
    print("initial nodes:", initial_adopters)

def infect(t):
    #infection probability p
    choices = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    inf_thisround = []
    
    #infect
    for node in G.Nodes():
        if t_list[node.GetId()] > 0 and node.GetId() not in inf_thisround:
            for dst in node.GetOutEdges():
                if  t_list[dst] == 0:
                    num = random.choice(choices)
                    if num == 1:
                        t_list[dst] = t
                        inf_thisround.append(dst)
                        
        
    #subtract from t
    for node in G.Nodes():
        if t_list[node.GetId()] > 0 and node.GetId() not in inf_thisround:
            t_list[node.GetId()]-=1
    


def print_stats():
    for i in range(0, len(t_list)):
        if t_list[i] == 0:
            status = "s"
        else:
            status="infected"
            

def init_removed():
    for node in G.Nodes():
        removed.append(0)
        
def get_no(l):
    count = 0
    for item in l:
        if item != 0:
            count+=1
    return count

def get_stats(G):
    print("Number of Nodes: %d" % G.GetNodes())
    G.PrintInfo("Python type TUNGraph", "info-pungraph.txt")

    #node with highest degree
    NId = snap.GetMxDegNId(G)
    print("max degree node:", NId)
    
    #degree distribution
    DegToCntV = snap.TIntPrV()
    snap.GetDegCnt(G,DegToCntV)

    for item in DegToCntV:
        noOfNodes.append(item.GetVal2())
        degrees.append(item.GetVal1())
        
    #modularity
    modularity, CmtyV = G.CommunityCNM()
    for Cmty in CmtyV:
        community_sizes.append(Cmty.Len())
    print("The modularity of the network is %f" % modularity)


# In[3]:


G = snap.TUNGraph.New()
nodesList = [] #record nodes added

cwd = os.getcwd()
datapath = '\\twitch\\ENGB\\musae_ENGB_edges.csv'
totalpath = cwd + datapath #dataset directory


no_susc = create_graph(no_susc)


# In[55]:


all_avgs =[]
def inf_rate(inf_record, max_step):
    for i in range(0,max_step-1):
        slope = (inf_record[i+1]-inf_record[i])/((i+1)-i)
        deriv.append(slope)
            
for i in range(0,20):
    print("Iteration: ", i)
    status = snap.TIntStrH()
    steps = 0
    t = 10 #sick period
    removed = []
    init_removed()
    t_list = []
    init_tlist(t)
    sus_record =[]
    inf_record = []
    rem_record = []
    
    #time
    max_step = 500

    while steps < max_step:
        infect(t)
        #print("========Step %d========" %(steps+1))
        print_stats()
        steps +=1
        susCount = no_susc - get_no(t_list) - get_no(removed)
        infCount =get_no(t_list)
        remCount = get_no(removed)
        #print("No. of Susceptible: ", susCount)
        #print("No. of Infected: ", infCount)
        sus_record.append(susCount)
        inf_record.append(infCount)
        rem_record.append(remCount)
        #print()
        
    deriv = []

    inf_rate(inf_record,max_step)
    avg = sum(deriv)/len(deriv)
    print("Average simulation infection rate:", avg)
    all_avgs.append(avg)
    
print("===============")
avg = sum(all_avgs)/len(all_avgs)
print("Average Infection Rate", avg)# average number of infections per step
# expected number of new cases in the entire network


# In[43]:


noOfNodes =[]
degrees = []
community_sizes = []
get_stats(G)


# In[56]:


plt.plot(sus_record,'forestgreen', label ="Susceptible")
plt.plot(inf_record,'crimson', label = "Infected")
plt.title('SIS - Simulation')
plt.xlabel("Time")
plt.ylabel("Population")

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()


# In[57]:


import numpy
from matplotlib import pylab
#plt.plot(sus_record,'forestgreen', label ="Susceptible")
plt.plot(inf_record,'crimson', label = "Infected")
plt.title('SIS - Simulation')
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

z = np.polyfit(range(0,500), inf_record, 1)
p = np.poly1d(z)
plt.plot(range(0,499),p(range(0,499)),"red")

plt.show()


# In[46]:


z = np.polyfit(range(0,500), inf_record, 1)
p = np.poly1d(z)
plt.plot(range(0,499),p(range(0,499)),"red")

plt.show()


# In[47]:


plt.plot(deriv,'blueviolet')
plt.title('SIS - Rates of Infection')
plt.xlabel("Time")
plt.ylabel("Rate of Infection")
plt.show()


# In[52]:


G.PlotClustCf("SIS", "Undirected graph - clustering coefficient")


# In[49]:


from mpl_toolkits.mplot3d import axes3d, Axes3D

fig = plt.figure()
ax = Axes3D(fig)

x = []
def create_x(max_step):
    for i in range(0,max_step):
        x.append(i)

create_x(max_step)
y = inf_record
z = deriv
z.append(0) #we need to add an arbitrary value since the length of the derivative list is 1 short.

ax.plot3D(x, y, z, color='crimson')
ax.set_title('SIS - A Comprehensive Relationship')
ax.set_xlabel('Time')
ax.set_ylabel('Infected population')
ax.set_zlabel('Rate of infection')

plt.show()


# In[ ]:




