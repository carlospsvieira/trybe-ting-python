import os
import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_name = os.path.basename(path_file)
    file_data = {}

    for item in instance:
        if item["nome_do_arquivo"] == file_name:
            return

    lines = txt_importer(path_file)
    file_data["qtd_linhas"] = len(lines)
    file_data["linhas_do_arquivo"] = lines
    file_data["nome_do_arquivo"] = path_file

    instance.append(file_data)

    sys.stdout.write(f"{file_data}\n")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
