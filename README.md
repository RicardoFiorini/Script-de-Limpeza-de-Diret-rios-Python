# Script de Limpeza de Diretórios (Python)
Uma ferramenta de **automação** robusta para manter seus diretórios organizados e otimizar o espaço de armazenamento do seu sistema.
## O que o script faz?
Este script foi criado para resolver o problema de acúmulo de arquivos desnecessários. Ele percorre caminhos definidos e aplica regras de limpeza automática:

- **Remoção por idade:** Deleta arquivos que não são modificados há X dias.
- **Filtro de Extensão:** Alvo específico para arquivos .tmp, .log ou .old.
- **Organização:** Move arquivos para pastas categorizadas (Imagens, Documentos, etc).
- **Recursividade:** Capacidade de limpar subpastas profundamente.

## Status de Desenvolvimento
- [x] Implementar varredura de diretórios
- [x] Lógica de exclusão por data de modificação
- [x] Filtro de extensões específicas
- [ ] Interface gráfica para seleção de pastas
- [ ] Geração de relatório de limpeza (Log em .txt)
## Exemplo de Código (Lógica de Varredura)
Abaixo, um trecho que demonstra como o script utiliza a biblioteca *os* para validar arquivos antigos:
```python

import os
import time
def limpar_antigos(diretorio, dias):
limite = time.time() - (dias * 86400)
for arquivo in os.listdir(diretorio):
caminho = os.path.join(diretorio, arquivo)
if os.path.getmtime(caminho) < limite:
os.remove(caminho)
print(f"Removido: {arquivo}")

```
## Avisos de Segurança
> [!TIP]
> Sempre execute o script em modo de teste (print) antes de ativar a função de deleção real para garantir que arquivos importantes não sejam removidos por engano!
## Configurações de Limpeza
| Tipo de Arquivo | Ação Recomendada | Frequência |
| --- | --- | --- |
| .log | Excluir | Semanal |
| .tmp | Excluir | Diário |
| .pdf / .docx | Mover para /Documentos | Manual |
