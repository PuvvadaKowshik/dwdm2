import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Load dataset
basket = pd.read_csv("Groceries_dataset.csv")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(basket.head())

# Grouping transactions by Member_number
transactions = basket.groupby(['Member_number'])['itemDescription'].apply(list).tolist()


# Convert transactions into binary format for Apriori
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Applying Apriori Algorithm
frequent_itemsets = apriori(df, min_support=0.02, use_colnames=True)

# Display Frequent Itemsets
print("\nFrequent Itemsets:")
print(frequent_itemsets)

# Extract Association Rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

# Display Association Rules
print("\nAssociation Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# Visualizing Rules using NetworkX
G = nx.DiGraph()
for _, rule in rules.iterrows():
    G.add_edge(tuple(rule['antecedents']), tuple(rule['consequents']), weight=rule['lift'])

plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)
edges = G.edges(data=True)
weights = [data['weight'] for _, _, data in edges]

nx.draw(G, pos, with_labels=True, edge_color=weights, width=2, edge_cmap=plt.cm.Blues)
plt.title("Association Rules Graph")
plt.show()
