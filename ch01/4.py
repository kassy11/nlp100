sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

numbers = [1, 5, 6, 7, 8, 9, 15, 16, 19]
words = sentence.split(" ")

# TODO: 問題文の意味が良くわからない
result_dict = {}
for i in range(len(words)):
    if i + 1 in numbers:
        result_dict[words[i]] = i + 1
    else:
        result_dict[words[i]] = i + 1


print(result_dict)
