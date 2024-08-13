import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime
from charts import revenue_by_month, transaction_by_location_chart,transaction_by_product_category_chart, revenue_by_product_category_chart,transaction_by_product_type_chart,revenue_by_product_type_chart

st.set_page_config(
    page_title="Coffee Shop Sales Analysis",
    page_icon="☕"
)

with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Data analysis of Coffee shop sales")

@st.cache_data
def load_data():
    df = pd.read_excel('CoffeeShopSales.xlsx', sheet_name="Transactions")    
    return df

data_load_state = st.text('Loading data...')
df = load_data().copy()
data_load_state.text("Done! (using cache)")

st.dataframe(df.head(5))

st.subheader("Revenue by month")
RBM=revenue_by_month(df)
st.altair_chart(RBM)

st.subheader("Count of transactions by location")
TBL=transaction_by_location_chart(df)
st.altair_chart(TBL)

st.subheader("Count of Transactions and Revenue by Product Category")
CTPC = transaction_by_product_category_chart(df)
RPC = revenue_by_product_category_chart(df)
tab1, tab2 = st.tabs(["Count of Transactions by Product Category", "Revenue by Product Category"])
with tab1:
    st.altair_chart(CTPC, theme="streamlit", use_container_width=True)
with tab2:
    st.altair_chart(RPC, theme="streamlit", use_container_width=True)

st.subheader("Count of Transactions and Revenue by Product Type")
CTPT = transaction_by_product_type_chart(df)
RPT = revenue_by_product_type_chart(df)
tab1, tab2 = st.tabs(["Count of Transactions by Product Type", "Revenue by Product Type"])
with tab1:
    st.altair_chart(CTPT, theme="streamlit", use_container_width=True)
with tab2:
    st.altair_chart(RPT, theme="streamlit", use_container_width=True)

st.markdown(f'<span class="footer">© {datetime.now().year} Viacheslav Koksharov</span>', unsafe_allow_html=True)