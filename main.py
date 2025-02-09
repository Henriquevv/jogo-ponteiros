# Importações do AIMA Python
from agents4e import Agent, XYEnvironment
from search import Problem, astar_search
import random
import ast 

# ==============================
# Ambiente do Jogo
# ==============================
class PointerGameEnvironment(XYEnvironment):
    def __init__(self, tamanho=2):
        super().__init__(width=tamanho, height=tamanho)
        self.estado = self.estado_inicial()
        self.agente = None

    def estado_inicial(self):
        """Cria um estado inicial como uma tupla ordenada"""
        estado = {(x, y): random.choice([0, 90, 180, 270]) for x in range(self.width) for y in range(self.height)}
        return tuple(sorted(estado.items()))  

    def percept(self, agent):
        return dict(self.estado)[agent.location]  

    def execute_action(self, agent, action):
        """Executa ação e atualiza o estado do ambiente"""

        if action in ["GirarHorario", "GirarAntiHorario"]:
            estado_dict = dict(self.estado)
            estado_dict[agent.location] = (estado_dict[agent.location] + (90 if action == "GirarHorario" else -90)) % 360
            self.estado = tuple(sorted(estado_dict.items()))  

        elif action.startswith("Mover"):
            try:
                nova_posicao = ast.literal_eval(action.split("Mover ")[1]) 
                if nova_posicao in dict(self.estado):  
                    agent.location = nova_posicao
                else:
                    print(f"Movimento inválido: {nova_posicao}")  
            except (ValueError, SyntaxError):
                print(f"Erro ao interpretar posição de movimento: {action}") 



    def mover_agente(self, agent, direction):
        """Move o agente dentro do tabuleiro"""
        x, y = agent.location
        movimentos = {
            "Esquerda": (x - 1, y),
            "Direita": (x + 1, y),
            "Cima": (x, y - 1),
            "Baixo": (x, y + 1)
        }
        if direction in movimentos and movimentos[direction] in dict(self.estado):
            agent.location = movimentos[direction]

    def estado_final(self):
        """Verifica se todos os ponteiros estão alinhados"""
        state = dict(self.estado)
        direcao_padrao = list(state.values())[0]
        return all(rotacao == direcao_padrao for rotacao in state.values())

# ==============================
# Agente Inteligente
# ==============================
class PointerGameAgent(Agent):
    def __init__(self, environment):
        super().__init__()
        self.environment = environment
        self.location = random.choice(list(dict(environment.estado).keys()))
        self.program = self.escolher_acao

    def escolher_acao(self, percept):
        estado_atual = self.environment.estado
        return resolver_jogo(estado_atual)

# ==============================
# Modelando o Problema de Busca
# ==============================
class PointerGameProblem(Problem):
    def __init__(self, initial_state):
        super().__init__(initial_state)

    def actions(self, state):
        """Converte estado para dicionário antes de acessar"""
        state = dict(state)
        posicoes = list(state.keys())
        acoes = []
        for pos in posicoes:
            if state[pos] != 0:
                acoes.append(("GirarHorario", pos))
                acoes.append(("GirarAntiHorario", pos))
        return acoes

    def result(self, state, action):
        """Aplica ação e retorna um estado imutável"""
        new_state = dict(state)
        if action[0] in ["GirarHorario", "GirarAntiHorario"]:
            sentido = 90 if action[0] == "GirarHorario" else -90
            new_state[action[1]] = (new_state[action[1]] + sentido) % 360
        return tuple(sorted(new_state.items())) 

    def goal_test(self, state):
        """Verifica se o estado é final"""
        state = dict(state)
        direcao_padrao = list(state.values())[0]
        return all(rotacao == direcao_padrao for rotacao in state.values())

    def h(self, node):
        """Heurística: Número de ponteiros desalinhados"""
        estado = dict(node.state)
        direcoes = {rotacao: list(estado.values()).count(rotacao) for rotacao in [0, 90, 180, 270]}
        melhor_direcao = max(direcoes, key=direcoes.get)
        return sum(1 for rotacao in estado.values() if rotacao != melhor_direcao)

# ==============================
# Resolvendo o Jogo com A*
# ==============================
def resolver_jogo(estado_inicial):
    problema = PointerGameProblem(estado_inicial)
    solucao = astar_search(problema)
    return solucao.solution()

# ==============================
# Executando o Jogo
# ==============================
if __name__ == "__main__":
    ambiente = PointerGameEnvironment()
    agente = PointerGameAgent(ambiente)
    ambiente.add_thing(agente, location=agente.location)

    print("Estado inicial:", ambiente.estado)
    print("Posição inicial do agente:", agente.location)
    
    solucao = resolver_jogo(ambiente.estado)

    if solucao:
        print("\nSolução encontrada!")
        passo = 1
        posicao_atual = agente.location  
        for acao in solucao:
            if acao[0] in ["GirarHorario", "GirarAntiHorario"]:
                if posicao_atual != acao[1]:
                    print(f"Passo {passo}: Mover para {acao[1]}")
                    ambiente.execute_action(agente, f"Mover {acao[1]}")
                    posicao_atual = acao[1] 
                    passo += 1

                print(f"Passo {passo}: {acao}")
                ambiente.execute_action(agente, acao[0])
                passo += 1

        print("\nEstado final dos ponteiros:")
        estado_final = dict(ambiente.estado) 
        for posicao, direcao in estado_final.items():
            print(f"Ponteiro em {posicao}: {direcao}°")
    else:
        print("\nNenhuma solução encontrada.")