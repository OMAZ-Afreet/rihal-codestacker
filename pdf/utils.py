from django.core.files.storage import default_storage


# from django.core.files.storage import FileSystemStorage

# from .exceptions import LocalSaveError, LocalDeleteError

# local_storage = FileSystemStorage()


# def local_save(pdf):
#     try:
#         return local_storage.save(f'temp/{pdf.name}', pdf)
#     except:
#         raise LocalSaveError(f'ERROR: local file SAVE failed -> {pdf.name}')


# def local_delete(pdf_path: str):
#     try:
#         local_storage.delete(pdf_path)
#     except:
#         raise LocalDeleteError(f'ERROR: local file DELETE failed -> {pdf_path}')


def get_file(name: str, mode='rb'):
    return default_storage.open(name, mode)

def delete_file(name: str):
    return default_storage.delete(name)