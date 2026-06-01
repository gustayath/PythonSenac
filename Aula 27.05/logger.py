import datetime

class MeuLogger:
    def __init__(self, ficheiro="meulog.txt"):
        self.ficheiro = ficheiro
    
    def escrever(self, nivel, mensagem):
        hora = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
        linha = f"[{hora}] {nivel}: {mensagem}\n"

        ''' 'a' para append (acrescentar ao final do ficheiro)'''
        with open(self.ficheiro, "a", encoding="utf-8") as f:
            f.write(linha)

    def info(self, msg): self.escrever("INFO", msg)
    def erro(self, msg): self.escrever("ERRO", msg)
    def debug(self, msg): self.escrever("DEBUG", msg)

'''Exemplos de uso'''
log = MeuLogger()
log.info("Sistema Iniciado.")
log.erro("Erro no sistema.")
log.debug("Debugando")
