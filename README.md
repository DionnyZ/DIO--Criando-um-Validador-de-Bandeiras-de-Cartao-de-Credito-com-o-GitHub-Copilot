# Criando um Validador de Bandeiras de Cartão de Crédito com o GitHub Copilot

O objetivo desse desafio foi utilizar o GitHub Copilot para gerar um código que valide e identifique a bandeira do cartão de crédito.

Foi gerado um código que faz a validação pela quantidade de dígitos, e identifica a bandeira pelo prefixo dos dígitos.

## Prompt

Desenvolva um algoritmo para validar e identificar a Bandeira do Cartão de crédito.

## Resposta

Segue um exemplo de algoritmo em Python para validar e identificar a bandeira de um cartão de crédito. O algoritmo utiliza o método de Luhn para validar o número do cartão e verifica os prefixos para identificar a bandeira.

```Python
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
```

Explicação:
1. Validação do Cartão:
- O método de Luhn é usado para verificar se o número do cartão é válido.
- Ele soma os dígitos do cartão, dobrando os dígitos alternados e ajustando os valores maiores que 9.

2. Identificação da Bandeira:
- Verifica os prefixos do número do cartão para determinar a bandeira (Visa, MasterCard, etc.).

3. Entrada e Saída:
- O usuário insere o número do cartão.
- O programa valida o número e identifica a bandeira.

Observação:

Certifique-se de que o número do cartão seja tratado com segurança e nunca armazene informações sensíveis em texto simples.
