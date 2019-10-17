##Input
#12
#insert 0 5
#insert 1 10
#insert 0 6
#print
#remove 6
#append 9
#append 1
#sort
#print
#pop
#reverse
#print

##Output
#[6, 5, 10]
#[1, 5, 9, 10]
#[9, 5, 1]


#######Code

def get_command():
    command = input()
    try:
        if len(command.split()) == 3:
            order, position, element = command.split()
            return order, position, element

        else:
            order, element = command.split()
            position = 'null'
            return order,position,element

    except:
        order, position, element = command, 'null', 'null'
        return order,position,element


#Funções específicas
def insert(lista, position, element):
    if len(lista) == 0:
        lista.append(element)
    else:
        lista.insert(position, element)

    return lista
 

def remove(lista, element):
    lista.remove(element)

    return lista

def append(lista, element):
    return lista.append(element)

def sort_(lista):
    lista.sort()
    return lista

def pop(lista):
    return lista.pop()

def reverse(lista):
    return lista.reverse()




def execute_command(lista, *args):
    #callback result
    #commands = [i for i in args]
    commands = args

    #Definindo order
    order = commands[0][0]

    if order == 'insert':
        lista = insert(lista, int(commands[0][1]), int(commands[0][2]))

    elif order == 'print':
        print(lista)
    
    elif order == 'remove':
        lista = remove(lista, int(commands[0][2]))
    
    elif order == 'append':
        lista = append(lista, int(commands[0][2]))

    elif order == 'sort':
        lista = sort_(lista)
    
    elif order == 'pop':
        lista = pop(lista)
    
    elif order == 'reverse':
        lista = reverse(lista)

        
#Exec

if __name__ == '__main__':
    try:
        N = int(input())
    except:
        print('Não é um valor válido!')
    
    lstate = []
    i = 0
    while i < N:
        execute_command(lstate, get_command())
        i += 1


    

    



#read input
#command = input('Comando: ')
