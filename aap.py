import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Load and clean data
df = pd.read_csv("../Datasets/CARS.csv")
df.MSRP = df.MSRP.replace('[$,]', '', regex=True).astype('int64')
df.Invoice = df.Invoice.replace('[$,]', '', regex=True).astype('int64')

st.title("Car Price Explorer")

# Brand selection
brands = sorted(df.Make.unique())
brand = st.selectbox("Select a Brand", brands)

# Filter by brand
brd = df[df.Make == brand]

# Model selection
models = sorted(brd.Type.unique())
model = st.selectbox("Select a Model Type", models)

# Filter by model
mdy = brd[brd.Type == model]

# Plot
st.subheader(f"MSRP of Models from {brand} - {model}")
plt.figure(figsize=(12, 6))
sb.barplot(x=mdy.Model, y=mdy.MSRP, palette='winter')
plt.xticks(rotation=90)
plt.ylabel("MSRP ($)")
plt.xlabel("Model")
plt.tight_layout()

st.pyplot(plt.gcf())
