"""Sua organização acaba de contratar um estagiário para trabalhar no
Suporte de Informática, com a intenção de fazer um levantamento nas
sucatas encontradas nesta área. A primeira tarefa dele é testar todos os
mouses que se encontram lá, testando e anotando o estado de cada um
deles, para verificar o que se pode aproveitar.
Foi requisitado que você desenvolva um programa para registrar este
levantamento. O programa deverá receber a quantidade de mouses, e o
tipo de defeito de cada um (armazene em um vetor), sendo eles:

 1 - necessita da esfera;
 2 - necessita de limpeza;
 3 - necessita troca do cabo ou conector;
 4 - quebrado ou inutilizado"""
"""Ao final o programa deverá emitir o seguinte relatório (exemplo):"""
lista = [0, 0, 0, 0]
mouse = int(input("digite a quantidade de mouses: "))
for i in range(mouse):
    print("agora digite o defeito de cada mouse\n 1 - necessita da esfera\n2 - necessita de limpeza \n3 - necessita troca do cabo ou conector \n4 - quebrado ou inutilizado\n ")
    defeito=int(input("digite o numero correspondente ao defeito:").strip())
    if 1 <= defeito or defeito <=4:
            lista[defeito - 1]= lista[defeito - 1]+1

print(f"Situação                                         Quantidade                      Percentual")
print(f"1 - necessita da esfera:                            {lista[0]}                              {(lista[0]/(mouse))*100:.2f}%")
print(f"2 - necessita de limpeza:                           {lista[1]}                              {(lista[1]/(mouse))*100:.2f}%")
print(f"3 - necessita troca do cabo ou conector:            {lista[2]}                              {(lista[2]/(mouse))*100:.2f}%")
print(f"4 - quebrado ou inutilizado:                        {lista[3]}                              {(lista[3]/(mouse))*100:.2f}%")





