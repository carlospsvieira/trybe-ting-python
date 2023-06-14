import os
import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_name = path_file

    # Check if the file has already been processed
    for item in instance:
        if item["nome_do_arquivo"] == file_name:
            return

    lines = txt_importer(path_file)
    file_data = {
        "nome_do_arquivo": file_name,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    instance.enqueue(file_data)

    sys.stdout.write(f"{file_data}\n")


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        removed_file = instance.dequeue()
        sys.stdout.write(f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso\n")



def file_metadata(instance, position):
    try:
        data = instance.search(position)
        sys.stdout.write(f"{data}\n")
    except IndexError:
        sys.stderr.write("Posição inválida\n")
