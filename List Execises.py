fruits=["Apple","Banana","Grapes","Grapes","Strawberry"]
print(fruits)
print()

colours=["red","blue","green","yellow","purple"]
print((colours[0]),
      (colours[2]),
      (colours[-1]))
print()

numbers=[10,20,30,40,50]
numbers[1]=25
numbers.append(60)
print(numbers)
print()

names=["Alice","Bob","Charlie","David","Emma"]
subset=names[:3]
print(subset)
print()

num=2
for i in range(1,11):
    print(i**num)

print()

shopping_cart=[]
shopping_cart.append("milk")
shopping_cart.append("bread")
shopping_cart.append("egg")
shopping_cart.extend(["butter","cheese"])
print(shopping_cart)
print()

numbers=[45,22,88,56,92,33]
print("the maximum number in the above list is" ,max(numbers))
print("the minimum the number in the above the list",min(numbers))
print()

letters=["a","b","a","c","b","a","d"]
print(letters.count("a"))
print()

square_of_evens=[x**2 
                 for x in range(11)if x%2==0]
print(square_of_evens)
print()

numbers=[1,2,2,3,4,4,5,6,6,7]
print(list(set(numbers)))
print()