from pathlib import Path
from muselearn.src.helpers.errors import FileExistsError2




def input_file_path(directory: str, file_name: str) -> Path:
    """Given the string paths to the result directory, and the input  file
    return the path to the  file.
    1. check if the input_file is an absolute path, and if so, return that.
    2. if the input_file is a relative path, combine it with the result_directory
       and return that.
    The resultant path must exist and be a file, otherwise raise an FileNotFoundException.
    """
    path_to_file = Path(file_name)
    if path_to_file.is_absolute() and path_to_file.is_file():
        return path_to_file

    input_directory_path = Path(directory)
    path_to_file = input_directory_path / path_to_file

    if path_to_file.is_file():
        return path_to_file.resolve()
    else:
        raise FileNotFoundError(
            'did not find the input file using result_directory={directory}, input_file={input_file}'.format(
                directory=directory, input_file=file_name
            )
        )


def output_file_path(directory: str, file_name: str, mode: str='protected') -> Path:
    """Given the string paths to the result directory, and the input  file
    return the path to the  file.
    1. check if the input_file is an absolute path, and if so, return that.
    2. if the input_file is a relative path, combine it with the result_directory
       and return that.
    The resultant path must exist and be a file, otherwise raise an FileNotFoundException.
    """
    path_to_file = Path(file_name)
    if path_to_file.is_absolute() and not path_to_file.exists():
        return path_to_file

    output_directory_path = Path(directory)
    path_to_file = output_directory_path / path_to_file

    if not path_to_file.exists():
        return path_to_file
    else:
        if mode == 'protected':
            raise FileExistsError2(
                'disallowing overwriting file using result_directory={directory}, output_file={output_file}'.format(
                    directory=directory, output_file=file_name)
                , directory, file_name)
        elif mode == 'overwrite':
            return path_to_file