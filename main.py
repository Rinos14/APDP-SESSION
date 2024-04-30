import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data(filename):
    return pd.read_csv(filename)

def main():
    purchase_data = load_data('2017Purchase.csv')
    financials_data = load_data('Financials.csv')
    sales_data = load_data('sales.csv')
    
    st.title("ERP System Reporting Tool from Rinos Engineer")
    
    dataset_name = st.sidebar.selectbox(
        "Select Dataset",
        ("Purchases 2017", "Financials", "Sales")
    )
    
    if dataset_name == "Purchases 2017":
        st.write("Purchases 2017 Data:")
        st.dataframe(purchase_data)
    elif dataset_name == "Financials":
        st.write("Financials Data:")
        st.dataframe(financials_data)
    elif dataset_name == "Sales":
        st.write("Sales Data:")
        st.dataframe(sales_data)
    
    if dataset_name == "Sales":
        st.write("Sales Data:")
        st.dataframe(sales_data)
        st.write(sales_data.columns)  # This line will help you confirm column names

    if st.sidebar.checkbox("Show Sales Analysis"):
        st.subheader("Sales Analysis")
        # Make sure the column names used here match exactly with what's in `sales_data.columns`
        if 'Quantity' in sales_data.columns and 'Product' in sales_data.columns:
            sales_summary = sales_data.groupby('Product').agg({'Quantity': 'sum'}).sort_values(by='Quantity', ascending=False)
            st.bar_chart(sales_summary)
        else:
            st.error("Required columns for analysis are missing from the sales data.")


if __name__ == "__main__":
    main()
