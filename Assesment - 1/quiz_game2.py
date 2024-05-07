def display_menu():

    print("Welcome To Tops Quiz Gaming Challange")
    print("-------------------------------------------------------------\n")
    print("\nSelect Your Role : ")

    print("\n1.Quiz Master")
    print("\n2.Quiz Craker")
    role=int(input("\nEnter Your Role : "))
    if role==1:
        print("\nWelcome Master")
        print("\nShake Your Brain And Add Some Challanging Questions...")
        print("-------------------------------------------------------------\n")
        while True:
            print("*****Display Menu****")
            print("\n1.Add Questions")
            print("\n2.View Questions")
            print("\n3.Delete Questions")
            print("\n4.Exit")

            choice=int(input("Which Operation You Want To Perform : "))
            if choice==1:

                #Add Question
                
                 question = input("Enter the question: ")
                
                 
                 option_a = input("Enter option A: ")
                 option_b = input("Enter option B: ")
                 answer=input("Enter Correct Answer : ")
                 d1={"question":question,
                     "option":{
                         "A":option_a,
                         "B":option_b},
                     "answer":answer}

                 {d1:{"question":question,
                     "option":{
                         "A":option_a,
                         "B":option_b},
                     "answer":answer}}







                 
                 
                
                
                 print("Question add  successfully!!!")

            elif choice==2:

                #view Question

                for key, value in d1.items():
                    print(key," : ",value)
           
                
                                  
            

        









display_menu()
