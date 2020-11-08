

while(True):
    i = int(input("if you want to quit press 1: "))

    if i ==1:
        print("Quiting...")
        break
    else:


        try:
            exam1= int(input("first midterm exam: "))
            exam2= int(input("second midterm exam: "))
            final= int(input("final exam: "))

            mid1percent= int(input("first midterm percent weigh: "))
            mid2percent = int(input("second midterm percent weigh: "))
            finalpercent= int(input("final percent weigh: "))
        except:
            print("Please enter valuable input.")
        else:

            result = (exam1 * mid1percent/100) + (exam2 * mid2percent/100) + (final * finalpercent/100)

            print(f"Your exam result is: {result}")

            if 100> result> 90:
                print("AA")
            elif 89 > result >85:
                print("BA")
            elif 84 > result >80:
                print("BB")
            elif 79 > result >75:
                print("CB")
            elif 74 > result > 65:
                print("CC")
            elif 64 > result > 60:
                print("DC")
            elif 59 > result > 55:
                print("DD")
            elif 54 > result > 50:
                print("FD")
            elif 49 > result > 00:
                print("FF")










