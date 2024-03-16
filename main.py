def identificar_sentimento(frase, palavras_positivas, palavras_negativas):

    palavras = frase.lower().split()

    contagem_positiva = 0
    contagem_negativa = 0
    palavra_anterior = None
    negacao_ativa = False

    negacoes = {"não", "nunca", "jamais", "nenhum"}

    for palavra in palavras:
        if palavra_anterior in palavras_positivas and not negacao_ativa:
            contagem_positiva += 1
        elif palavra_anterior in palavras_negativas and palavra_anterior not in negacoes and not negacao_ativa:
            contagem_negativa += 1

        palavra_anterior = palavra

        if palavra in palavras_positivas and not negacao_ativa:
            contagem_positiva += 1
        elif palavra in palavras_negativas and not negacao_ativa:
            contagem_negativa += 1
        elif palavra in negacoes:
            negacao_ativa = True

    # Ajuste para priorizar negatividade
    contagem_negativa *= 2

    if contagem_positiva > contagem_negativa or contagem_negativa == 0:
        return "positiva"
    elif contagem_negativa > contagem_positiva:
        return "negativa"
    else:
        return "neutra"

# Palavras positivas e negativas
palavras_positivas = {
    "bom", "boa", "ótimo", "maravilhoso", "maravilhosa", "excelente", "feliz", "alegre", 
    "divertido", "criativo", "amor", "sucesso", "ótima", "divertida", "criativa"
    "amável", "amigo", "satisfeito", "orgulho", "bonito", "satisfeito", "orgulhosa", "bonita", "orgulhoso"
    "gostei", "amei", "adoro", "adorei", "adorável", "incrível", "fantástico", "sim", "fantástico"
}

palavras_negativas = {
    "ruim", "péssimo", "péssima", "terrível", "horrível", "triste", "depressivo", "depressiva",
    "chato", "entediante", "aborrecido", "falta", "fracasso", "fracassado", "fracassada",
    "problema", "ódio", "inimigo", "cansado", "exausto", "preocupado", "inimigo", "cansada", "exausta"
    "inseguro", "feio", "detestei", "odiei", "aborreci", "não", "chata", "insegura", "feia"
}

frase = input("Insira a frase que deseja analisar:")

sentimento = identificar_sentimento(frase, palavras_positivas, palavras_negativas)
print("Sentimento da frase:", sentimento)
