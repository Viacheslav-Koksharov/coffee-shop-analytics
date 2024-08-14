import streamlit as st
import pandas as pd
import altair as alt

def revenue_by_month(df):
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    df['Month'] = df['transaction_date'].dt.to_period('M').astype(str)
    df_grouped = df.groupby(['Month', 'store_location'])['Revenue'].sum().reset_index()
    options = ["Main revenue"] + df['store_location'].unique().tolist()
    option = st.selectbox("Select a display type:", options)

    if option == "Main revenue":
        revenue_by_mohth = df_grouped.groupby('Month')['Revenue'].sum().reset_index()    
        chart = alt.Chart(revenue_by_mohth).mark_line(point=True).encode(
        x='Month:T',
        y='Revenue:Q'
        ).properties(
        width=700,
        height=400
        ).interactive()

        text = chart.mark_text(
        align='left',
        baseline='middle',
        dx=5,
        dy=-5,
        color="silver"
        ).encode(
        text='Revenue:Q'
        )
        return(chart + text)
    else:
        revenue_by_location = df_grouped[df_grouped['store_location'] == option]
        chart = alt.Chart(revenue_by_location).mark_line(point=True).encode(
        x='Month:T',
        y='Revenue:Q'
        ).properties(
        width=800,
        height=400
        ).interactive()

        text = chart.mark_text(
        align='left',
        baseline='middle',
        dx=5,
        dy=-5,
        color="silver"
        ).encode(
        text='Revenue:Q'
        )
        return(chart + text)

def transaction_by_location_chart(df):
    transaction_by_location = df.groupby(["store_location"])[["transaction_qty"]].sum().reset_index()
    scale = alt.Scale(
    domain=["Lower Manhattan", "Hell's Kitchen", "Astoria"],
    range=["#379683", "#EDF5E1", "#7395AE"],
    )
    bars = alt.Chart(transaction_by_location).mark_bar().encode(
    x=alt.X("store_location:N", axis=alt.Axis(labelAngle=0, title="Store location")),
    y=alt.Y("transaction_qty:Q",axis=alt.Axis(title="Transaction  Count")),
    color=alt.Color("store_location:N", scale=scale, legend=None)
    ).properties(
    width=700,
    height=400
    ).interactive()

    text = bars.mark_text(
    align='center',
    baseline='middle',
    dy=-15,
    fontSize=12, 
    color="silver"
    ).encode(
    text='transaction_qty:Q',
    )
    return bars + text

def transaction_by_product_category_chart(df):
    transaction_by_product_category = df.groupby(["product_category"])[["transaction_id"]].count().reset_index()
    transaction_by_product_category = transaction_by_product_category.sort_values(by="transaction_id", ascending=False)

    barsCTPC = alt.Chart(transaction_by_product_category).mark_bar().encode(
        y=alt.Y("product_category:N", sort="-x", axis=alt.Axis(labelAngle=0,title="Product  Category")),
        x=alt.X("transaction_id:Q",axis=alt.Axis(title="Transaction Count")),
    ).properties(
        width=800,
        height=400
    ).interactive()

    textCTPC = barsCTPC.mark_text(
        align='left',
        baseline='middle',
        dx=3,  
        fontSize=12, 
        color="silver"
    ).encode(
        text='transaction_id:Q',
    )

    return barsCTPC + textCTPC

def revenue_by_product_category_chart(df):
    revenue_by_product_category = df.groupby(["product_category"])[["Revenue"]].sum().reset_index()
    revenue_by_product_category = revenue_by_product_category.sort_values(by="Revenue", ascending=False)
    barsRPC = alt.Chart(revenue_by_product_category).mark_bar(color="#7395AE").encode(
    y=alt.Y("product_category:N", sort="-x", axis=alt.Axis(labelAngle=0,title="Product  Category")),
    x="Revenue:Q",
    ).properties(
    width=800,
    height=400
    ).interactive()

    textRPC = barsRPC.mark_text(
    align='center',
    baseline='middle',
    dx=30,
    fontSize=12, 
    color="silver"
    ).encode(
    text='Revenue:Q',
    )
    return barsRPC + textRPC

def transaction_by_product_type_chart(df):
    transaction_by_product_type = df.groupby(["product_type"])[["transaction_id"]].count().reset_index()
    transaction_by_product_type = transaction_by_product_type.sort_values(by="transaction_id", ascending=False)

    barsCTPT = alt.Chart(transaction_by_product_type).mark_bar().encode(
        y=alt.Y("product_type:N", sort="-x", axis=alt.Axis(labelAngle=0,title="Product  Type")),
        x=alt.X("transaction_id:Q",axis=alt.Axis(title="Transaction Count")),
    ).properties(
        width=800,
        height=700
    ).interactive()

    textCTPT = barsCTPT.mark_text(
        align='left',
        baseline='middle',
        dx=3,  
        fontSize=12, 
        color="silver"
    ).encode(
        text='transaction_id:Q',
    )
    return barsCTPT + textCTPT

def revenue_by_product_type_chart(df):
    revenue_by_product_type = df.groupby(["product_type"])[["Revenue"]].sum().reset_index()
    revenue_by_product_type = revenue_by_product_type.sort_values(by="Revenue", ascending=False)
    barsRPT = alt.Chart(revenue_by_product_type).mark_bar(color="#7395AE").encode(
    y=alt.Y("product_type:N", sort="-x", axis=alt.Axis(labelAngle=0,title="Product  Type")),
    x="Revenue:Q",
    ).properties(
    width=800,
    height=700
    ).interactive()

    textRPT = barsRPT.mark_text(
    align='center',
    baseline='middle',
    dx=30,
    fontSize=12, 
    color="silver"
    ).encode(
    text='Revenue:Q',
    )
    return barsRPT + textRPT