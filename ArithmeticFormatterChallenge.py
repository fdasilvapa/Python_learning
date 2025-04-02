def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    problems_splited = []
    for problem in problems:
        splited = problem.split()
        problems_splited.append(splited)

    linha1_str = []
    linha2_str = []
    linha3_str = []
    linha4_str = []

    for problem in problems_splited:
        # Verifica se os números são válidos
        if not problem[0].isdigit() or not problem[2].isdigit():
            return "Error: Numbers must only contain digits."

        # Verifica se os números têm no máximo 4 dígitos
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Verifica se o operador é válido
        if problem[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Determina a largura do problema
        largura = max(len(problem[0]), len(problem[2])) + 2

        # Formata cada linha
        linha1 = (' ' * (largura - len(problem[0]))) + problem[0]
        linha2 = problem[1] + (' ' * (largura - len(problem[2]) - 1)) + problem[2]
        linha3 = '-' * largura

        linha1_str.append(linha1)
        linha2_str.append(linha2)
        linha3_str.append(linha3)

        if show_answers:
            resultado = int(problem[0]) + int(problem[2]) if problem[1] == '+' else int(problem[0]) - int(problem[2])
            linha4 = (' ' * (largura - len(str(resultado)))) + str(resultado)
            linha4_str.append(linha4)

    # Junta tudo com 4 espaços entre os problemas
    arranged_problems = '\n'.join([
        '    '.join(linha1_str),
        '    '.join(linha2_str),
        '    '.join(linha3_str)
    ] + (['    '.join(linha4_str)] if show_answers else []))

    return arranged_problems

# Teste
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)}')
