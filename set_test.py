test_set = set({"dog", "cat", "monkey"})
# Set型に要素を追加する
test_set.add("bird")
print(test_set)
# Set型は要素の順番を保持しないため取り出される要素は不定
# test_set.pop()
# print(test_set)

# 要素を指定して削除
test_set.remove("monkey")
print(test_set)

# frozenset型はset型を不変にした型なので要素の追加、変更はできない
test_frozenset = frozenset({"dog", "cat", "monkey"})
test_frozenset.add("bird")
print(test_frozenset)
