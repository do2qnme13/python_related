def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        if '+' in problem:
            operator = '+'
            num1, num2 = problem.split(' + ')
        elif '-' in problem:
            operator = '-'
            num1, num2 = problem.split(' - ')
        elif '*' in problem or '/' in problem:
            return "Error: Operator must be '+' or '-'."
        else:
            return "Error: Operator must be '+' or '-'."

        if not num1.strip().isdigit() or not num2.strip().isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1.strip()) > 4 or len(num2.strip()) > 4:
            return "Error: Numbers cannot be more than four digits."

        num1 = num1.strip()
        num2 = num2.strip()
        width = max(len(num1), len(num2)) + 2  # +2 for operator and space

        first_line.append(num1.rjust(width))
        second_line.append(operator + ' ' + num2.rjust(width - 2))
        dashes.append('-' * width)

        if show_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            results.append(result.rjust(width))

    arranged_problems = (
        '    '.join(first_line) + '\n' +
        '    '.join(second_line) + '\n' +
        '    '.join(dashes)
    )

    if show_answers:
        arranged_problems += '\n' + '    '.join(results)

    return arranged_problems
