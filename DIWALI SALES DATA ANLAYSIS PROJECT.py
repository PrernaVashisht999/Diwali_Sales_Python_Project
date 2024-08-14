#!/usr/bin/env python
# coding: utf-8

# # DIWALI SALES DATA ANLAYSIS PROJECT

# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv('Diwali Sales Data.csv', encoding = 'unicode_escape')
# to avoid encoding error, use 'unicode_escape'
# r the r prefix is mainly used to handle backslashes in file paths,
#ensuring they are treated as literal characters rather than escape characters


# In[5]:


df


# In[5]:


df.shape # rows and columns


# In[6]:


df.head() # which shows top rows 


# # DATA CLEANING 

# In[7]:


df.info()


# In[8]:


#Drop unrelated/ blank columns using pandas
df.drop(['Status','unnamed1'], axis = 1, inplace=True)
#axis=0: Operates along rows (down the columns).This is used for operations on rows.horizontally
#axis=1: Operates along columns (across the rows).This is used for operations on columns.vertically


# In[9]:


df


# In[10]:


pd.isnull(df) #which give true or false values


# In[11]:


#check for null values
pd.isnull(df).sum()


# In[12]:


#Drop null values
df.dropna(inplace=True)


# In[13]:


df.shape


# In[14]:


#Change data types
df['Amount'] = df['Amount'].astype('int')


# In[15]:


df['Amount'].dtypes


# In[16]:


df.columns


# In[17]:


#Rename column
df.rename(columns = {'Marital_Status': 'Shadi'})
# but it will not save as i perform this code temporarlily 


# In[18]:


#Describe()- method returns description of the data in the dataframe(i.e count,mean,std,etc)
df.describe()


# In[19]:


#Describe for specific columns
df[['Age','Orders','Amount']].describe()


# # EXPLORATORY DATA ANALYSIS

# # GENDER

# In[20]:


df.columns


# In[22]:


ax = sns.countplot(x ='Gender', data = df)


# In[24]:


ax = sns.countplot(x = 'Gender', data = df)
for bars in ax.containers: # Iterate over containers of bars
    ax.bar_label(bars) # Add labels to the bars in each container
#an attribute that stores the containers of plotted elements. For bar plots, containers hold the BarContainer objects.
#bar_label(): It is used to add labels to the bars in a bar plot. 


# In[25]:


df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
#as_index=False: Keeps the group-by column(s) as regular columns in the resulting DataFrame. 
#as_index=True (default): Makes the group-by column(s) the index of the resulting DataFrame.


# In[32]:


sales_gen = df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)
ax =sns.barplot(x= 'Gender', y = 'Amount', data = sales_gen)
#for bars in ax.containers:
#   ax.bar_label(bars)


# # FROM ABOVE GRAPHS WE CAN SEE THE MOST OF THE BUYERS ARE FEMALES AND EVEN THE PURCHASING POWER OF FEMALES ARE GREATER THAN MEN

# # AGE 

# In[33]:


df.columns


# In[35]:


ax = sns.countplot(x ='Age Group', data = df, hue = 'Gender')
 
for bars in ax.containers:
    ax.bar_label(bars)


# # TOTAL AMOUNT VS AGE GROUP

# In[11]:


sales_age= df.groupby(['Age Group'],as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)
sns.barplot(x = 'Age Group', y = 'Amount', data =sales_age, hue ='Age Group')


# # FROM ABOVE GRAPHS WE CAN SEE MOST OF THE BUYERS ARE OF AGE GROUP BETWEEN 26-35 YRS FEMALE

# # TOTAL NUMBER OF ORDERS FROM TOP 10 STATES

# In[37]:


df.columns


# In[38]:


sales_state= df.groupby(['State'], as_index = False)['Orders'].sum().sort_values(by = 'Orders', ascending = False).head(10)
sns.set(rc={'figure.figsize':(15,5)})# width,height
sns.barplot(x = 'State', y ='Orders', data = sales_state)
#explain
#sns.set(): This function is used to set aesthetic parameters in Seaborn.
#It can control various aspects of the appearance of the plots.

#rc: Stands for "runtime configuration" or "rcParams" in Matplotlib.
#These parameters control the default styles and properties of the plots.

#figure.figsize: This is an rc parameter that controls the size of the figure.
#It is specified as a tuple of (width, height) in inches.


# # TOTAL AMOUNT/SALES FROM TOP 10 STATES

# In[40]:


sales_state= df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by = 'Amount', ascending = False).head()
sns.set(rc={'figure.figsize':(15,5)})
ax =sns.barplot(x = 'State', y ='Amount', data = sales_state)
for bars in ax.containers:
    ax.bar_label(bars)


# # FROM ABOVE GRAPHS WE CAN SEE THAT UNEXPECTEDLY MOST OF THE ORDERS ARE FROM UTTAR PRADESH, MAHARASHTRA,KARNATKA.

# # MARITAL STATUS

# In[7]:


ax =sns.countplot(x = 'Marital_Status', data = df, hue=)
sns.set(rc={'figure.figsize':(5,5)})
for bars in ax.containers:
        ax.bar_label(bars)
plt.savefig('marriage.png',bbox_inches ='tight')


# In[48]:


sales_set =df.groupby(['Marital_Status','Gender'],as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)
sns.set(rc={'figure.figsize':(5,5)})
 sns.barplot(x = 'Marital_Status', y = 'Amount', data=sales_set, hue='Gender')


# # FROM ABOVE GRAPHS WE CAN SEE THAT MOST OF THE BUYERS ARE MARRIED (WOMEN) AND THEY HAVE HIGH PURCHASING POWER

# # OCCUPATION

# In[53]:


sns.set(rc= {'figure.figsize':(20,5)})
ax = sns.countplot(x ='Occupation',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[56]:


sales_set =df.groupby(['Occupation'],as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x = 'Occupation', y = 'Amount', data=sales_set)


# # FROM ABOVE GRAPHS WE CAN SEE MOST OF THE BUYERS ARE WORKING IN IT,HEALTHCARE SECTOR,AVIATION

# In[57]:


df.columns


# # PRODUCT CATEGORY

# In[25]:


sns.set(rc= {'figure.figsize':(20,5)})
ax = sns.countplot(x ='Product_Category',data=df, hue ='Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)


# In[59]:


sales_set =df.groupby(['Product_Category'],as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(x = 'Product_Category', y = 'Amount', data=sales_set)


# # FROM ABOVE GRAPHS WE CAN SEE MOST OF THE SOLD PRODUCTS ARE FROM FOOD, CLOTHING, AND ELECTRONICS CATEGORY

# In[13]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders', hue ='Product_ID')


# In[67]:


#TOP 10 MOST SOLD PRODUCTS
fig1,ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending = False).plot(kind ='bar')


# # CONCLUSION

# # MARRIED WOMEN AGE GROUP 26-35 YRS ARE FROM UP,MAHARASHTRA, AN KARNATAKA WORKING IN IT, HEALTHCARE,AVIATION ARE MORE LIKELY TO BUY PRODUCTS FROM FOOD,CLOTHING AND ELECTRONICS CATEGORY
