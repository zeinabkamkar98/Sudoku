import random
import copy

###################################################################################################################################
#baray sort hast dige hich estefade nadare
def myFunc(e):
  return e['fit']

###################################################################################################################################

def make_population():
    
    global population
    global summ

    for i in range(100):
        
        t=initial()
        f=fitness(t)
        
        #save best initial
        if f>best["fit"]:
            best["table"]=copy.deepcopy(t)
    
        population.append({"table":copy.deepcopy(t),"fit":f})
        

###################################################################################################################################

def initial ():
#baray initial kardan :
#ghanoon square kochiktar hatman hefz mishe va dige lazem nis to fitness check beshan
#va saye mishe ba eshterak gereftan row va columns ham yekam behtar bashan vali baiad check beshan

    global table
    
    new_table=copy.deepcopy(table)
    
    numbers={"rows":[
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9]
                    ],
            "columns":[
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9]
                    ],
            "squares":[
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9]
                    ]
            }
    
    #remove numbers already exist in tabel (remove them from our selection list for initalize table)
    for i in range(9):
        for j in range(9):
            if table[i][j]!=0:
                numbers["rows"][i].remove(table[i][j])#related row
                numbers["columns"][j].remove(table[i][j])#related column
                numbers["squares"][(int(i/3)*3)+(int(j/3))].remove(table[i][j])#related square

    #fill tabel
    for i in range(9):
        for j in range(9):
            
            #if it's blank  
            if table[i][j]==0:  
                
                #common numbers in related row and related square
                common=[value for value in numbers["rows"][i] if value in numbers["squares"][(int(i/3)*3)+(int(j/3))]]
                #common numbers in related row and related square and related columns
                common2=[value for value in numbers["columns"][j] if value in common]
                
                # ehteml inke betoonim number moshtarak bine seta list ro pida koim kame vali olaviat avalemone.
                if len(common2)!=0:
                    #select random number from common2 list
                    element=random.choice(common2)
                    new_table[i][j]=element 
                    
                    #remove selected number from selection lists
                    numbers["squares"][(int(i/3)*3)+(int(j/3))].remove(element) 
                    numbers["rows"][i].remove(element)
                    numbers["columns"][j].remove(element)
               
                    
                elif len(common)!=0:
                    element=random.choice(common)
                    new_table[i][j]=element 
                    
                    numbers["squares"][(int(i/3)*3)+(int(j/3))].remove(element) 
                    numbers["rows"][i].remove(element)
                    
                #age hich addad moshtaraki nabood az squere list ye addad random mizarim ke ghanoon 
                #square be ham nakhore
                else:
                    element=random.choice(numbers["squares"][(int(i/3)*3)+(int(j/3))])
                    new_table[i][j]=element
                    
                    numbers["squares"][(int(i/3)*3)+(int(j/3))].remove(element)
                 
    return copy.deepcopy(new_table)
                
###################################################################################################################################

def fitness(array):
    
    numbers={"rows":[
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9]
                    ],
            "columns":[
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9]
                    ]
            }    

    fit=0
    #initial karadan va har taghiri ke ijad mishe be in tavajooh dare 
    #ke ghanoon square koocheck kharab nashe pas niazi niz check beshe
    
    #fitness ro in dar nazar migirim ke chenta az addaie ke baiad to rows and columns gharar begire 
    # gharargerefte 
    # solution => fit=162
    for i in range(9):
        for j in range(9):  
            
            if array[i][j] in numbers["rows"][i]:
                numbers["rows"][i].remove(array[i][j])
                fit=fit+1
                
                
            if array[i][j] in numbers["columns"][j]:
                numbers["columns"][j].remove(array[i][j])
                fit=fit+1
    
    return fit

###################################################################################################################################

def solve():
    
    global population
    global best
    
    generation_num=0
    
    #bara hazf kardan javab hai bad 
    #bound mige 25 ta aval haz beshan
    #vali bad band ro kamtar mikoim chon harchi berim jelotar (generation) javab
    # ham behtaran va behtare negaheshon darim ta betonim halata bettar motefavet tari besazim
    bound=25
    
    #ta zamani ke solution peida beshe edame mide
    while True:
        
        generation_num=generation_num+1
        
        print("best fitness:",best["fit"])
        print("generation:",generation_num)      
        
        #aval population ro sort mikonim ba tavajo be fitness ona bad bad ha hazf mishan
        population.sort(key=myFunc)       
        population=population[bound:100]   
        size=100-bound
        
        if bound>=5:
            bound=bound-5       
        
        #check for solution                   
        if best["fit"]==162:
            print("solution:")
            for b in best["table"]:
                print(b)
            break

        #new population list
        new_pop=[] 
        #reapeat list bara jelogiri az gharar gereftan javab tekrari to new population
        reapeat=[]
        
        #tedad table ezafe shode be new population
        number_added=0   
        
        #ta zamani ke 80 table jadid be new populatin ezafe kone edame dare ba ravesh crossover
        while True:
            
            parent1=copy.deepcopy(population[random.choice(range(size))])
            parent2=copy.deepcopy(population[random.choice(range(size))])

            child=crossover(parent1["table"], parent2["table"])            

            #convert child tabel to string 
            c=""
            for i in child["table"]:
                list1=i
                c=c+"".join(str(e) for e in list1)
                
            #check mikone ke on string to reapet list has ya na age nabood be new population ezafe mishe
            if c not in reapeat:
                new_pop.append(copy.deepcopy(child))
                number_added=number_added+1
                reapeat.append(c)
               
            #check if child is better than best 
            if child["fit"]>best["fit"]:
                best=copy.deepcopy(child)
            
            if number_added==80:
                break
            
        # 20 ta tabel dige ezafe mishe ba ravesh mutation 
        for i in range(10):
            
            m=copy.deepcopy(population[random.choice(range(size))])
            mutation_row(m["table"])
            m["fit"]=fitness(m["table"])
            new_pop.append(copy.deepcopy(m))
            
            if m["fit"]>best["fit"]:
                best=copy.deepcopy(m)
            
        for i in range(10):
            
            m=copy.deepcopy(population[random.choice(range(size))])
            mutation_column(m["table"])
            m["fit"]=fitness(m["table"])
            new_pop.append(copy.deepcopy(m))
            
            if m["fit"]>best["fit"]:
                best=copy.deepcopy(m)
            
        #list jadid ro mizarim to population
        population=copy.deepcopy(new_pop)

    

