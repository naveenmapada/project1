import random
movies={"salaar","saaho","geetha govindam","sankranthi","sanivaram"}
def create_question(picked_movie):
    n=len(picked_movie)
    a=list(picked_movie)
    temp=[]
    for i in range(n):
        if(a[i]==' '):
            temp.append(' ')
        else:
            temp.append('*')
    dn=''.join(str(x) for x in temp)
    return dn
def is_present(letter,picked_movie):
    c=picked_movie.count(letter)
    if(c==0):
        return False
    else:
        return True
def unlock(modified_qn,picked_movie,letter):
    ref=list(picked_movie)
    qn_list=list(modified_qn)
    temp=[]
    n=len(picked_movie)
    for i in range(n):
        if(ref[i]==' ' or ref[i]==letter):
            temp.append(ref[i])
        else:
            if(qn_list[i]=='*'):
               temp.append('*')
            else:
                temp.append(ref[i])
    sn=''.join(str(x) for x in temp)
    return sn        
def play():
    p1name=input("please  enter player 1 name")
    p2name=input("please enter player 2 name")
    p1p=0
    p2p=0
    turn=0
    willing=True
    while(willing):
        if(turn%2==0):
            print(p1name,"your turn")
            picked_movie=random.choice(list(movies))
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while(not_said):
                letter=input("Your answer")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("press 1 to guess the movie  or 2 to guess the letter"))
                    if(d==1):
                        ans=input("guess the movie name")
                        if(ans==picked_movie):
                            p1p=p1p+1
                            print("correct")
                            not_said=False
                            print("your score is",p1p)
                        else:
                           print("wrong answer try it again")
                else:
                    print(letter,"letter not found")
            c=int(input("press 1 to continue the game or 0 to quit the game"))
            if(c==0):
                print(p1name,"your score is",p1p)
                print(p2name,"your name is",p2p)
                print("Thanks for playing")
                print("Have a nice day")
                willing=False
    else:
        print(p2name,"your turn")
        picked_movie=random.choice(movies)
        qn=create_question(picked_movie)
        modified_qn=qn
        not_said=True
        while(not_said):
            letter=input("Your answer")
            if(is_present(letter,picked_movie)):
                modified_qn=unlock(modified_qn,picked_movie,letter)
                d=int(input("press 1 to guess the movie or 2 to guess the letter"))
                if(d==2):
                    ans=input("guess the movie name")
                    if(ans==picked_movie):
                        p2p=p2p+1
                        print("correct")
                        not_said=False
                        print("your score is",p2p)
                    else:
                       print("wrong answer try it again")
            else:
                print(letter,"letter not found")
        c=int(input("press 1 to continue the game or 0 to quit the game"))
        if(c==0):
            print(p1name,"your score is",p1p)
            print(p2name,"your name is",p2p)
            print("Thanks for playing")
            print("Have a nice day")
            willing=False
    turn=turn+1 
play()

           
                            
                            
                
