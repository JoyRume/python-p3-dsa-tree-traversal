class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, target_id):
        return self._dfs(self.root, target_id)

    def _dfs(self, node, target_id):
        # this is the base node, if node is None, return None
        if node is None:
            return None
        
        # Check if the current node's id matches the target id
        if node['id'] == target_id:
            return node
        
        # Recurrently search in the children of the current node
        for child in node['children']:
            result = self._dfs(child, target_id)
            if result:
                return result
        
        # If target id is not found in the current subtree, return None
        return None
