
# ---------------------------------------------------------------------------
# CONSTANTES E REGRAS DE NEGÓCIO
# ---------------------------------------------------------------------------
POSICOES = ["Goleiro", "Zagueiro", "Lateral", "Volante", "Meia", "Atacante"]
CRITERIOS = ["tecnica", "tatica", "fisica", "mental", "intensidade"]
NOTA_APROVACAO = 7.0

UFS_VALIDAS = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
    "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
    "RS", "RO", "RR", "SC", "SP", "SE", "TO"
]

# ---------------------------------------------------------------------------
# ESTRUTURAS DE DADOS (BASE EM MEMÓRIA COM DADOS DE TESTE)
# ---------------------------------------------------------------------------
atletas = [
    {
        "id": "A1",
        "nome": "João Vitor Silva",
        "idade": 18,
        "posicao": "Atacante",
        "cidade": "Santos",
        "estado": "SP",
        "pe": "Destro",
        "contato": "13988887777"
    },
    {
        "id": "A2",
        "nome": "Miguel Araújo",
        "idade": 17,
        "posicao": "Meia",
        "cidade": "Recife",
        "estado": "PE",
        "pe": "Canhoto",
        "contato": "81977776666"
    },
    {
        "id": "A3",
        "nome": "Lucas Ferreira",
        "idade": 19,
        "posicao": "Zagueiro",
        "cidade": "Belo Horizonte",
        "estado": "MG",
        "pe": "Destro",
        "contato": "31966665555"
    }
]

avaliacoes = [
    {
        "atleta_id": "A1",
        "scores": {"tecnica": 8, "tatica": 7, "fisica": 8, "mental": 7, "intensidade": 8},
        "pe_bonus": 0.5,
        "nota_geral": 8.1,
        "decisao": "aprovado",
        "comentario": "Boa finalização e drible rápido."
    },
    {
        "atleta_id": "A2",
        "scores": {"tecnica": 7, "tatica": 6, "fisica": 6, "mental": 6, "intensidade": 6},
        "pe_bonus": 0.0,
        "nota_geral": 6.2,
        "decisao": "reavaliar",
        "comentario": "Visão de jogo boa, mas precisa de ritmo físico."
    },
    {
        "atleta_id": "A3",
        "scores": {"tecnica": 5, "tatica": 5, "fisica": 7, "mental": 5, "intensidade": 6},
        "pe_bonus": 0.0,
        "nota_geral": 5.6,
        "decisao": "reprovado",
        "comentario": "Forte na bola aérea, passe precisa evoluir."
    }
]


# ---------------------------------------------------------------------------
# VALIDAÇÕES DE ENTRADA VIA VARIÁVEIS DE CONTROLE
# ---------------------------------------------------------------------------
def validar_apenas_letras(texto):
    """Permite letras Unicode (incluindo acentos) e espaços, sem números/símbolos."""
    texto = texto.strip()
    return bool(texto) and all(
        caractere.isspace() or caractere.isalpha()
        for caractere in texto
    )


def ler_nome():
    nome_valido = False
    nome_final = ""
    while not nome_valido:
        entrada = input("Nome completo do atleta: ").strip()
        partes = entrada.split()

        if len(partes) < 2:
            print("  [!] Nome inválido. Digite ao menos nome e sobrenome.")
        elif not validar_apenas_letras(entrada):
            print("  [!] O nome só pode conter letras e espaços, sem números ou símbolos.")
        else:
            nome_final = " ".join(partes).title()
            nome_valido = True
    return nome_final


def ler_cidade():
    cidade_valida = False
    cidade_final = ""
    while not cidade_valida:
        entrada = input("Cidade: ").strip()
        if len(entrada) < 2:
            print("  [!] O nome da cidade deve ter pelo menos 2 letras.")
        elif not validar_apenas_letras(entrada):
            print("  [!] A cidade só pode conter letras e espaços, sem números ou símbolos.")
        else:
            cidade_final = " ".join(entrada.split()).title()
            cidade_valida = True
    return cidade_final


def ler_estado():
    uf_valida = False
    uf_final = ""
    while not uf_valida:
        entrada = input("Estado (sigla UF, ex: SP, RJ): ").strip().upper()
        if len(entrada) == 2 and entrada in UFS_VALIDAS:
            uf_final = entrada
            uf_valida = True
        else:
            print("  [!] UF inválida. Digite apenas a sigla de 2 letras de um estado brasileiro.")
    return uf_final


