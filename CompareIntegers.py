def largest(num1, num2, num3):
    return max(num1, num2, num3)


def smallest(num1, num2, num3):
    return min(num1, num2, num3)


while True:
    try:
        userInputNum1 = int(input('Enter 1st number :'))
        userInputNum2 = int(input('Enter 2nd number :'))
        userInputNum3 = int(input('Enter 3rd number :'))
        break
    except:
        print('Must enter integer only')

print('The largest number is: ' + str(largest(userInputNum1, userInputNum2, userInputNum3)))
print('The smallest number is: ' + str(smallest(userInputNum1, userInputNum2, userInputNum3)))
