

# for i in range (1,10,1):
#     for j in range(i,8):
#         print("*", end="")
#     print()    
# for i in range(1,10,1):
#       for a in range(1,i,):
#           print("*", end="")
#       print()      


# def main():
#     empty
def inputt():
   
   
   x = (input("Choose rock ,paper or scissors :"))
   y = (input("Now other person chooses rock paper or scissors : "))  
   return x,y  


def processing(a,b):    
    if (a == 'rock'):
        if(b == 'rock'):
         print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
         print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
         print('ITS A TIE')
        elif(b == 'scissors'):

            print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
            print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
            print('PLAYER 1 WON')
        elif(b == 'paper'):
         print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
         print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
         print('PLAYER 2 WINS')
        else:
             print('INVALID INPUT')
    elif(a == 'scissors'):
        if(b == 'rock'):
               print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
               print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
               print('PLAYER 2 WINS')
        elif(b == 'scissors' ):
         print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
         print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
         print("ITS A TIE")
        elif(b == 'paper'):
            print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
            print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
            print('PLAYER 1 WINS')
        else:
         print('INVALID INPUT')    
    elif(a == 'paper'):
     if(b == 'rock'):
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print('PLAYER 1 WINS')
     elif(b == 'scissors'):
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print('PLAYER 2 WINS')
     elif(b == 'paper'):
         print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
         print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
         print('ITS A TIE')
    else:
        print("INVALID INPUT") 


a, b = inputt()     
processing(a, b)
        

    
        
            

        


            
        
          
   
        






    

      