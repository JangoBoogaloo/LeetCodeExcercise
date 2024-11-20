from typing import List
from collections import defaultdict


class Directory:
    def __init__(self):
        # string -> Dir
        self.directories = {}
        # string (file name) -> string (file content)
        self.file_content_map = defaultdict(str)


class FileSystem:
    _ROOT_PATH = "/"
    _PATH_SEPARATOR = "/"

    def __init__(self):
        self._root = Directory()

    def ls(self, path: str) -> List[str]:
        current_dir = self._root
        ls_paths = []
        if path != self._ROOT_PATH:
            path_levels = path.split(self._PATH_SEPARATOR)
            for i in range(1, len(path_levels) - 1):
                current_dir = current_dir.directories[path_levels[i]]
            if path_levels[-1] in current_dir.file_content_map:
                ls_paths.append(path_levels[-1])
                return ls_paths
            else:
                current_dir = current_dir.directories[path_levels[-1]]

        ls_paths.extend(list(current_dir.directories.keys()))
        ls_paths.extend(list(current_dir.file_content_map.keys()))
        ls_paths.sort()
        return ls_paths

    def mkdir(self, path: str) -> None:
        current_dir = self._root
        path_levels = path.split(self._PATH_SEPARATOR)
        for level in path_levels[1:]:
            if level not in current_dir.directories:
                current_dir.directories[level] = Directory()
            current_dir = current_dir.directories[level]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path_levels = filePath.split(self._PATH_SEPARATOR)
        current_dir = self._root
        for level in path_levels[1:-1]:
            current_dir = current_dir.directories[level]
        current_dir.file_content_map[path_levels[-1]] += content

    def readContentFromFile(self, filePath: str) -> str:
        path_levels = filePath.split(self._PATH_SEPARATOR)
        current_dir = self._root
        for level in path_levels[1:-1]:
            current_dir = current_dir.directories[level]
        return current_dir.file_content_map[path_levels[-1]]
