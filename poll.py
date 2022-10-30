print(" " * 26, "^_^ WELCOME IN ELECTION ^_^")
print()
B = input("Enter 1st Candidate:")
T = input("Enter 2nd Candidate:")
print()
print(""""Here is your Precious VOTE .....""")
print("    you have to give VOTE between", B, "&", T)
print("Press s to stop the vote")
print()
n = int(input("Enter no.of participant:"))
print()
print("""Press Enter To Start The Votting Stytem" """)
a = input()
main_list = []
vote_list = []
# id_list=[]

for g in range(n):
    user = input("Enter your VOTER ID : ")  # (blank id tao count hoi jabe)
    if user == "s":
        break
    for h in range(1, 2):
        main_list.append(user)
        s = main_list.count(user)
        if s != 1:
            print("""This is Not Your VOTER ID
                     already voted!!!!
Please chcck your ID! Sorry. """)
            break
        print("*" * 50)
        print("(To give your VOTE to", B, "press A or a)")
        print("(to give your VOTE to", T, "press B or b)")
        print("*" * 50)
        user_vote = input("Enter Your Precious VOTE :")
        if user_vote == "A" or user_vote == "a":
            print("        Thanks for giveing voting", "☺", B)
        elif user_vote == "B" or user_vote == "b":
            print("        Thanks for givieng voting", "☺", T)
        else:
            print("You should enter a vaild VOTE for giving Vote, Sorry!!!")
        print("Your Voting session is over !!!")
        print()
        print()

        vote_list.append(user_vote)

count_1 = vote_list.count("A")
count_2 = vote_list.count("a")
count_3 = vote_list.count("b")
count_4 = vote_list.count("B")

result_1 = (count_1 + count_2)
result_2 = (count_3 + count_4)
# final_result=result_1+result_2

vote_length = count_1 + count_2 + count_3 + count_4

if result_1 > result_2:
    z = (result_1 / vote_length) * 100
    print(B, "has won the election with", z, "% of VOTES")
elif result_2 > result_1:
    w = (result_2 / vote_length) * 100
    print(T, "has won the election with", w, "% of VOTES")
elif result_1 == result_2:
    print("both have equal no. of vote with each 50% ")

print()
print("voting session is over....(●'◡'●) ")

print("original main_list :" + str(main_list))
print("original vote_list :" + str(vote_list))

res = {}
for key in main_list:
    for value in vote_list:
        res[key] = value
        vote_list.remove(value)
        break
abc = ("net dictionary:" + str(res))

import json

print(res)
dic2 = json.dumps(res, indent=n)
print(dic2)

nibu = open("arkanibu.txt", 'a')
nibu.write(dic2)
nibu.close()











