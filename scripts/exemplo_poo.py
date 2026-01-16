# Exemplo prático de POO em Python para demonstrar o conhecimento do NotebookLM
class Conhecimento:
    def __init__(self, fonte):
        self.fonte = fonte
        self.processado = False

    def processar(self):
        self.processado = True
        return f"Processando {self.fonte} através da IA Generativa..."

class NotebookLM(Conhecimento):
    def gerar_insight(self):
        if self.processado:
            return "Insight gerado: A união de POO e Python cria estruturas sólidas!"
        return "Primeiro, processe a fonte."

# Demonstração
meu_projeto = NotebookLM("PDF de POO e Python")
print(meu_projeto.processar())
print(meu_projeto.gerar_insight())