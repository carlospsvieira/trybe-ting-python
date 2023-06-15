def exists_word(word, instance):
    result = []

    for file in instance:
        occurrences = []

        for i, line in enumerate(file["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                occurrences.append({"linha": i})

        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return result


def search_by_word(word, instance):
    results = []
    for data in instance:
        file_name = data.get("nome_do_arquivo")
        lines = data.get("linhas_do_arquivo")
        occurrences = []
        for line_number, line_content in enumerate(lines, 1):
            if word in line_content.lower():
                occurrence = {
                    "conteudo": line_content.strip(),
                    "linha": line_number,
                }
                occurrences.append(occurrence)
        if occurrences:
            result = {
                "arquivo": file_name,
                "ocorrencias": occurrences,
                "palavra": word,
            }
            results.append(result)
    return results
