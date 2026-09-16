from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # store word at end node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w  # mark end of word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            nxt = node.children[ch]

            # Found a word
            if nxt.word:
                result.append(nxt.word)
                nxt.word = None  # avoid duplicates

            # Mark visited
            board[r][c] = "#"
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)
            board[r][c] = ch  # restore

            # Optimization: prune empty nodes
            if not nxt.children:
                node.children.pop(ch)

        # Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result
