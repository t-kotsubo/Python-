items = {'note': 1, 'notebook': 2, 'sketchbook': 3}

print(items['macbook'])

print(items.get('macbook'))

# 重要
# 辞書は変数名[キー]の場合は存在しないキーを指定した場合はKeyErrorが発生する
# キーエラーを発生させたくない場合はget()を使う。キーが存在しない場合はNoneを返す/Users/t_kotsubo/Google ドライブ/ StudyPrograming/Python/Python-/dict_test.py
