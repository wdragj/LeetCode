class Solution:
    def simplifyPath(self, path: str) -> str:
        path_str = []
        for i in range(1, len(path)):
            if i > 0 and path[i] == "/" and path[i] == path[i - 1]:
                continue
            path_str.append(path[i])
        path_str = "".join(path_str)
        path_name = path_str.split("/")
        stack = []
        for op in path_name:
            if op == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            elif op == "." or op == "":
                continue
            else:
                stack.append(op)
        return "/" + "/".join(stack)