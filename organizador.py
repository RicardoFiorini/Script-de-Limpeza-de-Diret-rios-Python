import os
import shutil
import glob
import time
from pathlib import Path

# --- Configuração ---

# 1. Defina a pasta que você quer organizar.
# Usamos Path.home() para encontrar sua pasta de usuário (ex: /home/usuario ou C:/Users/Usuario)
# e depois adicionamos "Downloads" a ela.
PASTA_ALVO = os.path.join(Path.home(), 'Downloads')

# 2. Defina o mapeamento de extensões para pastas.
# A CHAVE (ex: '.pdf') é a extensão do arquivo (em minúsculas).
# O VALOR (ex: 'Documentos') é o nome da subpasta para onde o arquivo será movido.
MAPEAMENTO_PASTAS = {
    # Documentos
    '.pdf': 'Documentos',
    '.doc': 'Documentos',
    '.docx': 'Documentos',
    '.xls': 'Documentos',
    '.xlsx': 'Documentos',
    '.ppt': 'Documentos',
    '.pptx': 'Documentos',
    '.txt': 'Documentos',
    '.csv': 'Documentos',

    # Imagens
    '.jpg': 'Imagens',
    '.jpeg': 'Imagens',
    '.png': 'Imagens',
    '.gif': 'Imagens',
    '.bmp': 'Imagens',
    '.svg': 'Imagens',
    '.webp': 'Imagens',

    # Vídeos
    '.mp4': 'Videos',
    '.mov': 'Videos',
    '.avi': 'Videos',
    '.mkv': 'Videos',
    '.wmv': 'Videos',

    # Áudio
    '.mp3': 'Audio',
    '.wav': 'Audio',
    '.aac': 'Audio',
    '.flac': 'Audio',

    # Arquivos Compactados
    '.zip': 'Compactados',
    '.rar': 'Compactados',
    '.7z': 'Compactados',
    '.tar': 'Compactados',
    '.gz': 'Compactados',

    # Instaladores e Programas
    '.exe': 'Instaladores',
    '.msi': 'Instaladores',
    '.dmg': 'Instaladores', # Para macOS
    '.deb': 'Instaladores', # Para Linux (Debian/Ubuntu)
    '.iso': 'ImagensISO',
}

# 3. Nome da pasta para arquivos não mapeados
PASTA_OUTROS = 'Outros'

# 4. Intervalo de verificação em segundos
INTERVALO_VERIFICACAO = 30 # 30 segundos

# --- Fim da Configuração ---


def organizar_pasta(pasta):
    """
    Função principal que organiza os arquivos na pasta_alvo.
    """
    print(f"[{time.ctime()}] Verificando {pasta}...")
    arquivos_movidos = 0

    # Usando glob para encontrar todos os itens na pasta
    # O curinga '*' pega qualquer nome de arquivo/pasta
    caminho_busca = os.path.join(pasta, '*')

    for caminho_completo_origem in glob.glob(caminho_busca):
        
        # Etapa 1: Ignorar se for um diretório
        if not os.path.isfile(caminho_completo_origem):
            continue

        # Etapa 2: Obter nome do arquivo e extensão
        nome_arquivo = os.path.basename(caminho_completo_origem)
        _raiz, extensao = os.path.splitext(nome_arquivo)
        extensao = extensao.lower() # Normaliza para minúsculas

        # Etapa 3: Encontrar a pasta de destino no mapeamento
        # Se a extensão não for encontrada, usa PASTA_OUTROS como padrão
        nome_pasta_destino = MAPEAMENTO_PASTAS.get(extensao, PASTA_OUTROS)
        
        # Etapa 4: Criar o caminho completo da pasta de destino
        caminho_pasta_destino = os.path.join(pasta, nome_pasta_destino)

        # Etapa 5: Criar a pasta de destino se ela não existir
        # os.makedirs com exist_ok=True não dá erro se a pasta já existir
        os.makedirs(caminho_pasta_destino, exist_ok=True)

        # Etapa 6: Mover o arquivo
        caminho_completo_destino = os.path.join(caminho_pasta_destino, nome_arquivo)

        try:
            # A função shutil.move faz todo o trabalho de mover o arquivo
            shutil.move(caminho_completo_origem, caminho_completo_destino)
            print(f"  -> Movido: '{nome_arquivo}' para '{nome_pasta_destino}/'")
            arquivos_movidos += 1
        except Exception as e:
            print(f"  [ERRO] Nao foi possivel mover '{nome_arquivo}': {e}")

    if arquivos_movidos == 0:
        print("Nenhum arquivo novo para organizar.")
    else:
        print(f"Organização concluída. {arquivos_movidos} arquivo(s) movido(s).")


if __name__ == "__main__":
    if not os.path.isdir(PASTA_ALVO):
        print(f"Erro: A pasta '{PASTA_ALVO}' nao existe.")
        print("Por favor, verifique a configuracao 'PASTA_ALVO' no script.")
    else:
        print(f"--- Iniciando Organizador de Diretórios ---")
        print(f"Pasta monitorada: {PASTA_ALVO}")
        print(f"Intervalo de verificacao: {INTERVALO_VERIFICACAO} segundos")
        print("Pressione CTRL+C para parar o script.")
        
        try:
            # Loop infinito para "assistir" a pasta
            while True:
                organizar_pasta(PASTA_ALVO)
                time.sleep(INTERVALO_VERIFICACAO)
        except KeyboardInterrupt:
            print("\nScript interrompido pelo usuario. Encerrando...")