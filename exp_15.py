A={1,2,3,4,5,6}
B={4,5,6,3,8,9}
intersection=A&B
union=A|B
Similarity=len(intersection)/len(union)
print(f"A:{A}")
print(f"B:{B}")
print(f"Intersection:{intersection}")
print(f"Union:{union}")
print(f"Jaccard Similarity:{Similarity}")