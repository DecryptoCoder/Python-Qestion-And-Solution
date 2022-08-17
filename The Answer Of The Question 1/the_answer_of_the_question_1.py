import numpy as np

def square_matrix_returner_w_while(x):
    x_sqr=x*x # i find square of user input
    a=np.zeros((x,x)) # creating numpy matrix 2 dimentional x*x matrix 
    t=0 # define  t ,t is our matrix number.
    y,z=0,-1 #define y and z ,y is column start positions and z is row start positions
    oo=0 #define oo ,in my opinion oo is while loop breaker or stopper.
    y_vector=True #define y vector direction down positive(True) , up negative (False) 
    z_vector=True #define z vector direction right positive(True) , left negative (False)
    y_counter=1 #define y counter ,it benefit to says to program how many steps move in column 
    z_counter=0 #define z counter ,it benefit to says to program how many steps move in row
    while t <= x_sqr:
        if z_vector==True:
            for i in range(0,x-z_counter):# program will move throughout row
                #print(y,z,y_counter,z_counter,t,i,"z vector True")
                z+=1
                t+=1
                a[y,z]=t
                #print(a)
                #print(y,z,y_counter,z_counter,t,i,"z vector True procces after")
            z_vector=False # and z vector equals to false becuse program z ,this station position is the rightest and must turn left
            z_counter+=1

        else:

            for i in range(0,x-z_counter):# if z vector equals to false program move left in the row
                #print(y,z,y_counter,z_counter,t,i,"z vector False")
                z-=1
                t+=1
                a[y,z]=t


                #print(a)
                #print(y,z,y_counter,z_counter,t,i,"z vector False procces after")
            z_counter+=1
            z_vector=True #z vector true again

        if y_vector==True: #It's descriptions working principle same z vector just one difference is moving column
            for i in range(0,x-y_counter):
                #print(y,z,y_counter,z_counter,t,i,"y vector True")
                y+=1
                t+=1
                a[y,z]=t


                #print(a)
                #print(y,z,y_counter,z_counter,t,i,"y vector True procces after")
            y_vector=False
            y_counter+=1
        else:

            for i in range(0,x-y_counter):
                #print(y,z,y_counter,z_counter,t,"y vector False")
                y-=1
                t+=1
                a[y,z]=t
                #print(a)


                #print(y,z,y_counter,z_counter,t,"y vector False proccess after")
            y_vector=True
            y_counter+=1

        if oo-1>x_sqr:
            return a
        oo+=1
    return a

def main():
    while True:
        try:

            x=input("what is x")
            a=square_matrix_returner_w_while(int(x))
        except EOFError:
            print("")
            print(a)
            
            break
        except:
            pass
        else:
            print(a)
main()
