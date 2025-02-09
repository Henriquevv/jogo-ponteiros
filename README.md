# Pointer Game Solver  

##  Descrição  
Este projeto implementa um **jogo de ponteiros**, onde cada posição em um tabuleiro contém um ponteiro que pode apontar para 0°, 90°, 180° ou 270°. O objetivo do jogo é alinhar todos os ponteiros na mesma direção, utilizando um agente inteligente e uma abordagem de busca heurística.  

A solução do jogo é encontrada usando o algoritmo **A* (A-star search)** da biblioteca **AIMA-Python**.  

##  Funcionalidades  
- Simulação de um ambiente 2D onde os ponteiros giram e o agente se move.  
- Implementação de um **agente inteligente** que resolve o jogo.  
- Modelagem do jogo como um **problema de busca**, permitindo a aplicação do **algoritmo A*** para encontrar a solução ótima.  
- Estado inicial aleatório gerado automaticamente.  

##  Estrutura do Código  
O projeto é estruturado da seguinte forma:  

1️⃣ **Ambiente do Jogo (`PointerGameEnvironment`)**  
- Representa o tabuleiro e os ponteiros.  
- Define ações de rotação e movimento do agente.  

2️⃣ **Agente Inteligente (`PointerGameAgent`)**  
- Explora o ambiente e decide ações com base na estratégia de busca.  

3️⃣ **Modelagem do Problema (`PointerGameProblem`)**  
- Define o espaço de estados e a função heurística.  

4️⃣ **Algoritmo de Resolução (`resolver_jogo`)**  
- Implementação do algoritmo **A*** para encontrar a solução.  

5️⃣ **Execução do Jogo (`main`)**  
- Cria o ambiente e executa a solução passo a passo.  

##  Requisitos  
- Python 3.x  
- Biblioteca **AIMA-Python** (`agents4e`, `search`)   

###  Instalação das Dependências  
Se a biblioteca AIMA-Python não estiver instalada, acesse:  
```bash  
https://github.com/aimacode/aima-python
```

##  Como Executar  
Para rodar o jogo, basta executar o script principal:  
```bash  
python main.py  
```

##  Exemplo de Saída  
O programa imprime o **estado inicial**, a **sequência de ações** que resolvem o jogo e o **estado final** dos ponteiros.  

Exemplo de saída:  
```
Estado inicial: (((0, 0), 0), ((0, 1), 0), ((1, 0), 270), ((1, 1), 270))
Posição inicial do agente: (1, 0)

Solução encontrada!
Passo 1: ('GirarHorario', (1, 0))
Passo 2: Mover para (1, 1)
Passo 3: ('GirarHorario', (1, 1))

Estado final dos ponteiros:
Ponteiro em (0, 0): 0°
Ponteiro em (0, 1): 0°
Ponteiro em (1, 0): 0°
Ponteiro em (1, 1): 0°
```