def ler_telefone():
    telefone_valido = False
    telefone_final = ""
    while not telefone_valido:
        entrada = input("Telefone / WhatsApp com DDD (somente números): ").strip()
        if not entrada or any(caractere not in "0123456789" for caractere in entrada):
            print("  [!] Telefone inválido. Digite apenas números de 0 a 9, sem letras, espaços ou traços.")
        elif len(entrada) not in (10, 11):
            print(f"  [!] Quantidade incorreta de dígitos ({len(entrada)}). Esperado 10 (fixo) ou 11 (celular).")
        else:
            telefone_final = entrada
            telefone_valido = True
    return telefone_final


def ler_pergunta_pes():
    resposta_valida = False
    eh_ambidestro = False
    while not resposta_valida:
        entrada = input("\\nO atleta joga bem com os dois pés? (s/n): ").strip().lower()
        if entrada == "s":
            eh_ambidestro = True
            resposta_valida = True
        elif entrada == "n":
            eh_ambidestro = False
            resposta_valida = True
        else:
            print("  [!] Resposta inválida. Digite somente 's' para sim ou 'n' para não.")
    return eh_ambidestro


# ---------------------------------------------------------------------------
# CÁLCULOS E REGRAS DE NEGÓCIO
# ---------------------------------------------------------------------------
def calcular_nota(scores, bonus):
    soma = sum(scores[c] for c in CRITERIOS)
    media = soma / len(CRITERIOS)
    nota_final = media + bonus
    if nota_final > 10.0:
        nota_final = 10.0
    return round(nota_final, 2)


def processar_concierge_formulario():
    print("\n" + "=" * 55)
    print("  BACK-OFFICE CONCIERGE: PROCESSAMENTO DE TESTE REAL")
    print("=" * 55)

    nome = ler_nome()

    idade_valida = False
    idade = 0
    while not idade_valida:
        entrada_idade = input("Idade (12 a 21 anos): ").strip()
        if entrada_idade.isdigit():
            valor_idade = int(entrada_idade)
            if 12 <= valor_idade <= 21:
                idade = valor_idade
                idade_valida = True
            else:
                print("  [!] Idade fora da faixa permitida (12 a 21 anos).")
        else:
            print("  [!] Digite uma idade válida (apenas números).")

    print("\nPosições disponíveis:")
    for idx, pos in enumerate(POSICOES, start=1):
        print(f"  [{idx}] {pos}")
        
    posicao_valida = False
    posicao = ""
    while not posicao_valida:
        entrada_pos = input(f"Escolha a posição (1 a {len(POSICOES)}): ").strip()
        if entrada_pos.isdigit():
            idx_pos = int(entrada_pos)
            if 1 <= idx_pos <= len(POSICOES):
                posicao = POSICOES[idx_pos - 1]
                posicao_valida = True
            else:
                print(f"  [!] Opção fora do limite. Escolha de 1 a {len(POSICOES)}.")
        else:
            print("  [!] Digite apenas o número da opção.")

    cidade = ler_cidade()
    estado = ler_estado()

    pe_opcoes = ["Destro", "Canhoto"]
    print("\nPé dominante:")
    print("  [1] Destro\n  [2] Canhoto")
    pe_valido = False
    pe = ""
    while not pe_valido:
        entrada_pe = input("Escolha (1 ou 2): ").strip()
        if entrada_pe in ["1", "2"]:
            pe = pe_opcoes[int(entrada_pe) - 1]
            pe_valido = True
        else:
            print("  [!] Digite 1 para Destro ou 2 para Canhoto.")

    contato = ler_telefone()

    novo_id = f"A{len(atletas) + 1}"
    novo_atleta = {
        "id": novo_id,
        "nome": nome,
        "idade": idade,
        "posicao": posicao,
        "cidade": cidade,
        "estado": estado,
        "pe": pe,
        "contato": contato
    }
    atletas.append(novo_atleta)

    print("\n--- Digitação das Notas da Avaliação (0 a 10) ---")
    scores = {}
    for crit in CRITERIOS:
        nota_valida = False
        while not nota_valida:
            entrada_nota = input(f"Nota para {crit.capitalize()} (0 a 10): ").strip()
            if entrada_nota.isdigit():
                valor_nota = int(entrada_nota)
                if 0 <= valor_nota <= 10:
                    scores[crit] = valor_nota
                    nota_valida = True
                else:
                    print("  [!] A nota deve estar entre 0 e 10.")
            else:
                print("  [!] Digite um número inteiro.")

    ambidestro = ler_pergunta_pes()
    pe_bonus = 0.5 if ambidestro else 0.0

    comentario = input("\nParecer / Feedback do olheiro: ").strip()
    if not comentario:
        comentario = "Atleta avaliado durante a sessão de testes da peneira."

    nota_final = calcular_nota(scores, pe_bonus)
    if nota_final >= NOTA_APROVACAO:
        decisao = "aprovado"
    elif nota_final >= NOTA_APROVACAO - 1.0:
        decisao = "reavaliar"
    else:
        decisao = "reprovado"

    avaliacoes.append({
        "atleta_id": novo_id,
        "scores": scores,
        "pe_bonus": pe_bonus,
        "nota_geral": nota_final,
        "decisao": decisao,
        "comentario": comentario
    })

    print("\n" + "-" * 55)
    print("   RESULTADO GERADO PARA ENTREGA AO ATLETA")
    print("-" * 55)
    print(f"Atleta: {nome} (Código: {novo_id})")
    print(f"Posição: {posicao} | Idade: {idade} anos | Pé: {pe}")
    print(f"Contato: {contato} | Local: {cidade}/{estado}")
    print(f"Nota Final: {nota_final:.2f} / 10.0 (Bônus ambidestro: +{pe_bonus})")
    print(f"Veredito Oficial: {decisao.upper()}")
    print("\nNotas por fundamento:")
    for crit in CRITERIOS:
        print(f"  - {crit.capitalize():<12}: {scores[crit]}/10")
    print(f"Feedback: {comentario}")
    print("-" * 55)


def exibir_ranking():
    print("\n" + "=" * 55)
    print("              RANKING GERAL DA PENEIRA")
    print("=" * 55)
    
    tabela = []
    for a in atletas:
        notas_atleta = [av for av in avaliacoes if av["atleta_id"] == a["id"]]
        if notas_atleta:
            media = sum(av["nota_geral"] for av in notas_atleta) / len(notas_atleta)
            status = notas_atleta[-1]["decisao"]
            tabela.append({
                "id": a["id"],
                "nome": a["nome"],
                "posicao": a["posicao"],
                "media": media,
                "status": status
            })

    if not tabela:
        print("Nenhum atleta avaliado ainda.")
        return

    tabela.sort(key=lambda x: x["media"], reverse=True)

    print(f"{'Pos':<4}{'ID':<5}{'Nome':<22}{'Posição':<10}{'Média':<8}Status")
    print("-" * 55)
    for pos, item in enumerate(tabela, start=1):
        print(f"{pos:<4}{item['id']:<5}{item['nome'][:20]:<22}{item['posicao']:<10}{item['media']:<8.2f}{item['status']}")


def exibir_estatisticas():
    print("\n" + "=" * 55)
    print("         MÉTRICAS E DASHBOARD DE OPERAÇÃO")
    print("=" * 55)
    total_atletas = len(atletas)
    total_avaliacoes = len(avaliacoes)
    aprovados = sum(1 for av in avaliacoes if av["decisao"] == "aprovado")
    
    print(f"Total de atletas na base: {total_atletas}")
    print(f"Avaliações concluídas: {total_avaliacoes}")
    print(f"Aprovados: {aprovados}")

    if avaliacoes:
        matriz_criterios = [[av["scores"][c] for c in CRITERIOS] for av in avaliacoes]
        print("\nMédia geral dos critérios avaliados:")
        for col_idx, criterio in enumerate(CRITERIOS):
            soma_coluna = sum(linha[col_idx] for linha in matriz_criterios)
            media_criterio = soma_coluna / len(matriz_criterios)
            print(f"  - {criterio.capitalize():<12}: {media_criterio:.2f} / 10")


def listar_atletas():
    print("\n" + "=" * 55)
    print("               LISTA GERAL DE ATLETAS")
    print("=" * 55)
    for a in atletas:
        print(f"[{a['id']}] {a['nome']} — {a['posicao']} ({a['idade']} anos) — {a['cidade']}/{a['estado']}")


# ---------------------------------------------------------------------------
# MENU PRINCIPAL COM CONTROLE BOOLEANO
# ---------------------------------------------------------------------------
def main():
    executando = True
    while executando:
        print("\n" + "=" * 55)
        print("      PELÉ NEXT GEN — SISTEMA DE BACK-OFFICE (MVP)")
        print("=" * 55)
        print("  1. Inserir e processar teste real (Concierge)")
        print("  2. Ver ranking dos atletas")
        print("  3. Ver métricas gerais da seletiva")
        print("  4. Listar atletas cadastrados")
        print("  0. Sair")
        print("=" * 55)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            processar_concierge_formulario()
        elif opcao == "2":
            exibir_ranking()
        elif opcao == "3":
            exibir_estatisticas()
        elif opcao == "4":
            listar_atletas()
        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            executando = False
        else:
            print("\nOpção inválida, tente novamente.")


if __name__ == "__main__":
    main()