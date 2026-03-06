def verificador_media(media:int|float) -> str:
    """Esta função retorna se o aluno passou ou não de ano"""

    if not isinstance(media, (int, float)):
        raise TypeError ("Tipo inválido, a entrada deve ser numérico")

    if media >= 7:
        return "Aprovado"
    elif media < 4:
        return "Reprovado"
    else:
        return "Recuperação"


if __name__ == "__main__":
    print(verificador_media(7))
