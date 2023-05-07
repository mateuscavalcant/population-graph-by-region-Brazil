import matplotlib.pyplot as plt

x = ["Sudeste", "Nordeste", "Sul", "Norte", "Centro-Oeste"]
y = [89.7, 55.1, 30.1, 18.6, 17.6]

# Definindo uma paleta de cores mais adequada para gráficos de barras
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Criando o gráfico de barras
fig, ax = plt.subplots()
ax.bar(x, y, color=colors)

# Adicionando um título ao gráfico
ax.set_title("População de habitantes por região (milhões) - Brasil")

# Definindo o limite do eixo y
ax.set_ylim([0, 100])

# Adicionando um label com o valor de cada barra acima dela
for i, v in enumerate(y):
    ax.text(i, v + 1, str(v), ha='center', fontsize=10)

plt.text(0.5, -0.1, "Fonte: IBGE - Estimativas populacionais de 2021", ha='center', transform=ax.transAxes, fontsize=8)

# Mostrando o gráfico
plt.show()
