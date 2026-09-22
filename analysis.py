import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

df = pd.read_csv('price_comparison.csv')

print(df)
print("\nMEAN PRICES:")
print(df[['Kirana_Price','DMart_Price','Blinkit_Price']].mean())

# ANOVA Test
f_stat, p_val = stats.f_oneway(df['Kirana_Price'], df['DMart_Price'], df['Blinkit_Price'])
print(f"\nANOVA: F={f_stat:.2f}, p={p_val:.4f}")

# Bar Chart
x = np.arange(len(df))
width = 0.25
plt.figure(figsize=(10,5))
plt.bar(x - width, df['Kirana_Price'], width, label='Kirana')
plt.bar(x, df['DMart_Price'], width, label='DMart')
plt.bar(x + width, df['Blinkit_Price'], width, label='Blinkit')
plt.xticks(x, df['Item'], rotation=45, ha='right')
plt.ylabel('Price (Rs)')
plt.title('Price War: Kirana vs DMart vs Blinkit (Pune)')
plt.legend()
plt.tight_layout()
plt.savefig('price_barchart.png', dpi=200)
plt.show()

# Boxplot
plt.figure(figsize=(6,4))
plt.boxplot([df['Kirana_Price'], df['DMart_Price'], df['Blinkit_Price']], labels=['Kirana','DMart','Blinkit'])
plt.title('Price Distribution Comparison')
plt.ylabel('Price Rs')
plt.tight_layout()
plt.savefig('price_boxplot.png', dpi=200)
plt.show()
