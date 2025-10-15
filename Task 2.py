#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


# In[4]:


Data=pd.read_csv("/Users/habiba/Downloads/train.csv")


# In[6]:


Data.head()


# In[7]:


display(Data.info(),Data.head())


# In[8]:


#Variable	Definition	Key
#survival	Survival	0 = No, 1 = Yes
#pclass	Ticket class	1 = 1st, 2 = 2nd, 3 = 3rd
#sex	Sex	
#Age	Age in years	
#sibsp	# of siblings / spouses aboard the Titanic	
#parch	# of parents / children aboard the Titanic	
#ticket	Ticket number	
#fare	Passenger fare	
#cabin	Cabin number	
#embarked	Port of Embarkation	C = Cherbourg, Q = Queenstown, S = Southampton


# In[9]:


missing_values_count = Data.isnull().sum()
missing_values_count


# In[10]:


Data['Age'].fillna(Data['Age'].mean(), inplace=True)


# In[13]:


Data['Cabin'].fillna(Data['Cabin'].mode()[0], inplace=True)


# In[14]:


Data.tail()


# In[15]:


missing_values_count = Data.isnull().sum()
missing_values_count


# In[18]:


Data['Embarked'].fillna(Data['Embarked'].mode()[0],inplace=True)


# In[19]:


missing_values_count = Data.isnull().sum()
missing_values_count


# In[20]:


Data['Sex']=Data['Sex'].map({'male':1 ,'female':0})


# In[21]:


Data.head()


# In[22]:


survival_counts = Data[Data['Survived'] == 1]['Sex'].value_counts()
print(survival_counts)


# In[23]:


survival_percent = survival_counts / survival_counts.sum() * 100
print(survival_percent)


# In[24]:



survival_percent.plot(kind='bar', color=['#FF69B4', '#1E90FF'])

plt.title('Percentage of Survivors by Gender')
plt.ylabel('Percentage (%)')
plt.xlabel('Gender')
plt.xticks(rotation=0)
plt.show()


# In[25]:



sb.countplot(data=Data, x='Sex', hue='Survived', palette='pastel')
plt.title('Survival Count by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(['Did Not Survive', 'Survived'])
plt.show()


# In[26]:


survival_counts = Data[Data['Survived'] == 1]['Pclass'].value_counts()
print(survival_counts)


# In[27]:


survival_counts.plot(kind='bar', color=['#FF69B6', '#1E80FF','#1E90FF'])

plt.title('Percentage of Survivors by Class')
plt.ylabel('count')
plt.xlabel('class')
plt.xticks(rotation=0)
plt.show()


# In[28]:


plt.figure(figsize=(6,4))
sb.barplot(data=Data, x='Sex', y='Survived', palette=['#1E90FF', '#FF69B4'])
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate')
plt.xlabel('Gender')
plt.show()


# In[35]:


plt.figure(figsize=(6,4))
sb.barplot(data=Data, x='Pclass', y='Survived', palette='viridis')
plt.title('Survival Rate by Passenger Class')
plt.ylabel('Survival Rate')
plt.xlabel('Passenger Class')
plt.show()


# In[39]:


plt.figure(figsize=(8,5))
sb.barplot(data=Data, x='Pclass', y='Survived', hue='Sex', palette='coolwarm')
plt.title('Survival Rate by Gender and Class')
plt.show()


# In[ ]:




