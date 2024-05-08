print("                            Welcome To Tops Quiz Gaming Challange\n")
print("                            Select Your Role : \n")

print("                                   -> 1.Quiz Master (Press 1)")
print("                                   -> 2.Quiz Craker (Press 2)")

role = int(input("\nEnter Your Role : "))
    
if role==1:
    print("                               Welcome Master")
    print("             Shake Your Brain And Add Some Challanging Questions..")
    print("         --------------------------------------------------------------\n")
    d1={}
    while True:
        print("                                   Menu")
        print("                           Press 1 for Add Questions")
        print("                           Press 2 for View Questions")
        print("                           Press 3 for Delete Questions")
        print("                           Press 4 for Exit\n")
        print("\n")
            
        choice = int(input("Which Operation You Want To Perform : "))
        print("\n")

        if choice==1:
                
            que = input("\nEnter the question: ")         
            op_a = input("Enter op 1: ")
            op_b = input("Enter op 2: ")
            ans =input("Enter right answer : ")

            d1[que]={"A":op_a,"B":op_b,"Answer":ans}

            print("\nQuestion Added Successfully!")
            print("\n")

        elif choice==2:

            if len(d1) > 0:
                for key,value in d1.items():
                    print("Here is the Question: \n")
                    print(key, " : ", value)
                    print("\n")
            else:
                print("No questions available to view.")
                print("\n")

        elif choice==3:
                
            if len(d1) > 0:
                key = input("Enter the question to delete: ")

                if key in d1:
                    d1.pop(key)
                    print("Question deleted successfully!")
                    print("\n")
                else:
                    print("Question not found!")
                    print("\n")
            else:
                print("No questions available to delete.")
                print("\n")

        elif choice==4:
                
            print("Master Exit Successfully :-)")
            break


