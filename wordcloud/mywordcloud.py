# - * - coding: utf - 8 -*-
import jieba
jieba.enable_parallel(4)
# Setting up parallel processes :4 ,but unable to run on Windows
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

d = path.dirname(__file__)

stopwords_path = '/home/zhiwen/code/github/test/wordcloud/wc_cn/stopwords_cn_en.txt'

# Chinese fonts must be set
font_path = '/usr/share/fonts/truetype/arphic/uming.ttc'

# the path to save worldcloud
# imgname1 = d + '/wc_cn/LuXun.jpg'

# read the mask / color image taken from
back_coloring = imread('/home/zhiwen/code/github/test/wordcloud/wc_cn/LuXun_color.jpg')

# Read the whole text.
text = open(path.join(d, '斗破苍穹.txt')).read()

# if you want use wordCloud,you need it
# add userdict by add_word()
userdict_list = ['单四嫂子','恐怖如斯','海波东']


# The function for processing text with Jieba
def jieba_processing_txt(text):
    for word in userdict_list:
        jieba.add_word(word)

    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr = "/ ".join(seg_list)

    with open(stopwords_path, encoding='utf-8') as f_stop:
        f_stop_text = f_stop.read()
        f_stop_seg_list = f_stop_text.split('\n')

    for myword in liststr.split('/'):
        if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
            mywordlist.append(myword)
    return ' '.join(mywordlist)


wc = WordCloud(font_path=font_path, background_color="white", max_words=1000,
               random_state=42, width=1000, height=500, margin=2,)


wc.generate(jieba_processing_txt(text))

# create coloring from image
# image_colors_default = ImageColorGenerator(back_coloring)

plt.figure()
# recolor wordcloud and show
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

# save wordcloud
wc.to_file('text.jpg')

# create coloring from image
# image_colors_byImg = ImageColorGenerator(back_coloring)

# show
# we could also give color_func=image_colors directly in the constructor
# plt.imshow(wc.recolor(color_func=image_colors_byImg), interpolation="bilinear")
# plt.axis("off")
# plt.figure()
# plt.imshow(back_coloring, interpolation="bilinear")
# plt.axis("off")
# plt.show()

# save wordcloud
# wc.to_file(path.join(d, imgname2))

# import jieba

# f = open('content.txt').read()
# # print(f)
# /usr/share/fonts/truetype/arphic/uming.ttc
# result = jieba.cut(f)

# print(result)
# print('/'.join(result))
