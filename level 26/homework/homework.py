# 1)მომხმარებელს შემოატანინეთ რიცხვი და გამოიტანეთ ყველა მის წინ მდგომი რიცხვები მაგ: input:"3" output:(2, 1).
number = int(input("enter your number"))
for i in range(number):
    print(i)

# 2)1'დან 100'ის ჩათვლით გამოიტანეთ ყველა კენტი რიცხვი და დაამატეთ ლისტში, შემდეგ დაბეჭდეთ ეს ლისტი.
for i in range(1,100,2):
    print(i)

# 3)მომხმარებელს შემოატანინეთ რიცხვი და დაადგინეთ ლუწია თუ კენტი ეს რიცხვი.
number = int(input("enter your number"))
print(number%2==0)

# 4)მომხმარებელს შემოატანინეთ რიცხვი და უთხარით მისი grade ამ რიცხვის მიხედვით: (ანუ თუ მაგალითად 90'დან 100'ის ჩათვლით ექნება ქულა გამოუტანეთ "Grade A", თუ 80'დან 89'ის ჩათვლით გამოუტანეთ "Grade B" და ა.შ)
number = int(input("enter your grade"))
if number > 90:
    print("A")
else:
    print("B")

# 5)დაპრინტეთ რიცხვები 16'იდან 57'მდე while loop'ის მეშვეობით
counter = 16 
while counter < 57:
    print(counter)
    counter += 1

# 6)დაპრინტეთ Hello world 5'ჯერ (while loop'ით)
counter = 5
while  counter < 6:
    print("Hello World")
    counter += 1
