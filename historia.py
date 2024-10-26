import random

#função que gera a introdução da história
def gerar_introducao():
    introducoes = ["Era uma vez", "Há muito tempo atrás", "Num reino distante"]
    return random.choice(introducoes)

#função que gera o desenvolvimento da história
def gerar_desenvolvimento():
    desenvolvimentos = ["um valente cavaleiro", "uma destemida guerreira", "um bravo guerrreiro", "ujm bravo guerreiro", "uma poderosa feiticeira", "um sábio mago"]
    return random.choice(desenvolvimentos)

#função que gera o final da história
def gerar_final():
    finais = ["enfrentando dragões ferozes", "derrotando um terrível vilão", "descobrindo um tesouro escondido", "salvando o reino da escuridão", "encontrando o amor verdadeiro"]
    return random.choice(finais)

#função principal que gera toda a história
def gerar_historia():
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    final =  gerar_final()
    
    historia = f"{introducao}  {desenvolvimento} {final}"
    return historia


#exibe a história gerada
if __name__ == "__main__":
    print(gerar_historia())
