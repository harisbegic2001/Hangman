import random as r  
lista_imena = ["Haris", "Asima", "Tarik", "Dževad"]  
ime = lista_imena[r.randint(0,len(lista_imena)-1)].lower()  
ime_lista = []  
kodirana_lista = []  
brojac = 6  

for i in range (0, len(ime)):  
    kodirana_lista.append("_")  
    ime_lista.append(ime[i])  
    
    
while brojac != 0:  
    vase_slovo = input("Unesite slovo za koje mislite da se nalazi: ")  
    if vase_slovo not in ime:  
        brojac -= 1  
    else:  
        for i in range(0, len(ime)):  
            if ime[i] == vase_slovo: 
                kodirana_lista[i] = vase_slovo 

    print(kodirana_lista)  
    if kodirana_lista == ime_lista:  
        print("Uspješno ste riješili ovaj kviz!!")  
        break  
    if brojac == 0:  
        print("Niste uspjeli :(") 





















