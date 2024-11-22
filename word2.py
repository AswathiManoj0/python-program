string=input("enter a string")
word=string.lower().split()
word_count = count(word)
print("word occuurence")
for word,count in word_count.items():
 print(f"'{word}':{count}")
