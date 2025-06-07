class Solution:
    def simplifyPath(self, path: str) -> str:
        pathDirectory = []
        PATH_SPLIT = "/"
        PARENT = ".."
        directories = path.split(PATH_SPLIT)
        skipSet = {"", ".", ".."}

        for directory in directories:
            if pathDirectory and directory == PARENT:
                pathDirectory.pop()
            elif directory not in skipSet:
                pathDirectory.append(directory)

        return PATH_SPLIT + PATH_SPLIT.join(pathDirectory)
