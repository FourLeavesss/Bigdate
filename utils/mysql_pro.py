# ORM外部配置
import collections
import os

from django.db.models import Sum
from snownlp import SnowNLP


def orm_standby():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IntelligentHome.settings")  # manage.py文件中有同样的环境配置
    import django
    django.setup()





def word_counts_action(text, top_number):
    """
        :param text:  统计的文本
        :param top_number:   输出词频前几
        :return: [('非常', 36), ('很', 31), ('手机', 23), ('也', 18)]
    """
    object_list = []
    # 文本预处理
    remove_words = [u'的', u'，', u'和', u'是', u'随着', u'对于', u'对', u'等', u'能', u'都', u'。', u' ', u'、', u'中', u'在', u'了',
                    u'通常', u'如果', u'我们', u'需要']  # 自定义去除词库
    seg_list_exact = SnowNLP(text).words  # 每一个数组评论分词
    for word in seg_list_exact:  # 循环读出每个分词
        if word not in remove_words:  # 如果不在去除词库中
            object_list.append(word)  # 分词追加到列表
    word_counts = collections.Counter(object_list)  # 对分词做词频统计
    word_top_number = word_counts.most_common(top_number)  # 获取前10最高频的词
    return word_top_number




if __name__ == '__main__':
    orm_standby()
    from database import models








