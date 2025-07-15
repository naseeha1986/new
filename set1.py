my_set={10,20,30,40,50}
print("My set is ",my_set)
my_set.add(60)
print("\nSet after adding a element",my_set)
my_set.update({70,80,90,100})
print("\nSet after updating elements",my_set)
my_list=list(my_set)
print(f"\nIs 100 exist in set {my_set}\n,{100 in my_list}")
print("\n\nLength of my set is :", len(my_set))
