def validar_cartao(numero_cartao):
    """
    Valida o número do cartão de crédito usando o algoritmo de Luhn.
    """
    numero_cartao = numero_cartao.replace(" ", "")  # Remove espaços
    if not numero_cartao.isdigit():
        return False

    soma = 0
    alternar = False

    for digito in reversed(numero_cartao):
        n = int(digito)
        if alternar:
            n *= 2
            if n > 9:
                n -= 9
        soma += n
        alternar = not alternar

    return soma % 10 == 0


def identificar_bandeira(numero_cartao):
    """
    Identifica a bandeira do cartão de crédito com base nos prefixos.
    """
    numero_cartao = numero_cartao.replace(" ", "")  # Remove espaços

    if numero_cartao.startswith(("34", "37")):
        return "American Express"
    elif numero_cartao.startswith("4"):
        return "Visa"
    elif numero_cartao.startswith(("51", "52", "53", "54", "55")):
        return "MasterCard"
    elif numero_cartao.startswith("6011") or numero_cartao[:3] in ("644", "645", "646", "647", "648", "649") or numero_cartao[:2] == "65":
        return "Discover"
    elif numero_cartao.startswith("35"):
        return "JCB"
    elif numero_cartao.startswith("36") or numero_cartao.startswith("38"):
        return "Diners Club"
    else:
        return "Bandeira desconhecida"


# Exemplo de uso
numero_cartao = input("Digite o número do cartão de crédito: ")

if validar_cartao(numero_cartao):
    bandeira = identificar_bandeira(numero_cartao)
    print(f"Cartão válido. Bandeira: {bandeira}")
else:
    print("Número do cartão inválido.")