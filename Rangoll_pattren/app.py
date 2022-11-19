# rangol pattren:
def rangol_pattren(size: int) : 
    alpha=  'abcdefghijklmnopqrstuvwxyz'
    data= [alpha[i] for i in range(size)]
    item=list(range(size))
    item= item[:-1]+ item[:-1]
    for i in item : 
        tem= data[-(i+1)]
        row= tem[::1] + tem[1:]
        print('-'.join(row).center( size*4-3,'-' ))
if __name__ == '__main__': 
    sze= int(input('enter the size of pattren :  '))
    rangol_pattren(sze)
    