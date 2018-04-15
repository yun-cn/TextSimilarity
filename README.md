## 文本相似度算法
  首先，在短文进行对比的时候，先把一些无关紧要的一的词语去掉，如 `的`, `是`,`在`等这类常用词。然后留下实际意义的一些词语。
 > Stop Words

假设我们过滤了一些没有实际意义的词语之后，我们仍然可以回遇到多个关键字，或许他们出现的次数一样多。但并不代表他们就至关重要。
比如说 `中国`，`蚂蚁`，`养殖`。显然`中国`这个词很常见单，相对于`蚂蚁`,`养殖`闲的就不是那么重要了。
也就是说，在关键字排序上，`蚂蚁`,`养殖`，就应该在`中国`的前面。

我们需要衡量一个重要性调整系数，衡量一个词是不是常见。如果某个词比较少见，但是它在这篇文章中多次出现，
那么它很可能就反映了这篇文章的特性，正是我们需要的关键字。

用统计学语言表达，就是在词频的基础上，要对每个词分配一个`重要性`权重。最常见的词（`的`,`是`,`在`）给与最小的权限。较为常见词（`中国`）给与较小的权重，较为常见的词（`蚂蚁`,`养殖`）给予较大的权重。这种权重叫做***逆文档频率***（Inverse Document Frequency 缩写IDF）,她的大小与一个词的常见程度成反比。

>逆文档词频

>创建文本向量

目的是将自由文本的每个文档转换为一个文本向量


## World2vec

在Gensim中实现word2vec模型非常简单，首先，我们需要将原始训练预料转换成一个`sentence`的一个迭代器；每一次跌单返回的`sentence`是一个word（utf-8格式）的列表
> 参考代码

```
class NySentences(object):
	def __init__(self, dirname)
		self.dirname  =  dirname

	def __iter__(self):
		for fname in os.listdir(self, dirname):
		for line in open(os.path.join(self.dirname, fname)):
		yield line.split()

sentences =  MySentences('/some/directory')  ## a memory-firendly iterator
```

接下来，我们用这个迭代器作为输入，构造一个Gensim内奸的word2vec模型的对象。
```
model = gensim.models.Word2Vec(sentences)
```

## Doc2vec

Doc2vec是在word2vec基础上提出的另一个用于计算长文本向量的工具。它的工作原理与Word2vec即为相似----
只是将长文本作为一个特殊的`token id`引入训练语料中。在Gensim中，doc2ver也是继承与word2vec的一个子类，因此，无论是API参数接口还是调用文本向量的方式，doc2vec和word2vec都即为相似。

主要区别是在对输入数据的预处理上。Doc2vec接受一个有`LabeledSentence`对象组成的迭代器作为其结构的输入参数。其中，`LabeledSentence`是Gensim内健的一个类，它接受两个List作为其初始化的参数， `word list` 和 `label list`。

```
from gensim.model.doc2vec import LabeledSentence
sentence = LabeledSentence(words = [u'some', u'words', u'here], tags=[u'SENT_1'])
```

准备好训练数据，模型的训练只是一行命令
```
  from gensim.models import Doc2vec
  model   =   Doc2Vec(dm = 1,  size = 100, window = 5, negative = 5, hs = 0, min_count = 2, workers = 4)
```
