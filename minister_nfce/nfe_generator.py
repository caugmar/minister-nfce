from pynfe.processamento.nfe import ProcessadorNFe

def generate_nfce(dados_empresa, cliente, itens):
    proc = ProcessadorNFe()
    proc.ambiente = 2  # Homologação
    proc.certificado_digital_arquivo = "certificado.pfx"
    proc.senha_certificado = "senha"

    nfce = proc.criar_nfe(dados_empresa, cliente, itens)
    retorno = proc.enviar_nfe()
    return retorno
