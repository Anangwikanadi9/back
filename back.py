import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# no 1
st.title("Visualisasi Nilai Pembayaran dan Jumlah Transaksi berdasarkan Jenis Pembayaran")

payment_data = {
    'payment_type': ['boleto', 'credit_card', 'debit_card', 'voucher'],
    'payment_value': [2869361.27, 12542084.19, 217989.79, 379436.87],
    'payment_count': [19784, 76795, 1529, 5769]
}

df = pd.DataFrame(payment_data)

# Filtering - pilih jenis pembayaran (All atau per item)
selected_payment_type = st.selectbox("Pilih Jenis Pembayaran", ['All'] + list(df['payment_type'].unique()))

# Filter data berdasarkan pilihan
if selected_payment_type == 'All':
    filtered_df = df
else:
    filtered_df = df[df['payment_type'] == selected_payment_type]

fig, ax1 = plt.subplots(figsize=(10, 6))

sns.barplot(x='payment_type', y='payment_value', data=filtered_df, palette='Blues', ax=ax1)
ax1.set_ylabel('Total Payment Value (IDR)')
ax1.set_xlabel('Payment Type')
ax1.set_title('Comparison of Payment Value and Transaction Count by Payment Type')

ax2 = ax1.twinx()
sns.lineplot(x='payment_type', y='payment_count', data=filtered_df, marker='o', color='red', ax=ax2)
ax2.set_ylabel('Transaction Count')

ax1.legend(['Payment Value'], loc='upper left')
ax2.legend(['Transaction Count'], loc='upper right')

st.pyplot(fig)

# no 2
st.title("Visualisasi Total Berat Produk Berdasarkan Kategori")

data = {
    'product_category_name': ['Unknown', 'agro_industria_e_comercio', 'alimentos', 'alimentos_bebidas', 
                              'artes', 'sinalizacao_e_seguranca', 'tablets_impressao_imagem', 
                              'telefonia', 'telefonia_fixa', 'utilidades_domesticas'],
    'product_weight_g': [610, 74, 82, 104, 55, 93, 9, 1134, 116, 2335]
}
products_df = pd.DataFrame(data)

grouped_df = products_df.groupby(by="product_category_name").agg({
    "product_weight_g": "sum"
})

grouped_df_sorted = grouped_df.sort_values(by="product_weight_g", ascending=False)

# Filtering - pilih kategori produk (All atau per item)
selected_category = st.selectbox("Pilih Kategori Produk", ['All'] + list(products_df['product_category_name'].unique()))

# Filter data berdasarkan pilihan
if selected_category == 'All':
    filtered_grouped_df = grouped_df_sorted
else:
    filtered_grouped_df = grouped_df_sorted[grouped_df_sorted.index == selected_category]

st.write("### Total Berat Produk Berdasarkan Kategori")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=filtered_grouped_df.index, y=filtered_grouped_df['product_weight_g'], palette="viridis", ax=ax)
ax.set_title('Total Berat Produk Berdasarkan Kategori')
ax.set_xlabel('Kategori Produk')
ax.set_ylabel('Total Berat (gram)')
plt.xticks(rotation=90)

fig.tight_layout()  # To adjust layout and avoid label overlap

st.pyplot(fig)
