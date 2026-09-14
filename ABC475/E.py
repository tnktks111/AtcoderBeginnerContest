class _TrieNode:

    def __init__(self) -> None:
        self.o: _TrieNode | None = None
        self.x: _TrieNode | None = None
        self.cnt = 0

class Trie:
    def __init__(self, ans:str, m:int) -> None:
        self._root = _TrieNode()
        self.answer = ans
        self.m = m

    def insert(self, word: str):
        node: _TrieNode = self._root
        node.cnt += 1
        for char in word:
            if char == "o":
                if node.o is None:
                    node.o = _TrieNode()
                next_node = node.o
            else:
                if node.x is None:
                    node.x = _TrieNode()
                next_node = node.x
            node = next_node
            node.cnt += 1

    def delete(self, word: str):
        node: _TrieNode = self._root
        node.cnt -= 1

        for char in word:
            if char == "o":
                next_node = node.o
            else:
                next_node = node.x
            node = next_node
            node.cnt -= 1

    def judge(self, word: str):
        cur = self._root
        passed = 0

        for i, correct_char in enumerate(self.answer):

            if correct_char == "o":
                correct = cur.o
                wrong = cur.x
            else:
                correct = cur.x
                wrong = cur.o

            correct_cnt = 0 if correct is None else correct.cnt

            if passed + correct_cnt <= self.m:
                if word[i] == correct_char:
                    return True

                passed += correct_cnt
                cur = wrong

            else:
                if word[i] != correct_char:
                    return False

                cur = correct

        return False

N, M, K = map(int, input().split())
T = input()
trie = Trie(T, M)

S = []
for _ in range(N):
    s = input()
    trie.insert(s)
    S.append(s)

Q = int(input())
for _ in range(Q):
    i, j = map(lambda x: int(x) - 1, input().split())
    prv = S[i]
    new_char = "o" if prv[j] == "x" else "x"
    nxt = S[i][:j] + new_char + S[i][j + 1:]
    S[i] = nxt
    trie.delete(prv)
    trie.insert(nxt)
    if trie.judge(nxt):
        print("Yes")
    else:
        print("No")