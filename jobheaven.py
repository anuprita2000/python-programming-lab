from easygui import*
import sys

while 1:
 msgbox("welcome to jobheaven")
 msg="choose the type"
 title="types"
 choices=["part time","annual"]
 choice=choicebox(msg,title,choices)
 msgbox("you choice"+str(choice))
 
 if choice=="part time job":
  msg="choose ur age grp"
  title="age"
  choices=["above18","15-18yrs"]
  choice=choicebox(msg,title,choices)
  msgbox("you choose"+str(choice))
  
  if choice=="above 18":
   msg="choose ur job"
   title="job places"
   choices=["petrol station","dry cleaning","school job"]
   choice= choicebox(msg,title,choice)
   msgbox("you choose"+str(choice))
   
   if choice=="petrol station":
    msg="choose place"
    title="address"
    choices=["camp road=rs100","gandhisquare=80rs"]
    choice=choicebox(msg,title,choice)
    msgbox("you choose:"+str(choice))
   
   elif choice=="dry cleaning shop":
    msg="choose shop"
    title="dry cleaning shops"
    choices=["jandi 50/hr","jun rs40/hr"]
    choice=choicebox(msg,title,choice)
    msgbox("you choose"+str(choice)
  
   elif choice=="school job":
    msg="choose school"
    title="schools available"
    choices=["gov school 40rs/hr","modern schl 50rs/hr"]
    choice=choicebox(msg,title,choice)
    msgbox("you choose"+str(choice))
 
  elif choice=="15-18yrs":
   msg="choose ur workplace"
   title="places"
   choices=["clothes shop","book store","city library"]
   choice=choicebox(msg,tigle,choice)
   msgbox("you chose"+str(choice))
   
   if choice=="clothes shop":
    msg="available shops are"
    title="choose shop"
    choices=["a1 rs100/hr","a2 rs110/hr"]
    msgbox("you chose:"+str(choice))
   
   elif choice=="book store":
    msg="available book stores"
    title="choose ur store"
    choices=["crossword-50/hr","second world 55/hr"]
    msgbox("you chose:"+str(choice))
   
   elif choice=="city library"
    msg="choose ur job"
    title="positions available"
    choices=["organiser 80/hr","distribution"]
    choice=choicebox(msg,title,choice)
    msgbox("uchoose"+str(choice))
    
elif choice =="annual job"
 msg="choose qualification"
 title="qualification"
 choices=["art graduate","engg graduate","10-12th pass"]
 choice=choicebox(msg,title,choice)

 if choice=="arts graduate"
  msg="choose ur job"
  title="jobs available"
  choices=["teachers","counsellor"]
  choice=choicebox(msg,title,choice)
 elif choice=="engg graduate"
  msg="choose ur job"
  title="available choices"
  choices=["infosys 987654321","tata 45678942"]
  choice=choicebox(msg,title,choice)
 elif choice=="10/12 pass"
  msg="choose ur choice"
  title="select one"
  choices=["v1=camp salesman 500/day","v2=gandhi sq 600/day"]
  msgbox("you choose"+str(choice))