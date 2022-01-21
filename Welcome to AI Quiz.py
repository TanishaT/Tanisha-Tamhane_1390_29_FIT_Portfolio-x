print ('Welcome to AI Quiz ')
answer=input ('Are you ready to play the Quiz ? (yes/no) :')
score=0
print("\nYour current score: ", score)
total_questions=3
if answer=='yes':
print('\nQuestion 1: What is the long form of AI?')
ans=input('Answer: ')
if ans=='ARTIFICIAL INTELLIGENCE' or ans=='Artificial Intelligence':
score=score+1
print ('\ncorrect')
print('\nNew score is',score)
print ('\nWrong Answer :(')
print('\nQuestion 2: Which programming language is used to make AI projects? ')
a=input('Answer: ')
if a=='python':
score=score+1
print ('\ncorrect')
print('\nNew score is',score)
print ('\nWrong Answer :(')
print('\nQuestion 3: Who is the inventor of AI field?')
b=input('Answer: ')
if b=='John McCarthy':
score=score+1
print ('\ncorrect')
print('\nNew score is',score)
print ('\nWrong Answer :(')
print ('Thankyou for Playing this small quiz game',score)
mark= (score/total_questions)*100
print ('Percentage obtained: ',mark)
print ('BYE!')
print ('Bye!')
