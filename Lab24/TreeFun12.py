# Дано бинарное дерево с целыми числами в узлах и некоторое целое число S.
# Нужно найти в дереве все возможные пути, на которых сумма значений узлов будет равна S.

from TreeFun4 import TreeNode, BST


class PathFinderBST(BST):

    def find_paths_with_sum(self, target_sum):
        all_paths = []

        def dfs(node, current_sum, path):
            if not node:
                return

            current_path = path + [node.data]
            current_sum += node.data

            if not node.left and not node.right:
                if current_sum == target_sum:
                    all_paths.append(current_path)
                return

            dfs(node.left, current_sum, current_path)
            dfs(node.right, current_sum, current_path)

        dfs(self.root, 0, [])
        return all_paths


if __name__ == "__main__":
    try:
        with open('TreeWork.txt', 'r', encoding='utf-8') as f:
            line = f.readline()
            if line:
                values = [int(v) for v in line.split()]
            else:
                values = []
            S = int(f.readline().strip())
    except FileNotFoundError:
        print('Файл TreeWork.txt не найден')
        exit()

    print("Исходные данные из файла:", " ".join(map(str, values)))

    tree = PathFinderBST()
    tree.build_balanced(values)

    print("\nСтруктура получившегося дерева:")
    tree.print_tree_visual()
    paths = tree.find_paths_with_sum(S)

    print(f"\nРезультат поиска путей с суммой S = {S}:")
    if not paths:
        print("-1")
    else:
        for path in paths:
            print(" -> ".join(map(str, path)))