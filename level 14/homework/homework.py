# 2) დაწერე პროგრამა, რომელიც ამოწმებს, შეყვანილი რიცხვი 5-სა და 15-ს შორის არის, მაგრამ არა 10-ის ტოლი.
number=int(input("enter your number"))
print(number)
print(15>number>5 and number!=10)
# 3) მომხმარებელმა უნდა შეიყვანოს თავისი ასაკი და სახელი. პროგრამამ უნდა შეამოწმოს, რომ ასაკი 18-ზე მეტია და სახელი 
# იწყება "A"-ზე.
name=input("enter your name")
age=int(input("enter your age"))
print(age>18 and name.startswith ("A"))
# 4) დაწერე პროგრამა, რომელიც ამოწმებს, რიცხვი ლუწია ან 3-ის გამყოფი.
num=int(input("enter your number"))
print(num%2==0 or 3%num==0)
# 5) პროგრამამ უნდა გამოიანგარიშოს, მოცემული ორი რიცხვიდან რომელიმე 100-ის ტოლი ან მასზე მეტია თუ არა.
age=int(input("enter your age: "))
age2=int(input("enter your age: "))
print(age >= 100 or age2 >= 100)

