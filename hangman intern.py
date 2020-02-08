digit_num = int(input("Please enter 12 digit numbers: "))

hangman_dig=list()
score_num = 0
while len(str(digit_num))!= 12:
    print("You can enter only 12 digits")
    digit_num = int(input("Please enter 12 digit numbers: "))

for j in range(12):
    hangman_dig.append('_')
print(" ".join(hangman_dig))

for i in range (5):
    ans_dig= int(input("Guess the number: "))
    if ans_dig not in range(0,10):
        ans_dig= int(input("Your number can only be 0-9! Try again: "))
    elif str(ans_dig) not in str(digit_num):
        hangman_dig.append(str(ans_dig))
    
    for j in range(12):
        if str(ans_dig) == str(digit_num)[j]:
            hangman_dig[j] = str(ans_dig)
            score_num += 1
        
    print (" ".join(hangman_dig))
print (f"Score: {score_num}")


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      



