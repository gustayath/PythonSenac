from logger import MeuLogger

def test(u):
    logger = MeuLogger(u)
    logger.info("Sistema iniciado")

u = "gusta.txt"
test(u)

print("Fim do script de teste de importação! ")