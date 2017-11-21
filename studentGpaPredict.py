
# coding: utf-8

# In[117]:


import sys
import pandas as pd
import numpy as np
from numpy import *
df=pd.read_csv('traindata_ccy.csv',encoding = "gb18030")


# In[118]:

df.head()


# In[119]:

prov=zeros ((3023,3))


# In[120]:

for i in range(0,3022):
    if df.loc[i,"生源省市".decode('utf8')]==u"河南省":
        prov[i,0]=1
    elif  df.loc[i,"生源省市".decode('utf8')]==u"河北省" :
        prov[i,0]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"山西省":
        prov[i,0]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"江西省":
        prov[i,0]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"青海省":
        prov[i,0]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"甘肃省":
        prov[i,0]=1    
    elif df.loc[i,"生源省市".decode('utf8')]==u"西藏自治区":
        prov[i,0]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"贵州省":
        prov[i,0]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"内蒙古自治区":
        prov[i,0]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"新疆维吾尔自治区":
        prov[i,0]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"宁夏回族自治区":
        prov[i,0]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"吉林省":
        prov[i,0]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"黑龙江省":
        prov[i,0]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"云南省":
        prov[i,0]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"辽宁省":
        prov[i,0]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"广西壮族自治区":
        prov[i,0]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"四川省":
        prov[i,1]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"广东省":
        prov[i,1]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"重庆市":
        prov[i,1]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"安徽省":
        prov[i,1]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"福建省":
        prov[i,1]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"江苏省":
        prov[i,1]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"浙江省":
        prov[i,1]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"北京市":
        prov[i,1]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"天津市":
        prov[i,1]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"上海市":
        prov[i,1]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"山东省":
        prov[i,2]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"陕西省":
        prov[i,2]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"海南省":
        prov[i,2]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"湖北省":
        prov[i,2]=1
    elif df.loc[i,"生源省市".decode('utf8')]==u"湖南省":
        prov[i,2]=1


# In[121]:

print prov[0:100]
    


# In[122]:

for i in range(0,3022):
    if df.loc[i,"裸眼视力(左)".decode('utf8')]>0 and df.loc[i,"裸眼视力(左)".decode('utf8')]< 1.6:
        if df.loc[i,"裸眼视力(左)".decode('utf8')] == 0.1:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=4
        elif df.loc[i,"裸眼视力(左)".decode('utf8')] == 0.12:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=4.1
        elif df.loc[i,"裸眼视力(左)".decode('utf8')] == 0.15:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=4.2
        elif df.loc[i,"裸眼视力(左)".decode('utf8')] == 0.2:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=4.3
        elif df.loc[i,"裸眼视力(左)".decode('utf8')] == 0.25:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=4.4
        elif df.loc[i,"裸眼视力(左)".decode('utf8')] == 0.3:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=4.5
        elif df.loc[i,"裸眼视力(左)".decode('utf8')] == 0.4:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=4.6
        elif df.loc[i,"裸眼视力(左)".decode('utf8')] == 0.5:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=4.7
        elif df.loc[i,"裸眼视力(左)".decode('utf8')] == 0.6:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=4.8
        elif df.loc[i,"裸眼视力(左)".decode('utf8')] == 0.7:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=4.9
        elif df.loc[i,"裸眼视力(左)".decode('utf8')] == 0.8:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=4.9
        elif df.loc[i,"裸眼视力(左)".decode('utf8')] == 0.9:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=5.0
        elif df.loc[i,"裸眼视力(左)".decode('utf8')] == 1.0:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=5.0
        elif df.loc[i,"裸眼视力(左)".decode('utf8')] == 1.1:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=5.1
        elif df.loc[i,"裸眼视力(左)".decode('utf8')] == 1.2:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=5.1
        elif df.loc[i,"裸眼视力(左)".decode('utf8')] == 1.3:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=5.2
        elif df.loc[i,"裸眼视力(左)".decode('utf8')] == 1.4:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=5.2
        elif df.loc[i,"裸眼视力(左)".decode('utf8')] == 1.5:
            df.loc[i,"裸眼视力(左)".decode('utf8')]=5.3
    
    if df.loc[i,"裸眼视力(右)".decode('utf8')]>0 and df.loc[i,"裸眼视力(右)".decode('utf8')]< 1.6:
        if df.loc[i,"裸眼视力(右)".decode('utf8')] == 0.1:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=4
        elif df.loc[i,"裸眼视力(右)".decode('utf8')] == 0.12:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=4.1
        elif df.loc[i,"裸眼视力(右)".decode('utf8')] == 0.15:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=4.2
        elif df.loc[i,"裸眼视力(右)".decode('utf8')] == 0.2:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=4.3
        elif df.loc[i,"裸眼视力(右)".decode('utf8')] == 0.25:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=4.4
        elif df.loc[i,"裸眼视力(右)".decode('utf8')] == 0.3:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=4.5
        elif df.loc[i,"裸眼视力(右)".decode('utf8')] == 0.4:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=4.6
        elif df.loc[i,"裸眼视力(右)".decode('utf8')] == 0.5:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=4.7
        elif df.loc[i,"裸眼视力(右)".decode('utf8')] == 0.6:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=4.8
        elif df.loc[i,"裸眼视力(右)".decode('utf8')] == 0.7:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=4.9
        elif df.loc[i,"裸眼视力(右)".decode('utf8')] == 0.8:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=4.9
        elif df.loc[i,"裸眼视力(右)".decode('utf8')] == 0.9:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=5.0
        elif df.loc[i,"裸眼视力(右)".decode('utf8')] == 1.0:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=5.0
        elif df.loc[i,"裸眼视力(右)".decode('utf8')] == 1.1:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=5.1
        elif df.loc[i,"裸眼视力(右)".decode('utf8')] == 1.2:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=5.1
        elif df.loc[i,"裸眼视力(右)".decode('utf8')] == 1.3:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=5.2
        elif df.loc[i,"裸眼视力(右)".decode('utf8')] == 1.4:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=5.2
        elif df.loc[i,"裸眼视力(右)".decode('utf8')] == 1.5:
            df.loc[i,"裸眼视力(右)".decode('utf8')]=5.3


# In[123]:

cla=zeros((3023,2))


# In[124]:

for i in range(0,3022):
    if  df.loc[i,"考生类型".decode('utf8')] == u"农村应届":
        cla[i,1]=1
    elif  df.loc[i,"考生类型".decode('utf8')] == u"城镇应届":
        cla[i,0]=1
        cla[i,1]=1
    elif  df.loc[i,"考生类型".decode('utf8')] == u"城镇往届":
        cla[i,0]=1

        


# In[125]:

df.insert(3,u"全国卷",prov[:,0])
df.insert(4,u"自主命题",prov[:,1])
df.insert(5,u"半自主命题",prov[:,2])


# In[126]:

df.head()


# In[127]:

del df[u"生源省市"]


# In[128]:

df.head()


# In[131]:

df.insert(14,u"城镇考生",cla[:,0])


# In[132]:

df.insert(15,u"应届考生",cla[:,1])


# In[134]:

del df[u"考生类型"]


# In[135]:

df.columns


# In[138]:

df.to_csv("traindata_mxj.csv",encoding="gb18030")

