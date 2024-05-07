print("\n                   WELCOME TO TOPS QUIZ GAMING CHALLENGE")

print("\n                   Select your role : \n")

print("                              -> Quiz Master    (Press 1)")
print("                              -> Quiz cracker   (Press 2)")



while True:
    
    choice=int(input("\n Enter your role : "))

    if choice == 1:

        print("\n                        WELCOME MASTER ")
        print("          SHAKE YOUR BRAIN AND ADD SOME CHALLENGING QUESTIONS...")

        print("\n                              Menu")
        print("                      Press 1 for add questions")
        print("                      Press 2 for view questions")
        print("                      Press 3 for delete questions")
        print("                      Press 4 for exit")

        choice=int(input("\n Which operation you want to perform : "))

        if choice == 1:
            print(" Add questions : \n")

            q = input("Enter Questions: ")
            op_a = input("Enter Option A: ")
            op_b = input("Enter Option B: ")
            ans = input("Enter Right Answer: ")

            d = {"q":q,
                 "Option":
                 {
                     "A":op_a,
                     "B":op_b,
                 },
                 "ans":ans}

            print("\n",d)
            print("\n Question Added Successfully!")


        elif choice == 2:
            print(" View questions")

            for key, value in d.items():
                print(key, ":", value)


        elif choice == 3:
            print(" Delete questions")

        
        elif choice == 4:
            print(" Updation Complete")
            break

        else:
            print(" Wrong choice")


        

    elif choice == 2:
        print("                  WELCOME QUIZ CRACKER \n")

        break

    else:
        print(" Wrong Choice")
        break
    
