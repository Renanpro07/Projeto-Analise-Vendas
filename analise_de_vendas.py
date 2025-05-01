import pandas as pd

df = pd.read_excel("analise_vendas.xlsx")
df.head()

df["total"] = df["Valor"] * df["Quantidade"]
total_vendas = df["total"].sum()
print(f"total de vendas no mes: R$ {total_vendas: .2f}")

categoria_top = df.groupby("Categoria")["total"].sum().sort_values(ascending=False)

print("Vendedor")

Vendas_por_vendedor = df.groupby("Vendedor")["total"].sum().sort_values(ascending=False)
print("\nRanking de vendas por Vendedor:")
print(Vendas_por_vendedor)

ticket_medio = df.groupby("Produto")["Valor"].mean().sort_values(ascending=False)

print(ticket_medio)

if total_vendas > 5000:
    print("parabens! Vendas acima da media")
else:
    print("Atenção! Vendas abaixo da meta")