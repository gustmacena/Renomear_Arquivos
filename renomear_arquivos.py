import os

# Pasta mãe que contém as subpastas
pasta_mae = "C:\\Users\\gusta\\Desktop\\LPM"  # Substitua pelo caminho da sua pasta mãe

# Verifique se o caminho da pasta mãe é válido
if not os.path.exists(pasta_mae):
    print("A pasta mãe especificada não existe.")
else:
    # Lista todas as subpastas na pasta mãe
    subpastas = [f.path for f in os.scandir(pasta_mae) if f.is_dir()]

    # Loop pelas subpastas
    for subpasta in subpastas:
        # Obtenha a lista de arquivos na subpasta
        arquivos = os.listdir(subpasta)
        
        # Classifique os arquivos para garantir que eles sejam renomeados na ordem
        arquivos.sort()

        # Variável para controlar o novo nome dos arquivos
        novo_nome = 1

        # Loop pelos arquivos e renomeie-os mantendo a extensão
        for arquivo in arquivos:
            # Obtenha a extensão do arquivo
            extensao = os.path.splitext(arquivo)[1]
            
            # Crie o novo nome com base no contador
            novo_nome_completo = os.path.join(subpasta, str(novo_nome) + extensao)
            
            # Renomeie o arquivo
            os.rename(os.path.join(subpasta, arquivo), novo_nome_completo)
            
            # Incremente o contador
            novo_nome += 1

    print("Arquivos renomeados com sucesso nas subpastas.")
