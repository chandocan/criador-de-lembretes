'''
aplicativo para pequenos lebretes do dia a dia 
'''
from datetime import datetime


#tempo = int(input('diga o tempo:'))
# se bota o Y maiusculo sai a data completa:
data = (datetime.today().strftime('%d-%m-%Y'))

lista = ['','','','','']
while True:


    pedido = input('deseja criar um lembrete ? [s] ou [n] exibir [e] remover mensagem [r] espera tempo para lembrete ser exibido para você[es] ou salvar[salvar]:').lower()

    print('data',data)
    print('horas e minutos',datetime.today().strftime('%H:%M'))
    
    def salvandoArq(lista):
         
        with open("arquivoLista.txt", 'w') as f:
            for s in lista:
                f.write(str(s) + '\n')

        with open("arquivoLista.txt", 'r') as f:
            lista = [line.rstrip('\n') for line in f]

    def salvando_mensagemEmlista(mensagem1):
        bandeira = input('deseja colocara a messagem na  posição 1 ate 5:')

        if bandeira == '1':
            
            lista.insert(0,mensagem1) # inseril na posição 1 
            
        elif bandeira == '2':
            
            lista.insert(1,mensagem1)

        elif bandeira == '3':
            lista.insert(2,mensagem1)
        
        elif bandeira == '4':
            lista.insert(3,mensagem1)
            
        elif bandeira == '5':
            
            lista.insert(4,mensagem1)

    

  
    def tempo_espera(dia, mes, hora, minuto, mensagem1):
            while True:


                if dia == (datetime.today().strftime('%d')) and mes == (datetime.today().strftime('%m')) and ano == (datetime.today().strftime('%Y')) and hora == (datetime.today().strftime('%H')) and minuto == (datetime.today().strftime('%M')) :
                    print(mensagem1)
                    print('fim da transmissão')
                    break


            
    # removendo elemento
    if pedido == 'r':
        print(lista)
        r = input('elemento a remover da posição 1 ate 5:')
        if r == '1':
            lista.remove(lista[0])
        if r == '2':
            lista.remove(lista[1])
        if r == '3':
            lista.remove(lista[2])
        if r == '4':
            lista.remove(lista[3])
        if r == '5':
            lista.remove(lista[4])
          
    if pedido == 's':
        mensagem1 = input('Escreva MESSAGEM ou LEMBRETE:')
        dia = input('digite o dia que sera exibida:')
        mes = input('digite o mês que sera exibida:')
        ano = input('o ano dessa que sera exibida:')
        hora = input('qual hora você quer ver essa messagem:')
        minuto = input('dite os minuto da da hora aqui:')
        salvando_mensagemEmlista(mensagem1)
      
    if pedido == 'e':
        print(lista)

    if pedido == 'es':
        tempo_espera(dia, mes, hora, minuto, mensagem1)

    if pedido == 'salvar':
        salvandoArq(lista)
    
    else:
        print('estou sempre aqui para te lembra algo !')
        reinicio = input('deseja termina[sair] ou continuar [c] ?:')
        if reinicio == 'sair':
            break
        else:
            continue

