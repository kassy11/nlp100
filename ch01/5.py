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


# 文字列の場合
## 文字bi-gramの生成
text = "I am an NLPer"
char_bigrams = generate_ngrams(text, 2, type="moji")
print("文字bi-gram:", char_bigrams)

## 単語bi-gramの生成
word_bigrams = generate_ngrams(text, 2, type="tango")
print("単語bi-gram:", word_bigrams)

# リストの場合
## 文字bi-gramの生成
text = ["I", "am", "an", "NLPer"]
char_bigrams = generate_ngrams(text, 2, type="moji")
print("文字bi-gram:", char_bigrams)

## 単語bi-gramの生成
word_bigrams = generate_ngrams(text, 2, type="tango")
print("単語bi-gram:", word_bigrams)
