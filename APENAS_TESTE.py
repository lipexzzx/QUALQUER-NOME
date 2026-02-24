import random

class Pessoa:
    def __init__(self, nome, classe, altura, peso, idade, riqueza, interesses):
        self.nome = nome
        self.classe = classe
        self.altura = altura
        self.peso = peso
        self.idade = idade
        self.riqueza = riqueza
        self.interesses = interesses

def gerar_dados(quantidade):
    dados = []
    for _ in range(quantidade):
        pessoa = Pessoa(
            nome=f'Pessoa {random.randint(1, 1000)}',
            classe=random.choice(['A', 'B', 'C']),
            altura=random.uniform(1.4, 2.0),
            peso=random.randint(40, 120),
            idade=random.randint(18, 80),
            riqueza=random.choice([True, False]),
            interesses=random.sample(['Esportes', 'Música', 'Ler', 'Viajar'], random.randint(1, 3))
        )
        dados.append(pessoa)
    return dados

def separar_por_grupo(dados):
    grupos = {
        'A': [],
        'B': [],
        'C': [],
        'Altura Baixa': [],
        'Altura Média': [],
        'Altura Alta': [],
        'Peso Baixo': [],
        'Peso Médio': [],
        'Peso Alto': [],
        'Jovem': [],
        'Adulto': [],
        'Idoso': [],
        'Ricos': [],
        'Pobres': [],
        'Interesses Esportes': [],
        'Interesses Música': [],
        'Interesses Ler': [],
        'Interesses Viajar': []
    }
    for pessoa in dados:
        grupos[pessoa.classe].append(pessoa)
        if pessoa.altura < 1.6:
            grupos['Altura Baixa'].append(pessoa)
        elif pessoa.altura >= 1.6 and pessoa.altura < 1.8:
            grupos['Altura Média'].append(pessoa)
        else:
            grupos['Altura Alta'].append(pessoa)
        
        if pessoa.peso < 60:
            grupos['Peso Baixo'].append(pessoa)
        elif pessoa.peso >= 60 and pessoa.peso < 90:
            grupos['Peso Médio'].append(pessoa)
        else:
            grupos['Peso Alto'].append(pessoa)
        
        if pessoa.idade < 30:
            grupos['Jovem'].append(pessoa)
        elif pessoa.idade >= 30 and pessoa.idade < 60:
            grupos['Adulto'].append(pessoa)
        else:
            grupos['Idoso'].append(pessoa)
        
        if pessoa.riqueza:
            grupos['Ricos'].append(pessoa)
        else:
            grupos['Pobres'].append(pessoa)
        
        for interesse in pessoa.interesses:
            grupos[f'Interesses {interesse}'].append(pessoa)
    
    return grupos

def adicionar_pessoa(dados):
    while True:
        nome = input('Digite o nome da pessoa: ')
        if not nome:
            print('Nome inválido. Digite novamente.')
            continue
        break
    
    while True:
        classe = input('Digite a classe da pessoa (A, B, C): ')
        if classe.upper() not in ['A', 'B', 'C']:
            print('Classe inválida. Digite novamente.')
            continue
        break
    
    while True:
        altura = input('Digite a altura da pessoa: ')
        if not altura:
            print('Altura inválida. Digite novamente.')
            continue
        try:
            altura = float(altura)
            if altura < 1.4 or altura > 2.0:
                print('Altura inválida. Digite novamente.')
                continue
            break
        except ValueError:
            print('Altura inválida. Digite novamente.')
            continue
    
    while True:
        peso = input('Digite o peso da pessoa: ')
        if not peso:
            print('Peso inválido. Digite novamente.')
            continue
        try:
            peso = int(peso)
            if peso < 40 or peso > 120:
                print('Peso inválido. Digite novamente.')
                continue
            break
        except ValueError:
            print('Peso inválido. Digite novamente.')
            continue
    
    while True:
        idade = input('Digite a idade da pessoa: ')
        if not idade:
            print('Idade inválida. Digite novamente.')
            continue
        try:
            idade = int(idade)
            if idade < 18 or idade > 80:
                print('Idade inválida. Digite novamente.')
            