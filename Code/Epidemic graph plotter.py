#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


#varying p
wide = range(10)
sir = [63.05,66.25,66.55,64.2,63.65,62.25,63.5,61.8,64.0,60.25]

plt.plot(sir,'slategray', label ="SIR")

n = ['1','2','4','8','16','32','64','128','256','512']
plt.xticks(wide, n)
plt.title('Varying number of initial adopters')
plt.xlabel("n")
plt.ylabel("Disease lifespan")

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()


# In[32]:


#varying p
wide = range(10)
#sir = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
sis = [11.99,13.01,13.46,13.68,13.97,13.98,14.04,14.23, 14.26, 14.21]
sirs = [9.06,7.32,5.56,3.85,1.82,0.69,0.0,0.0,0.0,0.0]

#plt.plot(sir,'slategray', label ="SIR")
plt.plot(sis,'navy', label = "SIS")
plt.plot(sirs,'darkorange', label = "SIRS")

n = ['1','2','4','8','16','32','64','128','256','512']
plt.xticks(wide, p)
plt.title('Varying infection probabilities')
plt.xlabel("p")
plt.ylabel("Average number of infections per day")

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()


# In[31]:


#varying n
wide = range(10)
#sir = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
sis = [11.42, 12.05,12.05,12.05,12.01,11.97,11.87,11.59,11.18,10.25]
sirs = [8.86,9.15,8.84,8.74,8.49,8.12,7.75,7.34,6.79,5.80]

#plt.plot(sir,'slategray', label ="SIR")
plt.plot(sis,'navy', label = "SIS")
plt.plot(sirs,'darkorange', label = "SIRS")

n = ['1','2','4','8','16','32','64','128','256','512']
plt.xticks(wide, n)
plt.title('Varying number of initial adopters')
plt.xlabel("n")
plt.ylabel("Average number of infections per day")

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()


# In[40]:


#varying n
wide = range(10)
#sir = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
sis = [0.84,9.37,10.82,12.79,12.96,13.36,13.16,13.79,13.21,13.60]
sirs = [0.0,4.65,8.85,11.79,11.95,8.19,12.33,8.74,12.65,14.08]

#plt.plot(sir,'slategray', label ="SIR")
plt.plot(sis,'navy', label = "SIS")
plt.plot(sirs,'darkorange', label = "SIRS")

n = ['1','10','20','30','40','50','60','70','80','90']
plt.xticks(wide, n)
plt.title('Varying infection durations')
plt.xlabel("t {}".format('\N{LATIN SUBSCRIPT SMALL LETTER i}'))
plt.ylabel("Average number of infections per day")

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()


# In[42]:


#varying n
wide = range(10)
#sir = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#sis = [0.84,9.37,10.82,12.79,12.96,13.36,13.16,13.79,13.21,13.60]
sirs = [10.86,8.73,7.65,0.03,0.0,0.0,0.0,0.0,0.0,0.0]

#plt.plot(sir,'slategray', label ="SIR")
#plt.plot(sis,'navy', label = "SIS")
plt.plot(sirs,'darkorange', label = "SIRS")

r = ['1','10','20','30','40','50','60','70','80','90']
plt.xticks(wide, n)
plt.title('Varying removal durations')
plt.xlabel("r")
plt.ylabel("Average number of infections per day")

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()


# In[ ]:




