#!/usr/bin/env python
# coding: utf-8

# ## Chinook Database Case Study

# #### Importing Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()


# In[2]:


from IPython.display import Image
Image("imgs/chinook-erd.png")


# In[ ]:





# ##### Importing Libraries & Database

# In[5]:


# Load sqlalchemy's create_engine
from sqlalchemy import create_engine

# Create database engine to manage connections
engine = create_engine("sqlite:///sql/chinook.sqlite")


# In[6]:


# Getting tables names
table_names = engine.table_names()
table_names


# In[7]:


# Load entire 'Album' table
album = pd.read_sql("Album", engine)
album.head()


# In[8]:


# Another way to get the entire 'Album' table
pd.read_sql_table("Album", engine).head()


# In[ ]:





# ##### Provide a query showing Customers (just their full names, customer ID and country) who are not in the US.
# 

# In[9]:


# Write query to get the specified customers' info
query = '''
select customerid, firstname, lastname, country
from customer
where not country = 'USA';
'''


# In[10]:


pd.read_sql(query, engine).head()


# In[ ]:





# ##### Provide a query only showing the Customers from Brazil.

# In[11]:


# Let's use 'pd.read_sql_query' method for simplicity
pd.read_sql_query("select * from customer where country = 'Brazil';", engine)


# In[ ]:





# ##### Provide a query showing the Invoices of customers who are from Brazil. The resultant table should show the customer's full name, Invoice ID, Date of the invoice and billing country.

# In[12]:


query = '''
select c.firstname, c.lastname, i.invoiceid, i.invoicedate, i.billingcountry
from customer as c, invoice as i
where c.country = 'Brazil' and
c.customerid = i.customerid;
'''
pd.read_sql(query, engine).head()


# In[ ]:





# ##### Provide a query showing only the Employees who are Sales Agents.

# In[13]:


pd.read_sql("select * from employee where employee.title = 'Sales Support Agent';", engine)


# In[ ]:





# ##### Provide a query showing a unique list of billing countries from the Invoice table.

# In[14]:


pd.read_sql_query("select distinct billingcountry from invoice;", engine)


# In[ ]:





# ##### Provide a query showing the invoices of customers who are from Brazil.

# In[15]:


query = ''' 
select *
from customer as c, invoice as i
where c.country = 'Brazil' and
c.customerid = i.customerid;
'''

pd.read_sql(query, engine).head()


# In[ ]:





# ##### Provide a query that shows the invoices associated with each sales agent. The resultant table should include the Sales Agent's full name.

# In[16]:


query = '''
select e.firstname, e.lastname, i.invoiceid, i.customerid, i.invoicedate, i.billingaddress, i.billingcountry, i.billingpostalcode, i.total
from customer as c, invoice as i
on c.customerid = i.customerid
join employee as e
on e.employeeid = c.supportrepid
order by e.employeeid;
'''

pd.read_sql(query, engine).head()


# In[ ]:





# ##### Provide a query that shows the Invoice Total, Customer name, Country and Sale Agent name for all invoices and customers.

# In[17]:


query = '''
select e.firstname as 'employee first', e.lastname as 'employee last', c.firstname as 'customer first', c.lastname as 'customer last', c.country, i.total
from employee as e
join customer as c on e.employeeid = c.supportrepid
join invoice as i on c.customerid = i.customerid
'''

pd.read_sql(query, engine).head()


# In[ ]:





# ##### How many Invoices were there in 2009 and 2011? What are the respective total sales for each of those years?

# In[18]:


query = '''
select count(i.invoiceid), sum(i.total)
from invoice as i
where i.invoicedate between datetime('2011-01-01 00:00:00') and datetime('2011-12-31 00:00:00');
'''

pd.read_sql(query, engine).head()


# In[ ]:





# ##### Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for Invoice ID 37.

# In[19]:


pd.read_sql("select count(i.invoicelineid) from invoiceline as i where i.invoiceid = 37", engine)


# In[ ]:




