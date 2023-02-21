#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import json
import glob


import plotly.express as px
import streamlit as st

from plotly.subplots import make_subplots


# In[6]:


#Reading csv file using pandas
agg_tran=pd.read_csv("agg_trans.csv")
agg_user=pd.read_csv("agg_users.csv")
map_tran=pd.read_csv("map_trans.csv")
map_user=pd.read_csv("map_users.csv")
top_tran=pd.read_csv("top_trans.csv")
top_user=pd.read_csv("top_users.csv")


# In[3]:


# Replacing the state names
agg_tran["state"] = agg_tran["state"].replace({
    'andaman-&-nicobar-islands': 'Andaman & Nicobar',
    'andhra-pradesh': 'Andhra Pradesh',
    'arunachal-p': 'Arunachal Pradesh',
    'assam': 'Assam',
    'bihar': 'Bihar',
    'chandigarh': 'Chandigarh',
    'chhattisgarh': 'Chhattisgarh',
    'dadra-&-nagar-haveli-&-dama': 'Dadra & Nagar Haveli',
    'delhi': 'NCT of Delhi',
    'goa': 'Goa',
    'gujarat': 'Gujarat',
    'haryana': 'Haryana',
    'himachal-pradesh': 'Himachal Pradesh',
    '&-kashmir': 'Jammu & Kashmir',
    'jharkhand': 'Jharkhand',
    'karnataka': 'Karnataka',
    'kerala': 'Kerala',
    'ladakh': 'Ladakh',
    'lakshadweep': 'Lakshadweep',
    'madhya-pradesh': 'Madhya Pradesh',
    'maharashtra': 'Maharashtra',
    'manipur': 'Manipur',
    'meghalaya': 'Meghalaya',
    'mizoram': 'Mizoram',
    'nagaland': 'Nagaland',
    'puducherry': 'Puducherry',
    'punjab': 'Punjab',
    'rajasthan': 'Rajasthan',
    'sikkim': 'Sikkim',
    'tamil-nadu': 'Tamil Nadu',
    'telangana': 'Telangana',
    'tripura': 'Tripura',
    'uttar-pradesh': 'Uttar Pradesh',
    'uttarakhand': 'Uttarakhand',
    'west-bengal': 'West Bengal',
    'odisha': 'Odisha'
})


# In[4]:


# Replacing the state names
agg_user["state"] = agg_user["state"].replace({
    'andaman-&-nicobar-islands': 'Andaman & Nicobar',
    'andhra-pradesh': 'Andhra Pradesh',
    'arunachal-p': 'Arunachal Pradesh',
    'assam': 'Assam',
    'bihar': 'Bihar',
    'chandigarh': 'Chandigarh',
    'chhattisgarh': 'Chhattisgarh',
    'dadra-&-nagar-haveli-&-dama': 'Dadra & Nagar Haveli',
    'delhi': 'NCT of Delhi',
    'goa': 'Goa',
    'gujarat': 'Gujarat',
    'haryana': 'Haryana',
    'himachal-pradesh': 'Himachal Pradesh',
    '&-kashmir': 'Jammu & Kashmir',
    'jharkhand': 'Jharkhand',
    'karnataka': 'Karnataka',
    'kerala': 'Kerala',
    'ladakh': 'Ladakh',
    'lakshadweep': 'Lakshadweep',
    'madhya-pradesh': 'Madhya Pradesh',
    'maharashtra': 'Maharashtra',
    'manipur': 'Manipur',
    'meghalaya': 'Meghalaya',
    'mizoram': 'Mizoram',
    'nagaland': 'Nagaland',
    'puducherry': 'Puducherry',
    'punjab': 'Punjab',
    'rajasthan': 'Rajasthan',
    'sikkim': 'Sikkim',
    'tamil-nadu': 'Tamil Nadu',
    'telangana': 'Telangana',
    'tripura': 'Tripura',
    'uttar-pradesh': 'Uttar Pradesh',
    'uttarakhand': 'Uttarakhand',
    'west-bengal': 'West Bengal',
    'odisha': 'Odisha'
})


# In[5]:


# Replacing the state names
map_tran["state"] = map_tran["state"].replace({
    'andaman-&-nicobar-islands': 'Andaman & Nicobar',
    'andhra-pradesh': 'Andhra Pradesh',
    'arunachal-p': 'Arunachal Pradesh',
    'assam': 'Assam',
    'bihar': 'Bihar',
    'chandigarh': 'Chandigarh',
    'chhattisgarh': 'Chhattisgarh',
    'dadra-&-nagar-haveli-&-dama': 'Dadra & Nagar Haveli',
    'delhi': 'NCT of Delhi',
    'goa': 'Goa',
    'gujarat': 'Gujarat',
    'haryana': 'Haryana',
    'himachal-pradesh': 'Himachal Pradesh',
    '&-kashmir': 'Jammu & Kashmir',
    'jharkhand': 'Jharkhand',
    'karnataka': 'Karnataka',
    'kerala': 'Kerala',
    'ladakh': 'Ladakh',
    'lakshadweep': 'Lakshadweep',
    'madhya-pradesh': 'Madhya Pradesh',
    'maharashtra': 'Maharashtra',
    'manipur': 'Manipur',
    'meghalaya': 'Meghalaya',
    'mizoram': 'Mizoram',
    'nagaland': 'Nagaland',
    'puducherry': 'Puducherry',
    'punjab': 'Punjab',
    'rajasthan': 'Rajasthan',
    'sikkim': 'Sikkim',
    'tamil-nadu': 'Tamil Nadu',
    'telangana': 'Telangana',
    'tripura': 'Tripura',
    'uttar-pradesh': 'Uttar Pradesh',
    'uttarakhand': 'Uttarakhand',
    'west-bengal': 'West Bengal',
    'odisha': 'Odisha'
})


# In[6]:


# Replacing the state names
map_user["state"] = map_user["state"].replace({
    'andaman-&-nicobar-islands': 'Andaman & Nicobar',
    'andhra-pradesh': 'Andhra Pradesh',
    'arunachal-p': 'Arunachal Pradesh',
    'assam': 'Assam',
    'bihar': 'Bihar',
    'chandigarh': 'Chandigarh',
    'chhattisgarh': 'Chhattisgarh',
    'dadra-&-nagar-haveli-&-dama': 'Dadra & Nagar Haveli',
    'delhi': 'NCT of Delhi',
    'goa': 'Goa',
    'gujarat': 'Gujarat',
    'haryana': 'Haryana',
    'himachal-pradesh': 'Himachal Pradesh',
    '&-kashmir': 'Jammu & Kashmir',
    'jharkhand': 'Jharkhand',
    'karnataka': 'Karnataka',
    'kerala': 'Kerala',
    'ladakh': 'Ladakh',
    'lakshadweep': 'Lakshadweep',
    'madhya-pradesh': 'Madhya Pradesh',
    'maharashtra': 'Maharashtra',
    'manipur': 'Manipur',
    'meghalaya': 'Meghalaya',
    'mizoram': 'Mizoram',
    'nagaland': 'Nagaland',
    'puducherry': 'Puducherry',
    'punjab': 'Punjab',
    'rajasthan': 'Rajasthan',
    'sikkim': 'Sikkim',
    'tamil-nadu': 'Tamil Nadu',
    'telangana': 'Telangana',
    'tripura': 'Tripura',
    'uttar-pradesh': 'Uttar Pradesh',
    'uttarakhand': 'Uttarakhand',
    'west-bengal': 'West Bengal',
    'odisha': 'Odisha'
})


# In[8]:


# Replacing the state names
top_tran["state"] = top_tran["state"].replace({
    'andaman-&-nicobar-islands': 'Andaman & Nicobar',
    'andhra-pradesh': 'Andhra Pradesh',
    'arunachal-p': 'Arunachal Pradesh',
    'assam': 'Assam',
    'bihar': 'Bihar',
    'chandigarh': 'Chandigarh',
    'chhattisgarh': 'Chhattisgarh',
    'dadra-&-nagar-haveli-&-dama': 'Dadra & Nagar Haveli',
    'delhi': 'NCT of Delhi',
    'goa': 'Goa',
    'gujarat': 'Gujarat',
    'haryana': 'Haryana',
    'himachal-pradesh': 'Himachal Pradesh',
    '&-kashmir': 'Jammu & Kashmir',
    'jharkhand': 'Jharkhand',
    'karnataka': 'Karnataka',
    'kerala': 'Kerala',
    'ladakh': 'Ladakh',
    'lakshadweep': 'Lakshadweep',
    'madhya-pradesh': 'Madhya Pradesh',
    'maharashtra': 'Maharashtra',
    'manipur': 'Manipur',
    'meghalaya': 'Meghalaya',
    'mizoram': 'Mizoram',
    'nagaland': 'Nagaland',
    'puducherry': 'Puducherry',
    'punjab': 'Punjab',
    'rajasthan': 'Rajasthan',
    'sikkim': 'Sikkim',
    'tamil-nadu': 'Tamil Nadu',
    'telangana': 'Telangana',
    'tripura': 'Tripura',
    'uttar-pradesh': 'Uttar Pradesh',
    'uttarakhand': 'Uttarakhand',
    'west-bengal': 'West Bengal',
    'odisha': 'Odisha'
})


# In[9]:


# Replacing the state names
top_user["state"] = top_user["state"].replace({
    'andaman-&-nicobar-islands': 'Andaman & Nicobar',
    'andhra-pradesh': 'Andhra Pradesh',
    'arunachal-p': 'Arunachal Pradesh',
    'assam': 'Assam',
    'bihar': 'Bihar',
    'chandigarh': 'Chandigarh',
    'chhattisgarh': 'Chhattisgarh',
    'dadra-&-nagar-haveli-&-dama': 'Dadra & Nagar Haveli',
    'delhi': 'NCT of Delhi',
    'goa': 'Goa',
    'gujarat': 'Gujarat',
    'haryana': 'Haryana',
    'himachal-pradesh': 'Himachal Pradesh',
    '&-kashmir': 'Jammu & Kashmir',
    'jharkhand': 'Jharkhand',
    'karnataka': 'Karnataka',
    'kerala': 'Kerala',
    'ladakh': 'Ladakh',
    'lakshadweep': 'Lakshadweep',
    'madhya-pradesh': 'Madhya Pradesh',
    'maharashtra': 'Maharashtra',
    'manipur': 'Manipur',
    'meghalaya': 'Meghalaya',
    'mizoram': 'Mizoram',
    'nagaland': 'Nagaland',
    'puducherry': 'Puducherry',
    'punjab': 'Punjab',
    'rajasthan': 'Rajasthan',
    'sikkim': 'Sikkim',
    'tamil-nadu': 'Tamil Nadu',
    'telangana': 'Telangana',
    'tripura': 'Tripura',
    'uttar-pradesh': 'Uttar Pradesh',
    'uttarakhand': 'Uttarakhand',
    'west-bengal': 'West Bengal',
    'odisha': 'Odisha'
})


# In[20]:


# function block for transactions
def tran(menu1, menu2):
    a = agg_tran[(agg_tran.year == menu1) & (agg_tran.quarter == menu2)]
    a = a.groupby(["state", "year", "quarter"]).sum()
    a.reset_index(inplace=True)
    return a

# function block for users
def user(menu4, menu5, menu6):
    b = agg_user[(agg_user.year == menu4) & (agg_user.quarter == menu5)]
    b.reset_index(inplace=True)
    return b

# function block for state wise transaction analysis
# function block for state-wise transaction analysis
def aggTrans(menu7, menu8, menu9, menu10):
    c = agg_tran[(agg_tran.state == menu7) & (agg_tran.year == menu8) & (agg_tran.quarter == menu9)]
    c.reset_index(inplace=True)
    return c

# function block for state-wise users analysis
def aggUser(menu11, menu12, menu13, menu14):
    d = agg_user[(agg_user.state == menu11) & (agg_user.year == menu12) & (agg_user.quarter == menu13)]
    d.reset_index(inplace=True)
    return d

# background
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://i.pinimg.com/originals/74/8c/28/748c28cd15f309f6ae3895f6828861f9.jpg");
        background-attachment: fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# In[37]:



# In[ ]:




# In[7]:


import streamlit as st
import pandas as pd
import plotly.express as px


# In[8]:


# Load data
map_user = pd.read_csv("map_Users.csv")
map_tran = pd.read_csv("map_Trans.csv")
agg_tran = pd.read_csv("Agg_Trans.csv")
agg_user = pd.read_csv("Agg_Users.csv")
top_tran=pd.read_csv("top_trans.csv")
top_user=pd.read_csv("top_users.csv")

# Create a menu with different options
selected = st.sidebar.selectbox(
    "Select an option", ["Home", "Transactions", "Users", "State wise Transaction Analysis", "State wise User Analysis", "Top10 Transaction state wise", "Top10 Transaction district wise"]
)

# Home page
if selected == "Home":
    st.write("Welcome to my dashboard!")
    st.write("Please select an option from the menu.")

# State wise Transaction Analysis
if selected == "State wise Transaction Analysis":
    menu7 = st.selectbox("Select a state for your choice", ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"])
    menu8 = st.selectbox("Select a year", [2018, 2019, 2020, 2021, 2022])
    menu9 = st.selectbox("Select a quarter", ["Q1", "Q2", "Q3", "Q4"])
    menu10 = st.selectbox("Total transaction amount or count", ["transaction_amount", "transaction_count"])
    c = agg_tran[(agg_tran["state"] == menu7) & (agg_tran["year"] == menu8) & (agg_tran["quarter"] == menu9)]
    if st.sidebar.button("show"):
        fig = px.choropleth(
            c,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_state.geojson",
            featureidkey="properties.ST_NM",
            locations="state",
            color=menu10,
            color_continuous_scale="viridis",
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.write("total transaction")
        st.write(fig)

# State wise User Analysis
if selected == "State wise User Analysis":
    menu11 = st.selectbox("Select a state for your choice", ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"])
    menu12 = st.selectbox("Select a year", [2018, 2019, 2020, 2021, 2022])
    menu13 = st.selectbox("Select a quarter", ["Q1", "Q2", "Q3", "Q4"])
    c = agg_user[(agg_user["state"] == menu11) & (agg_user["year"] == menu12) & (agg_user["quarter"] == menu13)]
    if st.sidebar.button("show"):
        fig = px.choropleth(
            c,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_state.geojson",
            featureidkey="properties.ST_NM",
            locations="state",
            color="user_count",
            color_continuous_scale="viridis",
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.write("total users")
        st.write(fig)
# Top10 Transaction state wise
if selected == "Top10 Transaction state wise":
    menu11 = st.selectbox("Select a year", [2018, 2019, 2020, 2021, 2022])
    menu12 = st.selectbox("Select a quarter", ["Q1", "Q2", "Q3", "Q4"])
    menu13 = st.selectbox("Total transaction amount or count", ["transaction_amount", "transaction_count"])
    d = agg_tran[(agg_tran["year"] == menu11) & (agg_tran["quarter"] == menu12)].groupby("state")[menu13].sum().reset_index()
    d = d.nlargest(10, columns=menu13)
    fig2 = px.bar(d, x="state", y=menu13, color=menu13, title=f"Top 10 states with highest {menu13} in {menu12} {menu11}")
    st.write(fig2)

    # Top10 Transaction district wise
if selected == "Top10 Transaction district wise":
    menu14 = st.selectbox("Select a state", agg_tran["state"].unique())
    menu15 = st.selectbox("Select a year", [2018, 2019, 2020, 2021, 2022])
    menu16 = st.selectbox("Select a quarter", ["Q1", "Q2", "Q3", "Q4"])
    menu17 = st.selectbox("Total transaction amount or count", ["transaction_amount", "transaction_count"])
    d1 = agg_tran[(agg_tran["state"] == menu14) & (agg_tran["year"] == menu15) & (agg_tran["quarter"] == menu16)]
    d1 = d1.groupby("district")[menu17].sum().reset_index()
    d1 = d1.nlargest(10, columns=menu17)
    fig3 = px.bar(d1, x="district", y=menu17, color=menu17, title=f"Top 10 districts with highest {menu17} in {menu16} {menu15} for {menu14}")
    st.write(fig3)
    

if selected == "Top10 Users":
    menu18 = st.selectbox("Select a state", agg_tran["state"].unique())
    menu19 = st.selectbox("Select a year", [2018, 2019, 2020, 2021, 2022])
    menu20 = st.selectbox("Select a quarter", ["Q1", "Q2", "Q3", "Q4"])
    menu21 = st.selectbox("Total transaction amount or count", ["transaction_amount", "transaction_count"])
    d2 = agg_tran[(agg_tran["state"] == menu18) & (agg_tran["year"] == menu19) & (agg_tran["quarter"] == menu20)]
    d2 = d2.groupby("user_id")[menu21].sum().reset_index()
    d2 = d2.nlargest(10, columns=menu21)
    fig4 = px.bar(d2, x="user_id", y=menu21, color=menu21, title=f"Top 10 users with highest {menu21} in {menu20} {menu19} for {menu18}")
    st.write(fig4)






# In[ ]:





# In[ ]:





# In[ ]:




