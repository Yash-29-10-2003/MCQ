#Importing class Questions from mcqquestions.py 
from mcqquestions import Question

#Array of questions
questions_array = [
    "\n\nWhat is the latest nvidia geforce gpu lineup generation as of 2020 ? \n(A) The 5000 series \n(B) The 3000 series \n(C) The i9 series \n(D) The 11th generation \n\n",
    "\n\nWhich of the following kernels does android run on ? \n(A) NT kernel \n(B) Darwin kernel \n(C) Linux kernel \n(D) Tizen \n\n",
    "\n\nWhich of the following is commonly referred to as a 2k Display ? \n(A) QHD \n(B) FHD \n(C) UHD \n(D) HD \n\n"
]

#Pre defining some variables
i = 0
score = 0
answer_user = ""
total = len(questions_array)

#Starting the mcq via a loop

questions = [
    Question(questions_array[0] , "Bb"),
    Question(questions_array[1] , "Cc"),
    Question(questions_array[2] , "Aa")
]

for i in range(total):
    print("Question ", i+1 ,":")
    print(questions[i].question)
    answer_user = input("\nAnswer in (A/B/C/D) : ")
    if(answer_user in questions[i].answer):
        score = score + 1
        i += 1
    else:
        i += 1

print("\n\n\n\n\n\n\n\n\nThe test is complete.")
print("Your Score : " , score , "/" , total)