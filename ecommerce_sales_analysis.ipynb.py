#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("ecommerce_sales.csv")


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.isnull().sum()


# In[7]:


df.duplicated().sum()


# In[8]:


df.dtypes


# In[9]:


df["Order_Date"] = pd.to_datetime(df["Order_Date"])


# In[10]:


df.dtypes


# In[11]:


df.describe()


# ### Product Performance

# In[12]:


product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

product_sales


# ### Category wise sales

# In[13]:


category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

category_sales


# ### Region-wise Sales

# In[14]:


region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

region_sales


# ### Monthly Sales Trend

# In[15]:


monthly_sales = df.groupby(df["Order_Date"].dt.month)["Sales"].sum()

monthly_sales


# ### Profit by Category

# In[16]:


category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

category_profit


# ### Payment Mode Analysis

# In[17]:


payment_sales = df.groupby("Payment_Mode")["Sales"].sum().sort_values(ascending=False)

payment_sales


# ### Top 10 Customers

# In[18]:


top_customers = df.groupby("Customer_ID")["Sales"].sum().sort_values(ascending=False).head(10)

top_customers


# ### Discount Analysis

# In[19]:


discount_analysis = df.groupby("Discount")[["Sales", "Profit"]].sum()

discount_analysis


# ### Product-wise Sales Chart

# In[20]:


import matplotlib.pyplot as plt

product_sales.plot(kind="bar", figsize=(10,5))

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()


# ### Category-wise Sales Chart

# In[21]:


category_sales.plot(kind="bar", figsize=(8,5))

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.show()


# ### Monthly Sales Trend Chart

# In[22]:


monthly_sales.plot(kind="line", marker="o", figsize=(10,5))

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(range(1, 13))
plt.grid()
plt.show()


# ### Profit by Category Chart

# In[23]:


category_profit.plot(kind="bar", figsize=(8,5))

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.show()


# ### Region-wise Sales Chart

# In[24]:


region_sales.plot(kind="bar", figsize=(8,5))

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.show()


# ### Payment Mode Sales Chart

# In[25]:


payment_sales.plot(kind="bar", figsize=(8,5))

plt.title("Sales by Payment Mode")
plt.xlabel("Payment Mode")
plt.ylabel("Total Sales")
plt.xticks(rotation=20)
plt.show()


# In[26]:


kpi_summary = {
    "Total Sales": df["Sales"].sum(),
    "Total Profit": df["Profit"].sum(),
    "Total Orders": df["Order_ID"].count(),
    "Total Quantity": df["Quantity"].sum(),
    "Average Order Value": df["Sales"].mean()
}

kpi_summary


# In[27]:


df.to_csv("ecommerce_sales_cleaned.csv", index=False)


# In[ ]:




