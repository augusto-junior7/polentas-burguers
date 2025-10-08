def is_valid_cpf(cpf: str) -> bool:
    cpf = cpf.replace(".", "").replace("-", "")
    if not cpf.isdigit() or len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False

    def verifica_digito(cpf, peso):
        soma = 0
        for i in range(peso - 1):
            soma += int(cpf[i]) * (peso - i)
        resto = soma % 11
        if resto < 2:
            return int(cpf[peso - 1]) == 0
        return int(cpf[peso - 1]) == (11 - resto)

    try:
        return verifica_digito(cpf, 10) and verifica_digito(cpf, 11)
    except Exception:
        return False
