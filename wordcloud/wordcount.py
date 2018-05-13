import jieba

string ='''
从MVP开发模式至今，其实已经过了好久；很多开发者也已经轻车熟路的运用到了项目中，本来犹豫要不要写这篇文章，后来发现还是有人在问MVP怎么用，于是有了这篇文章。
MVP模式本身其实很简单，一些开发者难以理解，或许是因为要么直接一个Demo下来了，要么一些资料写的思路不是那么清晰，那么本篇文章以几个问题作为引导，先帮助不理解的开发者们了解一下MVP的理念是什么，关于架构理念的理解，也可以参考之前的
移动架构这么多，如何一次搞定所有1. 为什么使用MVP模式？答：这个问题其实问的是MVP的使用场景。每个项目的规模不同，业务不同，适用于不同的开发模式与架构，不要为了使用架构而去引入架构，要先问一下开发者自己，当前项目需要架构么？当前项目适合什么样的架构？架构千千万，但不是所有的架构都具有普适性。这个问题的目的其实是问MVP模式能解决什么问题？那么我们来分析一下。
为什么引入架构呢？如果一个项目，每个类3-500行代码就解决了，引入架构也就是玩玩而已。这时候重度引入架构反而影响了运行效率，得不偿失。 引入架构的项目，必是到了一定的规模，也就是出现了一定程度的耦合与冗余，也一定意义上违反了面向对象的单一职责原则。
那么MVP解决的问题就很明显了， 那就是冗余、混乱、耦合重。此时抛开MVP不讲，如果要我们自己想办法去解决，如何来解决呢？
分而治之， 我们可能会想到，根据单一职责原则，Activity或Fragment或其他组件冗余了，那么必然要根据不同的功能模块，来划分出来不同的职责模块，这样也就遵循了单一职责的原则。站在前人的智慧上，或许很多人就想到了M(Model)V(View)C(Controller)。我们可以借鉴这一开发模式，来达到我们的目的，暂时将一个页面划分为
UI模块，也即View层Model模块，也即数据请求模块Logic模块， 司逻辑处理这样划分首先职责分工就明确了，解决了混乱，冗余的问题。其实，一个项目从分包，到分类，最后拆分方法实现，都是遵从单一职责；一个职责划分越具有原子性， 它的重用性就越好，当然这也要根据实际业务而定。比如以下代码
'''
f = open('斗破苍穹.txt').read()
# result = jieba.cut(string)
jieba.add_word('恐怖如斯')
jieba.add_word('佛怒火莲')
jieba.add_word('凤毛麟角')
jieba.add_word('凉气')
result = jieba.cut(f)
print(result)
mywordlist=dict()
for myword in result:
    if myword not in ['恐怖如斯', '佛怒火莲', '凤毛麟角','凉气']:
        continue
    if myword.strip() in [',', '.', '。', '，','\\n',';','...']:
        continue
    if len(myword.strip()) < 2:
        continue
    if myword not in mywordlist:
        mywordlist[myword] = 1
    else:
        mywordlist[myword] += 1
    # if not (myword.strip() in [',','.','。','，']) and len(myword.strip()) > 1:
    #     mywordlist.append(myword)
mywordlist = sorted(mywordlist.items(), key=lambda d: d[1], reverse=True)[:10]
print(mywordlist)
# from collections import Counter
# c = Counter(mywordlist).most_common(30)
# print(c)
