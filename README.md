# Pelé Next Gen --- Back-office MVP Concierge

Projeto desenvolvido para a Sprint 4 da disciplina **Computational
Thinking with Python**. O sistema simula o back-office de uma peneira de
futebol: cadastra atletas, registra avaliações, calcula notas e exibe o
ranking e as métricas gerais.

## Funcionalidades

-   Cadastro de atletas com nome, idade, posição, cidade, estado, pé
    dominante e telefone/WhatsApp.
-   Validação das entradas para reduzir dados inválidos.
-   Registro de notas de 0 a 10 para cinco critérios de avaliação.
-   Pergunta sobre habilidade com os dois pés e aplicação de bônus na
    nota.
-   Cálculo da nota final e classificação do atleta.
-   Exibição do ranking geral, das métricas da seletiva e da lista de
    atletas cadastrados.

## Requisitos

-   Python 3 instalado.
-   Terminal ou prompt de comando para executar o programa.

O projeto utiliza apenas recursos da biblioteca padrão do Python; não é
necessário instalar dependências externas.

## Como executar

1.  Baixe ou clone os arquivos do projeto.
2.  Abra um terminal na pasta onde está o arquivo `console.py`.
3.  Execute:

``` bash
python console.py
```

Em alguns ambientes, pode ser necessário usar:

``` bash
python3 console.py
```

## Menu principal

Ao iniciar, o sistema apresenta as opções:

-   **1 --- Inserir e processar teste real:** cadastra um atleta,
    registra as notas e gera o resultado.
-   **2 --- Ver ranking dos atletas:** mostra os atletas avaliados em
    ordem decrescente de nota.
-   **3 --- Ver métricas gerais da seletiva:** apresenta totais e médias
    dos critérios.
-   **4 --- Listar atletas cadastrados:** mostra os atletas armazenados
    na sessão.
-   **0 --- Sair:** encerra o programa.

## Regras de validação

-   **Nome:** exige pelo menos nome e sobrenome; não aceita números nem
    caracteres especiais.
-   **Idade:** aceita valores inteiros de 12 a 21 anos.
-   **Posição:** deve ser escolhida entre as opções exibidas pelo
    sistema.
-   **Cidade:** exige pelo menos dois caracteres e não aceita números
    nem caracteres especiais.
-   **Estado:** aceita somente siglas válidas de duas letras dos estados
    brasileiros e do Distrito Federal.
-   **Pé dominante:** deve ser selecionado pelas opções apresentadas.
-   **Telefone/WhatsApp:** aceita somente números, com 10 ou 11 dígitos,
    incluindo DDD.
-   **Joga bem com os dois pés?:** aceita exclusivamente `s` (sim) ou
    `n` (não).
-   **Notas:** cada critério recebe uma nota inteira de 0 a 10.

Quando uma entrada é inválida, o programa exibe uma mensagem e solicita
que o usuário informe o valor novamente.

## Critérios de avaliação e classificação

O sistema utiliza cinco critérios:

-   Técnica
-   Tática
-   Física
-   Mental
-   Intensidade

A nota base é a média dos cinco critérios. Caso o atleta responda `s` à
pergunta sobre jogar bem com os dois pés, recebe bônus de **0,5 ponto**.
A nota final é limitada a 10.

A decisão é definida pela nota final:

-   **Aprovado:** nota igual ou superior a 7,0.
-   **Reavaliar:** nota igual ou superior a 6,0 e inferior a 7,0.
-   **Reprovado:** nota inferior a 6,0.

## Armazenamento dos dados

Nesta versão, os atletas e as avaliações ficam armazenados em listas na
memória do programa. Os dados iniciais são exemplos de teste. Os novos
cadastros não são salvos em um banco de dados ou arquivo e são perdidos
quando o programa é encerrado.

## Estrutura do projeto

``` text
.
├── console.py
└── README.md
```

## Observações

Este projeto é um MVP acadêmico para demonstrar validação de dados,
estruturas de controle, funções, listas e dicionários em Python. Antes
de utilizar o sistema em uma operação real, seria necessário implementar
persistência de dados, proteção de informações pessoais e testes
adicionais.

## Integrantes

Arthur Moreira Costa e equipe.
