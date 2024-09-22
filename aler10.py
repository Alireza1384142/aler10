import time

attempt=0

while True :

    username = input('enter your username :')

    attempt+=1

    if username == ('a123') :


        attemps=0

        while True :

            password = input ('enter your pass :')

            attemps+=1

            if password == ('a123'):

             print('Go forward')

             break
            
            else :
               
               print('try again')
             
            if attemps==3 or attemps==6 :
               
               print('You are timed out')

               time.sleep(5)

               

            if attemps==9:
               
               break
    else:
       
       print(' Wrong username. Try again')

       time.sleep(3)

    if attempt == 5 :
       
       print('you are timed out')

       time.sleep(3)

       attempt=0

   