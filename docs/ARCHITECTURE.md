# Arquitetura do Sistema Todo List

## Visão Geral

O Sistema Todo List é uma aplicação CLI (Command Line Interface) minimalista que gerencia uma lista de tarefas persistida em JSON. Sem dependências externas, utiliza apenas a biblioteca padrão do Python.

## Componentes Principais

### 1. Arquivo Principal (`src/todo.py`)

O arquivo principal contém toda a lógica da aplicação:

- **`TASKS_FILE`**: Caminho do arquivo `todo.json` onde as tarefas são armazenadas
- **`load_tasks()`**: Carrega tarefas do arquivo JSON (retorna lista vazia se arquivo não existe)
- **`save_tasks(tasks)`**: Persiste tarefas no arquivo JSON

### 2. Operações Suportadas

#### Adicionar Tarefa (`add_task`)
- Adiciona uma nova tarefa à lista
- Status inicial: não concluída (`done: False`)
- Persiste a mudança imediatamente no arquivo

#### Listar Tarefas (`list_tasks`)
- Exibe todas as tarefas com índice e status
- Tarefa concluída exibe com ✓
- Tarefa pendente exibe sem marcação

#### Marcar Concluída (`mark_done`)
- Marca uma tarefa como concluída por índice
- Alterna o valor de `done` para `True`

#### Editar Tarefa (`edit_task`)
- Altera o texto de uma tarefa existente
- Preserva o status de conclusão

#### Remover Tarefa (`remove_task`)
- Remove uma tarefa da lista por índice

#### Duplicar Tarefa (`duplicate_task`)
- Cria uma cópia idêntica de uma tarefa
- A cópia mantém o mesmo status de conclusão

#### Exportar como JSON (`export_tasks`)
- Exibe todas as tarefas em formato JSON
- Útil para integração com outras ferramentas

#### Exportar como CSV (`export_csv`)
- Exibe as tarefas em formato CSV
- Colunas: Texto, Status (Concluído/Pendente)
- Pronto para usar em planilhas

### 3. Estrutura de Dados

Cada tarefa é um dicionário com dois campos:

```json
{
  "text": "descrição da tarefa",
  "done": false
}
```

Todas as tarefas são armazenadas em um array JSON:

```json
[
  {"text": "tarefa 1", "done": true},
  {"text": "tarefa 2", "done": false},
  {"text": "tarefa 3", "done": false}
]
```

### 4. Persistência

- Arquivo padrão: `todo.json` no diretório de execução
- Formato: JSON puro (sem compressão)
- Salvo a cada operação que modifica tarefas
- Compatível com leitura manual e edição direta

## Interface CLI

A aplicação é invocada via linha de comando:

```bash
python src/todo.py <comando> [argumentos]
```

### Exemplos

```bash
python src/todo.py add "comprar leite"
python src/todo.py list
python src/todo.py done 0
python src/todo.py edit 0 "comprar leite orgânico"
python src/todo.py duplicate 0
python src/todo.py remove 0
python src/todo.py export
```

## Fluxo de Dados

```
CLI Input (sys.argv)
        ↓
    Parse Comando
        ↓
    Executar Operação
    (load_tasks → modificar → save_tasks)
        ↓
    Exibir Resultado
        ↓
    Atualizar todo.json
```

## Testes

O arquivo `tests/test_todo.py` contém testes unitários usando pytest:

- **`test_add_and_list_tasks`**: Valida adição e listagem
- **`test_mark_done`**: Valida conclusão de tarefas
- **`test_remove_task`**: Valida remoção
- **`test_edit_task`**: Valida edição de texto
- **`test_duplicate_task`**: Valida duplicação
- **`test_export_tasks_json`**: Valida exportação JSON
- **`test_export_tasks_csv`**: Valida exportação CSV
- **`test_full_workflow`**: Testa fluxo completo

Execute com:

```bash
python -m pytest tests/test_todo.py
```

## Sincronização com Repositório Finish

A aplicação está configurada para sincronizar automaticamente com um repositório "finish" via GitHub Actions:

1. **Trigger**: Push para a branch `main`
2. **Workflow**: `.github/workflows/sync-to-finish.yml`
3. **Ações**:
   - Copia arquivos Python da pasta `src/`
   - Remove comentários do código
   - Remove documentação (mantém README do destino)
   - Faz commit e push no repositório alvo

Isso permite que o código limpo chegue no repositório finish pronto para execução por agentes de IA.

## Design Decisions

- **Sem dependências**: Usa apenas stdlib Python (json, csv, sys, pathlib)
- **Simplicidade**: Uma só classe/arquivo para facilitar compreensão
- **Imediato**: Persiste a cada operação (sem staging/commit explícito)
- **Agnóstico**: Funciona em qualquer diretório (cria `todo.json` localmente)