###################################################################################################################################

def crossover(arr1,arr2):
    
    #to initail kardan ghanoon square reaiat shod
    #va tajae ke shod row ham reat shod(common list)
    #pas ye jori cross over mikonim ke nazm be ham nakhore (row va square)
    
    #5 ta halate mitone pish biad barai takib kardan be sorat random yekish ro entekhab mikonim
    l=[1,2,3,4,5]
    selected=random.choice(l)

    if selected==1:
        row=range(0,3)
    elif selected==2:
        row=range(3,6)
    elif selected==3:
        row=range(6,9)
    elif selected==4:
        row=range(0,6)
    elif selected==5:
        row=range(3,9)
    
    #row ha enetkhab shode ro switch mikonim
    for a in row:
        temp=copy.deepcopy(arr1[a])
        arr1[a]=copy.deepcopy(arr2[a])
        arr2[a]=temp 
    
    #fitness 2 ta child ro entekhab mikonim va behtarineshon ro barmigardonim
    f1=fitness(arr1)
    f2=fitness(arr2)
    
    if f1>f2:
        return {"table":copy.deepcopy(arr1),"fit":f1}
    
    return {"table":copy.deepcopy(arr2),"fit":f2}

###################################################################################################################################

def mutation_row (arr):
    
    #be sorat random ye row enekhab mikonim
    row=random.choice(range(9))
    
    #row entekhab shode be 3 ta square marboot has yeki az squire ha entekhab mishe
    j=random.choice([0,3,6])
    
    #tedad bland ha on radif to on square
    zero=0
    for i in range(3):
        if table[row][j+i]==0:
            zero=zero+1
    
    if zero==0 or zero==1:
        return
    
    elif zero==2:
    
        if table[row][j]==0:
            if table[row][j+1]==0:
                arr[row][j],arr[row][j+1]=arr[row][j+1],arr[row][j]
            else:
                arr[row][j],arr[row][j+2]=arr[row][j+2],arr[row][j]
    
        else:
            if table[row][j+2]==0:
                arr[row][j+1],arr[row][j+2]=arr[row][j+2],arr[row][j+1]  
    
    #if we have 3 blank we have 3 switch 
    #be sorat random yekishon ro anjam midim
    else:
        t=[0,1,2]
        n1=random.choice(t)
        t.remove(n1)
        n2=random.choice(t)
        arr[row][j+n1],arr[row][j+n2]=arr[row][j+n2],arr[row][j+n1]
              
###################################################################################################################################

def mutation_column (arr):
    
    col=random.choice(range(9))
    
    j=random.choice([0,3,6])
    
    zero=0
    for i in range(3):
        if table[j+i][col]==0:
            zero=zero+1
    
    if zero==0 or zero==1:
        return
    
    elif zero==2:
    
        if table[j][col]==0:
            if table[j+1][col]==0:
                arr[j][col],arr[j+1][col]=arr[j+1][col],arr[j][col]
            else:
                arr[j][col],arr[j+2][col]=arr[j+2][col],arr[j][col]
    
        else:
            arr[j+2][col],arr[j+1][col]=arr[j+1][col],arr[j+2][col] 
    
    else:
        t=[0,1,2]
        n1=random.choice(t)
        t.remove(n1)
        n2=random.choice(t)
        arr[j+n2][col],arr[j+n1][col]=arr[j+n1][col],arr[j+n2][col]
                
###################################################################################################################################

table=[[5,3,0,0,7,0,0,0,0],
       [6,0,0,1,9,5,0,0,0],
       [0,9,8,0,0,0,0,6,0],
       
       [8,0,0,0,6,0,0,0,3],
       [4,0,0,8,0,3,0,0,1],
       [7,0,0,0,2,0,0,0,6],
       
       [0,6,0,0,0,0,2,8,0],
       [0,0,0,4,1,9,0,0,5],
       [0,0,0,0,8,0,0,7,9]]

population=[]
best={"table":[],"fit":0}

make_population()
solve()
#best fitness is 162 . solution has 162 fitness score