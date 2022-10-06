def biggestPath(file_system: dict) -> str:
    biggest_path = ''
    path = '/'
    for current_dir in file_system:
        if isinstance(file_system[current_dir], dict):
            path += f"{current_dir}"
            if to_add := biggestPath(file_system[current_dir]):
                path += f"{to_add}"

        if len(path) > len(biggest_path):
            biggest_path = path
        path = '/'
    return biggest_path


if __name__ == "__main__":
    paths = {'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': {}}}}}
    biggestPath(file_system=paths)
