import jieba
import pandas

lines = pandas.read_csv("./data/user_post.csv")
contents = [str(it) for it in lines.iloc[:, 2]]
words = list()
for content in contents:
    words += [str(it) for it in jieba.cut(content)]
with open("words_in_post.txt", 'w') as f:
    f.write('\n'.join(words))
