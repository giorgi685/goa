# 1)კომენტარის სახით ახსენით რაში გამოიყენება sliceing და რას გადავცემთ მას
# sliceing გამოიყენეა იმისთვის რომ გამოვსახეოთ ინდექსები

# 2)მომხმარებელს შემოატანინეთ თავისი გვარი, შემდეგ შეამოწმეთ თუ მისი გვარი სრულდება "shvili"-ზე, მაშინ დაბეჭდეთ "Hello" / თუ სრუდება "dze"-ზე, მაშინ დაბეჭდეთ "Bye"
surname=input("enter your surname")
if surname=="shvili":
    print("Hello")
elif surname=="dze":
    print("bye")

 # 3)მომხმარებელს შემოატანინეთ წინადადება, შემდეგ შემოატანინეთ იდნექსი და გამოიტანეთ ამ წინადადების ნაწილი დაწყებული 0-დან დამთავრებული მომხმარებლის ინდექსამდე
sentance=input("enter sentance")
index =int(input("enter your number"))
print(sentance[0:index])

 # 4)ცვლადში შეინახეთ თქვენი ასაკი და while ციკლი ამუშავეთ იქამდე სანამ არ მიაღწევს თქვენი (ასაკი * 3)-ს (ყოველ ჯერზე დაბეჭდეთ თქვენი ასაკი და გვერძე მიუწერეთ "year"
age=30
while age < age * 3:
    print(age, "year")

# 5)სიაში შეინახეთ 10 ელემენტი და sliceing-ის მეშვეობით გამოიტანეთ ყველა ლუწ ინდექსზე მდგომი ელემენტი
items=["gamarjoba","Hello","hallo","guttenmorgen","naxvabdis","shexvedramde","bye","rogor xar","ra gqvia","rogor brdzandebit","kargad madloba"]
print(items[::2])

 