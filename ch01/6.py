# 5と同じ
def generate_ngrams(sentence, n, type="tango"):
    if type != "tango" and type != "moji":
        return
    # n-gram生成
    ngrams = []
    if type == "tango":
        if isinstance(sentence, str):
            # 文字列の場合は空白を削除してリストに変換
            sentence_list = sentence.strip().split()
        elif isinstance(sentence, list):
            # リストの場合は空白を削除
            sentence_list = [word.strip() for word in sentence]

        for i in range(len(sentence_list) - n + 1):
            ngrams.append(tuple(sentence_list[i : i + n]))
    if type == "moji":
        if isinstance(sentence, str):
            # 文字列の場合は空白を削除してリストに変換
            sentence = sentence.strip().replace(" ", "")
        elif isinstance(sentence, list):
            sentence = "".join(sentence).strip()

        for i in range(len(sentence) - n + 1):
            ngrams.append(tuple(sentence[i : i + n]))

    return ngrams


sentence1 = "paraparaparadise"
sentence2 = "paragraph"

x = set(generate_ngrams(sentence1, 2, "moji"))
y = set(generate_ngrams(sentence2, 2, "moji"))
# 和集合
print(x | y)
# 積集合
print(x & y)
# 差集合
print(x - y)
print(y - x)

se = ("s", "e")
if se in x:
    print("xに'se'が含まれています")
elif se in y:
    print("yに'se'が含まれています")
