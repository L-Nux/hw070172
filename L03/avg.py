#Exercise Ch2 - 3 (Zelle 2017, Python Programming: An Introduction to Computer Science)


# A simple program to average two exam scores

def main():
    print("This program computes the average of three exam scores: ")
    score1, score2, score3 = eval(input("Please enter three scores separated by a comma: "))
    avg = (score1 + score2 + score3) /2
    print("The average of the scores is: ", avg)

main()