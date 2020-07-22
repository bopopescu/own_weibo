
/home/ubuntu3/linhao/dogapi
scrapy crawl friends_spider -a users_txt=group.txt -a ftype=1 -a since_idx=1 -a max_idx=1184 --loglevel=INFO --logfile=group.log #>>写入日志文件

scrapy crawl weibo_user_spider -a users_txt="group.txt" -a mtype=2 -a since_idx=1 -a max_idx=1184 --loglevel=INFO --logfile=weibo_group.log

    id = Field() # 用户UID, 2854532022,
 10     # idstr = Field() # 字符串型用户ID, 与id字段重复, 不用存, "2854532022"
 11     class_type = Field() # 1, ?
 12     screen_name = Field() # "Come_On_TAO", 用户昵称
 13     name = Field() # "Come_On_Tao", 友好显示名称
 14     province = Field() # "100", 用户所在省级ID
 15     city = Field() # "1000", 用户所在城市ID
 16     location = Field() # "\u5176\u4ed6", 用户所在地
 17     description = Field() # 用户自我描述
 18     url = Field() # 用户博客地址
 19     profile_image_url = Field() # 用户头像地址（中图），50×50像素
 20     profile_url = Field() # 用户的微博统一URL地址, http://weibo.com/profile_url就是用户微博主页
 21     domain = Field() # 用户个性化URL, 同上
 22     weihao = Field() # 用户的微号(新浪微博用户个性化纯数字号码), ""
 23     gender = Field() # 用户性别, 'f'
 24     followers_count = Field() # 粉丝数
 25     friends_count = Field() # 关注数
 26     pagefriends_count = Field() # ?
 27     statuses_count = Field() # 微博数
 28     favourites_count = Field() # 收藏数
 29     created_at = Field() # 注册日期, "Thu Jun 28 21:13:09 +0800 2012"
 30     timestamp = Field() # created_at字段转化而来的时间戳
 31     following = Field() # false, ?
 32     allow_all_act_msg = Field() # true, 是否允许所有人给我发私信，true：是，false：否
 33     geo_enabled = Field() # 是否允许标识用户的地理位置, false
 34     verified = Field() # 加V标示，是否微博认证用户, false
 35     verified_type = Field() # 用户认证类型, -1
 36     ptype = Field() # 0
 37     allow_all_comment = Field() # 是否允许所有人对我的微博进行评论
 38     avatar_large = Field() # 用户头像地址（大图），180×180像素
 39     avatar_hd = Field() # 用户头像地址（高清），高清头像原图
 40     verified_reason = Field() # 认证原因, ""
 41     verified_trade = Field() # "", ?
 42     verified_reason_url = Field() # "", ?
 43     verified_source = Field() # "", ?
 44     verified_source_url = Field() # "", ?
 45     follow_me = Field() # false, 该用户是否关注当前登录用户，true：是，false：否
 46     online_status = Field() # 用户的在线状态，0：不在线、1：在线
 47     bi_followers_count = Field() # 用户的互粉数
 48     lang = Field() # 用户当前的语言版本，"zh-cn"：简体中文，"zh-tw"：繁体中文，"en"：英语
 49     star = Field() # 0, ?
 50     mbtype = Field() # 12, ?
 51     mbrank = Field() # 5, ?
 52     block_word = Field() # 1, ?
 53     block_app = Field() # 1, ?
 54     credit_score = Field() # ?
 55
 56     cover_image = Field() # 用户封面地址
 57     cover_image_phone = Field() # ?
 58     ulevel = Field() # 0, ?
 59     badge_top = Field() # "", ?
 60     extend = Field() # ?, {"privacy":{"mobile":0},"mbprivilege":"0000000000000000000000000000000000000000000000000000000000000000"}
 61     remark = Field() # "" ?
 62     verified_state = Field() # 0
 63     # uids list
 64     followers = Field() # just uids
 65     friends = Field() # just uids
 66     # 自定义字段
 67     first_in = Field()
 68     last_modify = Field()

 70     # utils.py中解析返回数据的字段
 71     RESP_ITER_KEYS = ['id', 'name', 'screen_name', 'class_type', 'gender', 'province', 'city', 'location', 'url', 'domain', \
 72     'geo_enabled', 'verified', 'verified_type', 'description', \
 73     'followers_count', 'statuses_count', 'friends_count', 'favourites_count', \
 74     'profile_image_url', 'allow_all_act_msg', 'created_at', 'verified_reason']
 75 ····
 76     # mongodb pipelines中更新的字段
 77     PIPED_UPDATE_KEYS = ['name', 'class_type', 'gender', 'province', 'city', 'location', 'url', 'domain', \
 78     'geo_enabled', 'verified', 'verified_type', 'description', \
 79     'followers_count', 'statuses_count', 'friends_count', 'favourites_count', \
 80     'profile_image_url', 'allow_all_act_msg', 'created_at', 'verified_reason']
 81
  class WeiboItem_search(Item):
106     """
107     search spider，字段值中有转义符
108     """
109     #mmid = Field()
110     id = Field() # 16位微博ID, 3752470516005693
111     uid = Field() # just uid, 用户uid
112     user = Field() # user info dict
113     mid = Field() # 16位微博ID, "3752470516005693"
114     created_at = Field() # 微博创建时间, "Mon Sep 08 10:09:10 +0800 2014"
115     timestamp = Field() # created_at字段转化而来的时间戳
116     text = Field() # unicode, 微博信息内容
117     source = Field() # 微博来源, <a href=\"http:\/\/app.weibo.com\/t\/feed\/8crQy\" rel=\"nofollow\">Weico.iPhone<\/a>",
118
119     favorited = Field() # false, 是否已收藏，true：是，false：否
120     truncated = Field() # false, 是否被截断，true：是，false：否
121     in_reply_to_status_id = Field() # "", 回复ID
122     in_reply_to_user_id = Field() # "", 回复人UID
123     in_reply_to_screen_name = Field() # "", 回复人昵称
124     geo = Field() # null, 地理信息字段
125     reposts_count = Field() # 转发数
126     comments_count = Field() # 评论数
127     attitudes_count = Field() # 赞数
128     mlevel = Field() # 0, ?
129     visible = Field() # 微博的可见性及指定可见分组信息, 该object中type取值，0：普通微博，1：私密微博，3：指定分组微博，4：密友微博; list_id为分组130 ····
131     pic_ids = Field() # queryWeiboBykw返回该字段, 微博配图id, 多图时返回多图id, 无配图返回“[]”, 转发微博无法配图此字段为[]
132     pic_ids = Field() # queryUserWeibo返回该字段, [{"thumbnail_pic": "http://ww4.sinaimg.cn/thumbnail/475b3d56gw1ek4vgg9x3xj20c60ee0t7.jpg"},]
133 ····
134     pid = Field() # 3752469458416290, ?, 原创微博无该字段
135     thumbnail_pic = Field() # 缩略图片地址，没有时不返回此字段, 转发微博无法配图不返回该字段
136     bmiddle_pic = Field() # 中等尺寸图片地址，没有时不返回此字段, 转发微博无法配图不返回该字段
137     original_pic = Field() # 原始图片地址，没有时不返回此字段, 转发微博无法配图不返回该字段
138     retweeted_status = Field() # 源微博dict
139     annotations = Field() # ?, 转发微博无该字段，原创微博有该字段, [{"client_mblogid":"iPhone-2849F7C0-695E-4C50-B9A9-101770EEFC70"}]
140     reposts = Field() # just mids, 转发微博id列表
141     comments = Field() # just ids, 评论微博id列表
142     category = Field() # 31, ?, 转发微博有该字段，原创微博无该字段
143
144     floor_num = Field() # 楼号 3
145     reply_comment = Field() # 回复的评论mid
146
147     keywords = Field() # search接口定义的话题关键词
148
149     # ad = Field() # 微博流内的推广微博ID, 没有该字段
150     # url_objects = Field() # 有该字段，但太长没有必要，?
151     # idstr = Field() # 16位微博ID, 和mid重复不用存, 字符串型微博ID, "3752470516005693"
152     # darwin_tags = Field() # [], ?
153
154     # 自定义字段
155     first_in = Field()
156     last_modify = Field()
157
158     search_type = Field()
159
160     RESP_ITER_KEYS = ['created_at', 'id', 'mid', 'mmid',  'text', 'source', 'favorited', 'truncated', \
161     'in_reply_to_status_id', 'in_reply_to_user_id', 'in_reply_to_screen_name', \
162     'pic_ids', 'thumbnail_pic', 'geo', 'reposts_count', 'comments_count', \
163     'attitudes_count']
164
165     PIPED_UPDATE_KEYS = ['created_at', 'source', 'favorited', 'truncated', \
    	'in_reply_to_status_id', 'in_reply_to_user_id', 'in_reply_to_screen_name', \
167     'pic_ids', 'thumbnail_pic', 'geo', 'reposts_count', 'comments_count', \
168     'attitudes_count']




sublime的配置文件
{  
    "cmd": ["python", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python",
    "path":"E:/python"
}

commend + P 文件切换
commend + R 函数切换、   commend+shift+R 不同文件的函数切换

python 环境变量
pip  环境变量
anaconda  python相关包的安装包

在开始目录里加上其他组件   C:\Users\NaNa\Anaconda2\Scripts 里面也有
conda update menuinst
conda install -f console_shortcut ipython ipython-notebook ipython-qtconsole launcher spyder

matplotlib里面箱图的属性
boxplot(self, x, notch=None, sym=None, vert=None, whis=None,
        positions=None, widths=None, patch_artist=False,
        bootstrap=None, usermedians=None, conf_intervals=None,
        meanline=False, showmeans=False, showcaps=True,
        showbox=True, showfliers=True, boxprops=None, labels=None,
        flierprops=None, medianprops=None, meanprops=None,
        capprops=None, whiskerprops=None, manage_xticks=True):


pip install numpy 可以直接装
pip install openblas

print a.shape
expElogbetad = self.expElogbeta[:, ids]   取所有行的第ids这些列

> use tourism
switched to db tourism
> show collections
hongkong_1000
hongkong_duplicate
system.indexes
> db.hongkong_1000.findOne()


mongodb:::
mongoVUE  可视化界面
安装好后找到mongodb的路径
cd 'c:\programe files\mongodb\server\3.2\bin'
创建一个存放数据的文件夹
mongod --dbpath=e:\data

http://my.oschina.net/chiyong/blog/599326  启动引擎，默认是tiger，是否需要mmapv1
  mongod --storageEngine wiredTiger  --dbpath 数据目录
  mongod  --storageEngine mmapv1 --dbpath=e:\data    数据目录

打开两边的mongo，可以传数据

ERROR: listen(): bind() failed errno:98 Address already in use for socket: 0.0.0.0:27017
因为已经开了一个，把进行kill掉，重新打开

conn = pymongo.MongoClient()
collc = conn.mongo_data.tsai
a = collc.find_one({"comment_count":385})


db.stats()
db.XXX.stas()
查看数据库和表的大小

连接远程时conn = pymongo.MongoClient(host='219.224.134.212',port=27017)

219.224.134.212
Step1、使用Bitvise SSH工具连接服务器
Step2、在ssh terminal中使用tmux，新建会话，输入如下命令，启动Mongod服务，并保持会话持续运行
 cd /home/mongodb/bin
./mongod --dbpath=./data/db

因为mongo的shell是用的javascript，javascript的object的property的名称是数字的时候，不能用“.”来表示，所以你需要：
1
db.getCollection('201405081400').renameCollection('exam');

win下命令用""


转码：
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

写入csv文件：
path='./content_withblock.csv'
csvfile=open(path,'wb')
writer=csv.writer(csvfile)

try-except的形式；writerow的时候要加[]，否则会切成一个一个字:     
for i in collc.find():
    try:
        a.append([i['content']])
        writer.writerow([i['content']])
    except KeyError:
        pass


TextRank 算法可以用来从文本中提取关键词和摘要（重要的句子）。TextRank4ZH是针对中文文本的TextRank算法的python算法实现。

结巴分词  selfword自己添加的新词  n名词

这里的defaultdict(function_factory)构建的是一个类似dictionary的对象，其中keys的值，自行确定赋值，但是values的类型，是function_factory的类实例，而且具有默认值。比如default(int)则创建一个类似dictionary对象，里面任何的values都是int的实例，而且就算是一个不存在的key, d[key] 也有一个默认值，这个默认值是int()的默认值0.


关键词提取 
jieba.analyse.extract_tags(sentence,topK) #需要先import jieba.analyse
setence为待提取的文本
topK为返回几个TF/IDF权重最大的关键词，默认值为20 


标注句子分词后每个词的词性，采用和ictclas兼容的标记法 
用法示例

>>> import jieba.posseg as pseg
>>> words = pseg.cut("我爱北京天安门")
>>> for w in words:
...    print w.word, w.flag
...
我 r
爱 v
北京 ns
天安门 ns

分词
list(jieba.cut(...))转化为list    不转成list的话就是个游标

jieba.load_userdict(file_name) # file_name为自定义词典的路径
词典格式和dict.txt一样，一个词占一行；每一行分三部分，一部分为词语，另一部分为词频，最后为词性（可省略），用空格隔开 
范例： 
自定义词典：
云计算 5
李小福 2 nr
创新办 3 i
easy_install 3 eng
好用 300
韩玉赏鉴 3 nz

并行分词
jieba.enable_parallel(4) # 开启并行分词模式，参数为并行进程数
jieba.disable_parallel() # 关闭并行分词模式


frequency = defaultdict(int)
这里的defaultdict(function_factory)构建的是一个类似dictionary的对象，其中keys的值，自行确定赋值，但是values的类型，是function_factory的类实例，而且具有默认值。比如default(int)则创建一个类似dictionary对象，里面任何的values都是int的实例，而且就算是一个不存在的key, d[key] 也有一个默认值，这个默认值是int()的默认值0.


nltk自然语言处理  分词、停用词...

正则
使用re的一般步骤是先使用re.compile()函数，将正则表达式的字符串形式编译为Pattern实例，然后使用Pattern实例处理文本并获得匹配结果（一个Match实例），最后使用Match实例获得信息，进行其他的操作。
举一个简单的例子，在寻找一个字符串中所有的英文字符：
import re
pattern = re.compile('[a-zA-Z]')
result = pattern.findall('as3SiOPdj#@23awe')
print result
# ['a', 's', 'S', 'i', 'O', 'P', 'd', 'j', 'a', 'w', 'e']

>>> import re
# 编译:
>>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
>>> re_telephone.match('010-12345').groups()
('010', '12345')
>>> re_telephone.match('010-8086').groups()
('010', '8086')

解决'ascii' codec can't encode characters in position 12-15
import sys
reload(sys)
sys.setdefaultencoding('utf8')  
不管用：
        for k,v in keywords_dict_list.iteritems():
            print k,v  还是会报错
改成：
        for k,v in keywords_dict_list.iteritems():
            print k.encode('utf8'),v




恩，建议你存在mysql里的文字，都以unicode的形式存
这样比较不容易出错


str是字节串，由unicode经过编码(encode)后的字节组成的
unicode才是真正意义上的字符串，由字符组成
s = ‘中文‘ s = u‘中文‘.encode(‘utf-8‘)  >>> type(‘中文‘) <type ‘str‘> 
s = u‘中文‘ s = ‘中文‘.decode(‘utf-8‘) s = unicode(‘中文‘, ‘utf-8‘)  >>> type(u‘中文‘) <type ‘unicode‘> 
对的处理方法(str.decode/unicode.encode),不要对str使用encode，不要对unicode使用decode

不同编码转换,使用unicode作为中间编码:
#s是code_A的str s.decode(‘code_A‘).encode(‘code_B‘) 

直接存成了
a="[u'\u8f6c\u53d1\u5fae\u535a']"这样的字符串
读的时候eval(a)。。。。。不过代码有危险

到系统地址、目录下
import os
for files in os.listdir(r'C:\Users\NaNa\DataScraperWorks\jiang0li0na'):
    if 'jian' in files:
        files_name.append(files)


读取xml：
for files in files_name:
    dom = ml.parse('C:\Users\NaNa\DataScraperWorks\jiang0li0na\\'+files)
    root = dom.documentElement
    uid = root.getElementsByTagName('uid')
    name = root.getElementsByTagName('name')
    for j in range(0,len(uid)-1):
        uid0 = uid[j].firstChild.data
        uid0 = re.findall(r'id=(.*)&',uid0)
        uids.append(str(uid0[0]))
        unames.append(name[j].firstChild.data)

爬虫软件：
gooseeker  集搜客；跟firefox一起用


anaconda安装包:
conda install opencv

import os
#获取当前工作目录
>>>os.getcwd()
#更改当前工作目录
>>>os.chdir('d:\')'
>>>os.getcwd()


222有文件 practice等
212上有Mongo

解决方案:‘couldn't connect to server 127.0.0.1 shell/mongo.js '
  删除mongodb\data\mongod.lock文件即可！

   db.createCollection('content')新建表

 mongod --dbpath /home/jiangln/own_weibo/data/

"you are running on a numa machine":
 numactl --interleave=all mongod --dbpath=/home/jiangln/own_weibo/data/  #启动Mongo
 

 tail -10 xxx.json   看后10行
 htop  查看内存

'\t'   以tab分隔  a.split('\t')

 pandas read_csv时路径要用英文的，不然not exist  可能是编码的问题

df=pd.read_csv('G:\melon.csv',encoding='gbk') 表里有中文的时候   或者试utf-8
csv只有一表格  csv 本质是带分号的txt
读sheet：
epath=u'E:/Rjiaoben/总.xlsx'
df=pd.read_excel(epath,'Ali')

df.count() 每列的个数  df[u'好瓜'].count()
df.dtypes  每列的类型

df_new = df.drop(u'好瓜',axis=1)  把“好瓜”的这一列丢掉，形成新的dataframe
v = [1,3,4]
df_iter = df_new.iloc[v]  把v里的当做行索引，取到新的dataframe里面
df_iter.index=range(0,len(v))   改变索引值


找到这列中值是 稍凹  的索引
    a = [i for i,a in enumerate(list(df_test[u'脐部'])) if a==u'稍凹']
    print a


 一列中各类的个数
    a =  df[u'好瓜'].value_counts()   series对象
    print a.index
    print a.values
    print a
    print a[u'否']
>>>
Index([u'否', u'是'], dtype='object')
[9 8]
否    9
是    8
9

数组排序：
temp = np.array(df[i]) 先把panda的这一列转成numpy的数组
temp = np.sort(temp)

round(a,3)取3为小数

 tuple元组初始化后不能更改，元素不能被修改和删除，可以将两个连在一起；可以删除整个元祖  del tup

 xxx.rstrip() 删除 string 字符串末尾的指定字符（默认为空格）

 teamviewer连接不上，找不到网络地址——设置代理IP，在其他——选项——常规——代理设置


pymongo连接超时，可能是ip不对，换掉localhost为ip地址

xx.lower()
xx.upper()
Methods that use dot notation only work with strings.

On the other hand, len() and str() can work on other data types.

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

from datetime import datetime

now = datetime.now()
print now
print now.year
print now.month
print now.day

not is evaluated first;
and is evaluated next;
or is evaluated last.
For example, True or not False and False returns True.

获取今天0点的时间戳
def test():
    today = datetime.date.today() 
    print today
    a = int(time.mktime(today.timetuple()))
    print a

获得当前日期及其前一个月的
    today = datetime.date.today() 
    a = [str(today + datetime.timedelta(days=-i)) for i in range(30)]

b = datetime.date(2016,10,05) --><type 'datetime.date'> 2016-10-05
b = datetime.datetime(2016,10,05) --><type 'datetime.date'> 2016-10-05 00:00:00

判断Nonetype
if hashtag != None:

strftime将一个tm结构格式化为一个字符串，strptime则是将一个字符串格式化为一个tm结构。
import time

def unix2hadoop_date(ts):
    return time.strftime('%Y_%m_%d', time.localtime(ts))

def ts2datetime(ts):
    return time.strftime('%Y-%m-%d', time.localtime(ts))

def ts2date(ts):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))

def datetime2ts(date):
    return int(time.mktime(time.strptime(date, '%Y-%m-%d')))
    
def full_datetime2ts(date):
    return int(time.mktime(time.strptime(date,'%Y-%m-%d %H:%M:%S')))

class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."
            
my_cart = ShoppingCart('name')
my_cart.add_item('food',23)

scrapy startproject itzhaopin





python中，遍历dict的方法有四种。但这四种遍历的性能如何呢？我做了如下的测试
[python] view plain copy 在CODE上查看代码片派生到我的代码片
l = [(x,x) for x in xrange(10000)]  
d = dict(l)  
  
from time import clock  
  
t0=clock()  
for i in d:  
    t = i + d[i]  
t1=clock()  
  
for k,v in d.items():  
    t = k + v  
t2=clock()  
  
for k,v in d.iteritems():  
    t = k + v  
t3=clock()  
  
for k,v in zip(d.iterkeys(),d.itervalues()):  
    t = k + v  
t4=clock()  
  
print t1-t0, t2-t1, t3-t2, t4-t3   

将这段脚本运行5次，结果如下：
[plain] view plain copy 在CODE上查看代码片派生到我的代码片
python test.py  
0.00184039735833 0.00326492977712 0.00214993552657 0.00311549755797  
  
python test.py  
0.00182356570728 0.00339342506446 0.00234863111466 0.00321566640817  
  
python test.py  
0.00185107108827 0.00324563495762 0.00211175641563 0.00313479237748  
  
python test.py  
0.0018215130669 0.00320950848705 0.00215814608806 0.00322798225041  
  
python test.py  
0.00216635664955 0.00391807994377 0.00207604047314 0.00322757172233  

显然第一种方法效率最高，第三种方法略差一点但相差无几，方法二四性能就差得多
不过实际的差别不是太大，不必过于纠结




有重复数据的时候存Mongo要先建索引！
在mongo中建索引删除重复数据
 db.allinfo.ensureIndex({"id":1},{unique:true,dropDups:true})

 创建唯一索引并删除重复的数据
coll.ensureIndex({productid:1}) // 在productid上建立普通索引
coll.ensureIndex({district:1, plate:1}) // 多字段索引
coll.ensureIndex({productid:1}, {unique:true}) // 唯一索引
coll.ensureIndex({productid:1}, {unique:true, dropDups:true}) // 建索引时，如果遇到索引字段值已经出现过的情况，则删除重复记录
coll.getIndexes() // 查看索引
coll.dropIndex({productid:1}) // 删除单个索

mongo –path
db.AddUser(username,password) 添加用户
db.auth(usrename,password) 设置数据库连接验证
db.cloneDataBase(fromhost) 从目标服务器克隆一个数据库
db.commandHelp(name) returns the help for the command
db.copyDatabase(fromdb,todb,fromhost) 复制数据库fromdb—源数据库名称，todb—目标数据库名称，fromhost—源数据库服务器地址
db.createCollection(name,{size:3333,capped:333,max:88888}) 创建一个数据集，相当于一个表
db.currentOp() 取消当前库的当前操作
db.dropDataBase() 删除当前数据库
db.eval_r(func,args) run code server-side
db.getCollection(cname) 取得一个数据集合，同用法：db['cname'] or db.cname
db.getCollenctionNames() 取得所有数据集合的名称列表
db.getLastError() 返回最后一个错误的提示消息
db.getLastErrorObj() 返回最后一个错误的对象
db.getMongo() 取得当前服务器的连接对象get the server connection object
db.getMondo().setSubordinateOk() allow this connection to read from then nonmain membr of a replica pair
db.getName() 返回当操作数据库的名称
db.getPrevError() 返回上一个错误对象
db.getProfilingLevel() ?什么等级
db.getReplicationInfo() ?什么信息
db.getSisterDB(name) get the db at the same server as this onew
db.killOp() 停止（杀死）在当前库的当前操作
db.printCollectionStats() 返回当前库的数据集状态
db.printReplicationInfo()
db.printSubordinateReplicationInfo()
db.printShardingStatus() 返回当前数据库是否为共享数据库
db.removeUser(username) 删除用户
db.repairDatabase() 修复当前数据库
db.resetError()
db.runCommand(cmdObj) run a database command. if cmdObj is a string, turns it into {cmdObj:1}
db.setProfilingLevel(level) 0=off,1=slow,2=all
db.shutdownServer() 关闭当前服务程序
db.version() 返回当前程序的版本信息
 
db.linlin.find({id:10}) 返回linlin数据集ID=10的数据集
db.linlin.find({id:10}).count() 返回linlin数据集ID=10的数据总数
db.linlin.find({id:10}).limit(2)返回linlin数据集ID=10的数据集从第二条开始的数据集
db.linlin.find({id:10}).skip(8) 返回linlin数据集ID=10的数据集从0到第八条的数据集
db.linlin.find({id:10}).limit(2).skip(8) 返回linlin数据集ID=1=的数据集从第二条到第八条的数据
db.linlin.find({id:10}).sort() 返回linlin数据集ID=10的排序数据集
db.linlin.findOne([query]) 返回符合条件的一条数据
db.linlin.getDB() 返回此数据集所属的数据库名称
db.linlin.getIndexes() 返回些数据集的索引信息
db.linlin.group({key:…,initial:…,reduce:…[,cond:...]})
db.linlin.mapReduce(mayFunction,reduceFunction,
)
db.linlin.remove(query) 在数据集中删除一条数据
db.linlin.renameCollection(newName) 重命名些数据集名称
db.linlin.save(obj) 往数据集中插入一条数据
db.linlin.stats() 返回此数据集的状态
db.linlin.storageSize() 返回此数据集的存储大小
db.linlin.totalIndexSize() 返回此数据集的索引文件大小
db.linlin.totalSize() 返回些数据集的总大小
db.linlin.update(query,object[,upsert_bool])在此数据集中更新一条数据
db.linlin.validate() 验证此数据集
db.linlin.getShardVersion() 返回数据集共享版本号
db.linlin.find({‘name’:'foobar’}) select * from linlin where name=’foobar’
db.linlin.find() select * from linlin
db.linlin.find({‘ID’:10}).count() select count(*) from linlin where ID=10
db.linlin.find().skip(10).limit(20) 从查询结果的第十条开始读20条数据 select * from linlin limit 10,20 ———-mysql
db.linlin.find({‘ID’:{$in:[25,35,45]}}) select * from linlin where ID in (25,35,45)
db.linlin.find().sort({‘ID’:-1}) select * from linlin order by ID desc
db.linlin.distinct(‘name’,{‘ID’:{$lt:20}}) select distinct(name) from linlin where ID<20
db.linlin.group({key:{'name':true},cond:{'name':'foo'},reduce:function(obj,prev){prev.msum+=obj.marks;},initial:{msum:0}})
select name,sum(marks) from linlin group by name
db.linlin.find('this.ID<20',{name:1}) select name from linlin where ID<20
db.linlin.insert({'name':'foobar’,'age':25}) insert into linlin ('name','age’)values('foobar',25)
db.linlin.insert({'name':'foobar’,'age':25,’email’:'cclove2@163.com’})
db.linlin.remove({}) delete * from linlin
db.linlin.remove({'age':20}) delete linlin where age=20
db.linlin.remove({'age':{$lt:20}}) delete linlin where age<20
db.linlin.remove({'age':{$lte:20}}) delete linlin where age<=20
db.linlin.remove({'age':{$gt:20}}) delete linlin where age>20
db.linlin.remove({‘age’:{$gte:20}}) delete linlin where age>=20
db.linlin.remove({‘age’:{$ne:20}}) delete linlin where age!=20
db.linlin.update({‘name’:'foobar'},{‘$set’:{‘age’:36}}) update linlin set age=36 where name=’foobar’})
db.linlin.update({‘name’:'foobar'},{‘$inc’:{‘age’:3}}) update linlin set age=age+3 where name=’foobar’})


例如：
db.doubanbook.ensureIndex({"书名":1,"dd":1},{unique:true,dropDups:true})

db.version()

Ubuntu
在Ubuntu平台上，我们可以使用 wc 命令在不打开文件的情况下，来统计文件的信息。
比如：

wc -l myfile.txt 
统计文件的行数

wc -m myfile.txt
统计文件的字符数

wc -w myfile.txt
统计文件的单词数

删除换行符
 t = line.replace('\N','0').strip('\n').split('\t')

db.allinfo.find({"sex":1}).count()

不等于-1
 db.text.find({"root_text":{$ne:"-1"}}).count()

 222上  /home/ubuntu3/huxiaoqian/redis-2.8.13
 src/redis-server redis.conf   #启动redis
src/redis-cli -h 219.224.134.222 -p 6379  #进入redis

src/redis-cli -c -h 219.224.134.222 -p 6379  #如果是集群的话

数据存在跟config文件统一目录的地方
redis.conf    cluster.enable  是不是集群

select 0 选db0
keys *  看所有的key
type XXX  查看数据类型
dbsize   看db的大小
lrange XX 0 -1   看名叫xx的list的从0到-1个数
del  xxx  删除某个key 
zrange xxx  0 -1  看zset的名字
llen XXX 看列表的长度

hgetall hashtag_1378483200

# 交集
结构
redis键值太多的时候可以把一些合并起来存储    减少内存使用量


219.224.134.222:6379[1]> zrange both_out_degree -1 -1
1) "3994142429"
219.224.134.222:6379[1]> zrank both_out_degree 3994142429
(integer) 140190

redis 127.0.0.1:6379> ZINTERSTORE sum_point 2 mid_test fin_test

报错：
WRONGTYPE Operation against a key holding the wrong kind of value
解决：
redis有重复的key  删除那个就行了

错误： 
raise ClusterError('TTL exhausted.')
问题：
networks goes down or the client can't get in touch with the node it tries to talk to.

r.keys('*')

mongo 查找，只显示location这个字段
 db.allinfo.find({},{"location":1},{"_id":0})

按id查
 db.foo.find({"_id" : ObjectId("544a3dc0d4646f0c8c904962")})

python里用mongo，用find_one就不是游标的形式，是数据

matplotlib画图保存
from matplotlib.matlab import * 
 
  x = linspace(-4, 4, 200) 
  f1 = power(10, x) 
  f2 = power(e, x) 
  f3 = power(2, x)  
 
  plot(x, f1, 'r',  x, f2, 'b', x, f3, 'g', linewidth=2) 
  axis([-4, 4, -0.5, 8])
  text(1, 7.5, r'$10^x$', fontsize=16)
  text(2.2, 7.5, r'$e^x$', fontsize=16)
  text(3.2, 7.5, r'$2^x$', fonsize=16)
  title('A simple example', fontsize=16)
  
  savefig('power.png', dpi=75)
  show()

plt.loglog(x,y)




错误：
  _tkinter.TclError: no display name and no $DISPLAY environment variable
解决：
import matplotlib
matplotlib.use('Agg') #要写在一开始
import matplotlib.pyplot as plt    

错误：
ValueError: matplotlib display text must have all code points < 128 or use Unicode strings
编码问题，可能label用了中文


Python3以后删除了has_key()方法
用 if key1 in adict:  


pdf是概率密度分布

pymongo.errors.CursorNotFound: cursor id '4487089422038786904' not valid at server
你在用db.collection.find()的时候，它返回的不是所有的数据，而实际上是一个“cursor”。它的默认行为是：第一次向数据库查询 101 个文档，或 1 MB 的文档，取决于哪个条件先满足；之后每次 cursor 中的文档用尽后，查询 4 MB 的文档。另外，find()的默认行为是返回一个 10 分钟无操作后超时的 cursor。如果我一个 batch 的文档十分钟内没处理完，过后再处理完了，再用同一个 cursor id 向服务器取下一个 batch，这时候 cursor id 当然已经过期了，这也就能解释为啥我得到 cursor id 无效的错误了。

Stack Overflow 上有人提出过解决方法，是在 find() 时传入timeout=False来禁用 10 分钟超时的保护措施(但须记得对cursor迭代完成后，将cursor关闭。)。但是我觉得这是非常差的办法，因为如果你循环时产生异常，甚至断电或断网，都会导致 MongoDB 服务器资源永远无法被释放。而更好的办法是（我也发在了 Stack Overflow 上），估计一个 batch 大小，让 MongoDB 客户端每次抓取的文档在 10 分钟内能用完，这样客户端就不得不 10 分钟内至少联系服务器一次，保证 cursor 不超时。

具体用法：

a = collection.find(timeout=False)

for document in db.collection.find().batch_size(30):
    do_time_consuming_things()


Running setup.py install for python-igraph



解压   http://blog.csdn.net/imyang2007/article/details/7634470
tar zxvf xxx.tar.gz
python setup.py install
gunzip facebook_combined.txt.gz   把这个文件直接解压成txt文件，原文件没有，要想保留的话，可以加-c 再重定向


*.tar 用 tar –xvf 解压
*.gz 用 gzip -d或者gunzip 解压
*.tar.gz和*.tgz 用 tar –xzf 解压
*.bz2 用 bzip2 -d或者用bunzip2 解压
*.tar.bz2用tar –xjf 解压
*.Z 用 uncompress 解压
*.tar.Z 用tar –xZf 解压
*.rar 用 unrar e解压
*.zip 用 unzip 解压

tar xvf onlineldavb.tar -C ./onlinelda/到指定目录下


 To avoid name collision with the igraph project, this visualization library has been renamed to 'jgraph'. Please upgrade when convenient.

cluto 一个聚类分析的软件


微信目录：
C:\Users\NaNa\Documents\WeChat Files\gir123\Attachment


cluto使用:
 ./vcluster ../wap.mat 10
文件里的第一行写矩阵的‘行数、列数、特征值总数’
之后的形式：
特征值序号  序号对应的得分 特征值序号  序号对应的得分 特征值序号  序号对应的得分
特征值序号  序号对应的得分 特征值序号  序号对应的得分 特征值序号  序号对应的得分    

对于文本 得分可以是tfidf，序号就是对分词后的词的排序

The first line of the matrix file contains exactly three numbers, all of which are integers. The first integer is the
number of rows in the matrix (n), the second integer is the number of columns in the matrix (m), and the third integer
is the total number of non-zeros entries in the n × m matrix.

报错：（默认是当成文档的idf值，要是稀疏的）
IDF column model only applies to sparse matrices and non-correlation-coefficient similarities!
修改：
 ./vcluster -colmodel=none ./for_cluster.txt 3 

生成了个wap.mat.clustering.10  输出文件
scluster主要作图
./vcluster  xxx.mat  10
======================================
cid  Size  ISim  ISdev   ESim  ESdev
======================================
cid  类别号；size  类别里包含的数量；isim  类内元素间平均相似度
isdev  相似度的标准差   esim   类间的外部相似度    
esdev  类外部的相似度标准差


比较的时候用set，快的真的不是一星半点！


a = set(['1','2'])
b =set(['1','2','4'])
if b.issuperset(a):



    counts = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0) + 1
    print counts


selenium  自动化获取


?ptetty   组织形式更整齐
curl –XGET 'http://219.224.134.213:9206/flow_text_2016-05-21?pretty'
标识   方法  协议  
'{"query":{"match_all":{}}}'

-d  具体的搜索语句 相当于where


213  ubuntu8
211-215上有es   213管分发，挂的了话换214
mapping!很重要，是针对即将存入的数据（文档）格式做规范要求，以满足ES多种检索要求
index：no  不能被检索
score在结构化查询时，结果与语句的匹配程度
gte大于等于   lte小于等于


>>> G.out_degree([0,1])
{0: 1, 1: 1}
>>> list(G.out_degree([0,1]).values())
[1, 1]

联合多个$in操作：联合多个in表达式，将可能触发联合索引的合并限制。如果符合的item大于等于4000000，mongo将产生“combinatorial limit of $in partitioning of result set exceeded” 错误。


ps ef|grep elasticsearch


    index_list = []
    for i in range(7, 0, -1):
        if RUN_TYPE == 1:
            iter_date = ts2datetime(datetime2ts(now_date) - i * DAY)
        else:
            iter_date = '2013-09-01'
        index_list.append(flow_text_index_name_pre + iter_date)
    print '726'
    try:
        weibo_result = es_flow_text.search(index=index_list, doc_type=flow_text_index_type,\
                body={'query':{'filtered':{'filter':{'term': {'uid': uid}}}}, 'size':MAX_VALUE,'sort':{sort_type:{'order':'desc'}}})['hits']['hits']
        #print weibo_result
    except:
        weibo_result = []

更新数据
将id=1的文档的uid字段更新为3，同时增加user_fansnum字段，设为100
es.update(index=”flow_text”, doc_type=”text”, id=1,  body={“doc”:{“text”:“更新”, “user_fans
num”: 100}})

    query_body = {
        'query':{
            'filtered':{
                'filter':{
                    'terms':{
                        'uid': list(uid_set)
                        }
                    }
                }
            },
        'aggs':{
            'all_domain':{
                'terms':{'field': 'domain'}
                }
            }
        }


curl:  -X 后面跟 RESTful ：  GET, POST ... 
-d 后面跟数据。 (d = data to send) 

 'sort':{'timestamp':{'order':'asc'}}增序

删除符合这一query的数据
curl -XDELETE 'http://219.224.134.211:9204/topics/text/_query' -d '{"query":{"filtered":{"filter":{"term":{"comput_status":-1}}}}}'

es集群elasticsearch-1.6.0，除了93是在我的目录下，其余的都在各自的ubuntu下
211-215
211-111111
es模糊查询“
aoyunhui/_search    POST
{"query":{"wildcard":{"text":"*【*"}}}

    query_body = {
        "query":{
            "filtered":{
                "query":{
                    "wildcard":{"text":"*兴业*"}
                },
                "filter":{
                    "range":{
                        "timestamp": {"gte":1378522700, "lte": 1378522977}
                        }
                    }
                }
            }
        }

        {"query": {"bool": {"must": [{"wildcard": {"text": "*兴业*"}}, {"range": {"timestamp": {"gte": 1378522700, "lte": 1378522977}}}]}}}

bin/elasticsearch –Xmx30g –Xms30g –Des.max-open-files=true –d  
max-open-files对应的是系统上的：
ulimit -n 
ulimit -HSn 65535   临时性改最大的启动文件     这个终端关掉就没了

用id查
result = es_group_result.get(index=group_index_name, doc_type=group_index_type, id=task_id)['_source']

错误：
portrait_exist_result = es_user_portrait.mget(index=portrait_index_name, doc_type=portrait_index_type, \
            body={'uname':uname})['docs']
RequestError: TransportError(400, u'ActionRequestValidationException[Validation Failed: 1: no documents to get;]')
原因：   
mget对id搜


es有时候往里面插数据插不进去
错误：
TransportError: TransportError(503, u'UnavailableShardsException[[group_manage][3] Primary shard is not active or isn\'t assigned to a known node. Timeout: [1m], 
原因：
可能是因为分片掉了，数据有丢失，就问题，要重建个表


在python的shell里import xxx包，再输入xxx.__file__ 可以查看包的路径

get:['_source']
mget:['docs']
search:['hits']
['hits']['hits']['_source']


mysql

使用MySQL

阅读: 56291
MySQL是Web世界中使用最广泛的数据库服务器。SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。而MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。

此外，MySQL内部有多种数据库引擎，最常用的引擎是支持数据库事务的InnoDB。

安装MySQL

可以直接从MySQL官方网站下载最新的Community Server 5.6.x版本。MySQL是跨平台的，选择对应的平台下载安装文件，安装即可。

安装时，MySQL会提示输入root用户的口令，请务必记清楚。如果怕记不住，就把口令设置为password。

在Windows上，安装时请选择UTF-8编码，以便正确地处理中文。

在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。MySQL的配置文件默认存放在/etc/my.cnf或者/etc/mysql/my.cnf：

[client]
default-character-set = utf8

[mysqld]
default-storage-engine = INNODB
character-set-server = utf8
collation-server = utf8_general_ci

show variables like '%char%';  看编码
show databases;
show tables;
取前5条
select * from propagate_weibos where topic = 'aoyunhui' LIMIT 0,5;

>>> a.extend([1,2])
>>> print a
[1, 2, '3', '1', 1, 2]
>>> a.append([1,2])
>>> print a
[1, 2, '3', '1', 1, 2, [1, 2]]
append和extend都仅只可以接收一个参数，
append 任意，甚至是tuple
extend 只能是一个列表



es:

错误：
{u'items': [{u'index': {u'status': 503, u'_type': u'text', u'_id': u'3618063561370373', u'error': u"UnavailableShardsException[[\u5965\u8fd0\u4f1a][0] Primary shard is not active or isn't assigned to a known node. Timeout: [60ms], request: org.elasticsearch.action.bulk.BulkShardRequest@5e963070]", u'_index': u'\u5965\u8fd0\u4f1a'}}], u'errors': True, u'took': 94}
es挂了。。。/中文建的索引，找不到那个index，可能是解码问题，也可能不能用中文


错误： No query registered for [timestamp]];
query里的must[]
        query_body = {
            'query':{
                'bool':{
                    'must':[
                        {'term':{'sentiment':sentiment}},  #一个话题，不同情绪下给定时间里按关键词聚合
                        {'range':{
                            'timestamp':{'gte': begin_ts, 'lt':end_ts} 
                        }
                    }]
                }
            },
            'aggs':{
                'all_interests':{
                    'terms':{
                        'field': 'keywords_string',
                        'size': k_limit #SENTIMENT_MAX_KEYWORDS
                    }
                }
            }
        }



错误，插入的时候：
TypeError: list indices must be integers, not str
数据有错。。。

215/ubuntu10
1.5.2   9200


df -h 看空间大小


es  中文解码成unicode

@修饰符
http://blog.sina.com.cn/s/blog_6fe87f870101d9cm.html


class SentimentCount(db.Model):#情绪绝对数量曲线--已改
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    query = db.Column(db.String(20))
    end = db.Column(db.BigInteger(10, unsigned=True))
    range = db.Column(db.BigInteger(10, unsigned=True))
    sentiment = db.Column(db.Integer(1, unsigned=True))
    count = db.Column(db.BigInteger(20, unsigned=True))

    def __init__(self, query, range, end, sentiment, count):
        self.query = query 
        self.range = range
        self.end = end
        self.sentiment = sentiment
        self.count = count

mysql   

use weibocase;
show tables;
describe sentiment_weibos;
select count(*) from table;
select * from sentiment_weibos where query='aoyunhui' LIMIT 1;

建索引：   快很多！
ALTER TABLE sentiment_weibos ADD INDEX (end);
或者alter table sentiment_weibos add index end_ts_index(end);
http://www.jb51.net/article/32149.htm
查看已有索引：
show index from propagate_count;

b-tree （平衡多路查找树）
http://www.2cto.com/database/201411/351106.html
B-tree，B是balance，一般用于数据库的索引。使用B-tree结构可以显著减少定位记录时所经历的中间过程，从而加快存取速度。
而B+tree是B-tree的一个变种，大名鼎鼎的MySQL就普遍使用B+tree实现其索引结构。
一般来说，索引本身也很大，不可能全部存储在内存中，因此索引往往以索引文件的形式存储的磁盘上。这样的话，索引查找过程中就要产生磁盘I/O消耗，相对于内存存取，I/O存取的消耗要高几个数量级，所以评价一个数据结构作为索引的优劣最重要的指标就是在查找过程中磁盘I/O操作次数的渐进复杂度。
索引的结构组织要尽量减少查找过程中磁盘I/O的存取次数。



字典按键值排序，并取前几个
sen_with_keyword[sentiment] = sorted(keyword_dict.items(),key=lambda x:x[1], reverse=True)[:k_limit]
reverse=true:由大到小
reverse=false：由小到大

bb = {'类ID':[{'weight':0.4,'text':'a'},{'weight':0.6,'text':'b'}]}
for k,v in bb.iteritems():
    s = sorted(v,key=lambda x:x['weight'],reverse=True)
    print s

bb = {'lei1':{'weight':0.4,'text':'a'},'lei2':{'weight':0.6,'text':'a'},'lei3':{'weight':0.5,'text':'a'},'lei4':{'weight':0.2,'text':'a'}}

s = sorted(bb.items(),key=lambda x:x[1]['weight'],reverse=True)
print s

a = {'a':1,'b':2,'c':3,'d':1}
b = sorted(a.items(), key=lambda x: x[1], reverse=False)
for i in a.items():
    print i[1]

>>>>>
1
3
2
1

错误：
    for uid,geos in result['activity_geo_disribution']:
ValueError: too many values to unpack

要加上.iteritems()


a = {'1':{'shaanxi':{'total':5,'tc':3,'xian':2}},'2':{'beijing':{'total':2,'beijing':2}}}
for i in a.iteritems():
    print i[1].values()[0]['total']

es插入、删除（插入以id标识唯一性）
    #es.index(index='topics',doc_type='text',body={'name':'老虎','index_name':'laohu','end_ts':'1470900837',\
                                                #'start_ts':'1467648000','submit_user':'jln'})
    #es.delete(index='topics',doc_type='text',id='1467648000_1470900837')

mapping的索引副本默认是1

错误：
加上一个关键词后，es查不出来数据，之前可以
原因：
在优化顺序的时候重建了表，忘了对那个字段设置不分词
（浪费了很多时间查bug啊啊啊啊）


错误：
 filter does not support [index_name]]; }]')

错误：
 Traceback (most recent call last):
  File "cron_topic_city.py", line 217, in <module>
    cityTopic(topic, start_ts=START_TS, over_ts=END_TS, during=Fifteenminutes)
  File "cron_topic_city.py", line 153, in cityTopic
    print weibo['_source']['geo']#.encode('utf8')
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

解决：
print weibo['_source']['geo'].encode('utf8')

把多个unicode编码的列表转成一个字符串：
''.join(v)

不要把简单的事情想复杂！

错误：TypeError: string indices must be integers, not tuple
'''原：
        query_body = {   #按message_type得到微博
            'query':{
                'bool':{
                    'must'[
                        {'terms':{'message_type':[1,3]}},
                        {'range':{
                            'timestamp':{'gte': startts, 'lt':endts} 
                        }
                    }]
                }
            },
            'sort':{'message_type':{"order":"desc"}}
        }
'''

must 没有加冒号啊！！！！！
        query_body = {
            'query':{
                'bool':{
                    'must':[
                        {'terms':{'message_type':[1,3]}},  #一个话题，不同情绪下给定时间里按关键词聚合
                        {'range':{
                            'timestamp':{'gte': startts, 'lt':endts} 
                        }
                    }]
                }
            },
            'sort':{"message_type":{"order":"desc"}}
        }

主题河——词   反向找到微博  形成鱼骨图
https://github.com/rcsc/opinion_news/tree/master/opinion_cal run.py 不用！ 




https://github.com/rcsc/opinion_news/tree/master/opinion ——package 新闻 package_weibo 微博  观点分析

整理好的观点分析代码   ——主观、客观的情绪和子观点
/home/ubuntu2/linhao/opinionapi   package/package_weibo


flask错误：
jinja2.exceptions.TemplateSyntaxError: expected token 'end of print statement', got '%'
多打了个空格{% block XXX  %}，百分号应该紧挨着大括号


分类评价
def cluster_evaluation(items, top_num=5, topk_freq=20, least_freq=10, min_tfidf=None, least_size=8):
    
    聚类评价，计算每一类的tf-idf: 计算每一类top词的tfidf，目前top词选取该类下前20个高频词，一个词在一个类中出现次数大于10算作在该类中出现
    input:
        items: 新闻数据, 字典的序列, 输入数据示例：[{'title': 新闻标题, 'content': 新闻内容, 'label': 类别标签}]
        top_num: 保留top_num的tfidf类
        topk_freq: 选取的高频词的前多少
        least_freq: 计算tf-idf时，词在类中出现次数超过least_freq时，才被认为出现
        min_tfidf: tfidf大于min_tfidf的类才保留
        least_size: 小于least_size的簇被归为其他簇
    output:
        各簇的文本, dict

聚类，然后计算每类的tfidf值，再剔除些低于阈值的，剩下的是每类的关键词

zip：
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = zip(x, y, z)
print xyz
复制代码
运行的结果是：

[(1, 4, 7), (2, 5, 8), (3, 6, 9)]



Type:      instancemethod
-->是一个方法  要加括号()

判断话题是否活跃：在给定的时间段里没有新文本，就不活跃


    def check_ifsplit(self, timestamp):
        """给定时间判断其他类是否需要分裂子事件, 每小时执行一次
           input:
               timestamp: 截止时间戳, 整点
           output:
               True or False
        """
         # 每天0、6、12、18时检测, 其他类存量文本数 > avg, 则分裂
        # 每小时检测，该小时内其他类文本数 > avg * 5 或 该小时内其他类文本数-上个小时内其他类文本数 > avg * 2, 则分裂

#-*-coding=utf-8-*-
import math
def tfidf_cal(keywords_dict_list, topk=3):
    '''计算tfidf
       input
           keywords_dict_list: 不同簇的关键词, list
       output
           不同簇的top tfidf词
    '''
    results = []
    for keywords_dict in keywords_dict_list:
        tf_idf_dict = dict()

        total_freq = sum(keywords_dict.values()) # 该类所有词的词频总和
        total_document_count = len(keywords_dict_list) # 类别总数
        for keyword, count in keywords_dict.iteritems():
            tf = float(count) / float(total_freq)
            document_count = sum([1 for kd in keywords_dict_list if keyword in kd.keys()])
            idf = math.log(float(total_document_count) / float(document_count + 1))
            tf_idf = tf * idf
            tf_idf_dict[keyword] = tf_idf

        tf_idf_results = sorted(tf_idf_dict.iteritems(), key=lambda(k, v): v, reverse=False)
        tf_idf_results = tf_idf_results[len(tf_idf_results)-topk:]
        tf_idf_results.reverse()  #元组
        tf_idf_results = {w: c for w, c in tf_idf_results}
        results.append(tf_idf_results)

    return results


print tfidf_cal([{'aaa':2,'bbb':4},{'bbb':2,'ddd':3},{'ccc':2},{'ddd':2},{'ccc':2},{'aaa':2}])
对于keywords_dict_list里的元素kd，如果keyword在kd的键值里，就得1
短if判断，x if condition else y

两个字典合并：
a = {'aa':1,'bb':1}
b = {'aa':2,'cc':1}
c = dict(a,**b)
但只是{'aa': 2, 'cc': 1, 'bb': 1}
键值也合并的话，还是for循环更快


错误：
 def comments_list(taskid,cluster_num=-1,cluster_eva_min_size=default_cluster_eva_min_size,vsm=default_vsm,calcu=1,weibo_list):#weibo_list把微博读进来
SyntaxError: non-default argument follows default argument
应该把不能默认的变量放在前面

新闻：
{"news_id":"news", "content168": "\u7d27\u6025\u63a7\u544a\u9020\u5047\u628a\u4e00\u540d\u521b\u65b0\u5de5\u4f5c\u7684\u56fd\u7f51\u5e72\u90e8\u6253\u5165\u53e6\u518c\u6765\u538b\u5236\u79d1\u6280", "id": "2016081516213116", "datetime": "2015-10-07 21:46:43"}

content168：文本内容    id：微博的mid     datetime:shijian   还可以加赞数、评论数等等
微博：
{"news_id":"weibo", "reposts_count": 0, "datetime": "2015-06-18 09:18:24", "content": "\u98ce\u5e06\u80a1\u4efd(sh600482) \u6c5f\u5c71\u80a1\u4efd(sh600389) \u9752\u677e\u5efa\u5316(sh600425) \u4e03\u559c\u63a7\u80a1(sz002027) \u4e1c\u4fe1\u548c\u5e73(sz002017) \u82cf\u5b81\u4e91\u5546(sz002024) \u8fea\u9a6c\u80a1\u4efd(sh600565) \u5b89\u5fbd\u6c34\u5229(sh600502) \u5149\u7535\u80a1\u4efd(sh600184) \u5b81\u6caa\u9ad8\u901f(sh600377) \u519c\u53d1\u79cd\u4e1a(sh600313) \u7ca4\u6c34\u7535(sz002060)", "attitudes_count": 0, "comments_count": 0, "id": 3855013502246501}

当前时间戳：time.time()
当前日期：time.ctime()
1、Python下日期到时间戳的转换
import datetime
import time
dateC=datetime.datetime(2010,6,6,8,14,59)
timestamp=time.mktime(dateC.timetuple())
print timestamp

2、Python下将时间戳转换到日期
import datetime
import time
ltime=time.localtime(1395025933)
timeStr=time.strftime("%Y-%m-%d %H:%M:%S", ltime)
print timeStr


# -*- coding: utf-8 -*-

import time

def unix2hadoop_date(ts):
    return time.strftime('%Y_%m_%d', time.localtime(ts))

def ts2datetime(ts):
    return time.strftime('%Y-%m-%d', time.localtime(ts))

def ts2date(ts):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))

def datetime2ts(date):
    return int(time.mktime(time.strptime(date, '%Y-%m-%d')))

def window2time(window, size=24*60*60):
    return window*size

def datetimestr2ts(date):
    return time.mktime(time.strptime(date, '%Y%m%d'))

def ts2datetimestr(ts):
    return time.strftime('%Y%m%d', time.localtime(ts))

def ts2HourlyTime(ts, interval):
    # interval 取 Minite、Hour
    ts = ts - ts % interval
    return ts

def ts2datetime_full(ts):
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(ts))



{"sentiment": 3, "title": "", "text": "\u3010\u7f8e\u56fd\u4e13\u5bb6\u58f0\u79f0 \u6ca1\u6709\u4fc4\u7f57\u65af\u8fd0\u52a8\u5458\u7684\u5965\u8fd0\u4f1a\u65e0\u8da3\u3011]\u534e\u76db\u987f\u653f\u6cbb\u5b66\u4e2d\u5fc3\u201c\u6b27\u4e9a\u4e2d\u5fc3\u201d\u526f\u4e3b\u4efb\u5384\u5c14\u00b7\u62c9\u65af\u7a46\u68ee\u5728\u63a5\u53d7\u536b\u661f\u901a\u8baf\u793e\u91c7\u8bbf\u65f6\u8868\u793a\uff0c\u4fc4\u7f57\u65af\u9009\u624b\u6216\u5168\u4f53\u7f3a\u5e2d\u91cc\u7ea6\u5965\u8fd0\u4f1a\uff0c\u8fd9\u4e0d\u4ec5\u4f1a\u7834\u574f\u6bd4\u8d5b\u7cbe\u795e\uff0c\u8fd8\u4f1a\u8ba9\u8bb8\u591a\u4eba\u76f4\u63a5\u653e\u5f03\u89c2\u770b\u6bd4\u8d5b\u3002http://t.cn/Rtw876w", "clusterid": "nonsense_rub", "datetime": "2016-07-21 10:29:54", "ad_label": 1, "id": "3999624253146996"}
{"sentiment": "nonsense_news", "title": "", "text": "\u3010\u5173\u4e8e\u91cc\u7ea6\u5965\u8fd0\u4f1a\u76848\u4e2a\u51b7\u77e5\u8bc6\u3011", "clusterid": "6a40fbe1-d065-4cd9-9c1a-dbecc189f1af", "datetime": "2016-07-21 16:47:13", "duplicate": false, "ad_label": 0, "same_from": "3999719212384214", "id": "3999719212384214"}

{"sentiment": 1, "title": "", "text": "//@\u6cb3\u5317\u9ad8\u9662: #\u8f7b\u677e\u4e00\u523b#\u3010\u5173\u4e8e\u91cc\u7ea6\u5965\u8fd0\u4f1a\u76848\u4e2a\u51b7\u77e5\u8bc6\u3011", "clusterid": "6a40fbe1-d065-4cd9-9c1a-dbecc189f1af", "datetime": "2016-07-21 10:36:20", "duplicate": false, "ad_label": 0, "same_from": "3999625867700355", "id": "3999625867700355"}

{"sentiment": 1, "title": "", "text": "\u6211\u53c2\u4e0e\u4e86@Rio2016\u91cc\u7ea6\u5965\u8fd0\u4f1a \u53d1\u8d77\u7684\u6295\u7968\u3010\u5927\u5bb6\u6700\u671f\u5f85\u7684\u91cc\u7ea6\u5965\u8fd0\u9879\u76ee\u662f\u54ea\u4e9b\u5462\uff1f\u3011\uff0c\u6211\u6295\u7ed9\u4e86\u201c\u6e38\u6cf3\u201d\u7b492\u4e2a\u9009\u9879\uff0c\u4f60\u4e5f\u5feb\u6765\u8868\u6001\u5427~", "clusterid": "nonsense_rub", "datetime": "2016-07-21 10:47:21", "ad_label": 0, "id": "3999628644892379"}




dump_file.write(json.dumps({"params": params, "features":features, "senti_dump_dict":sentiment_dump_dict, \
            "cluster_dump_dict":cluster_dump_dict, "ratio":ratio_results, "sentiratio": sentiratio_results, \
            "before_filter_count": before_filter_count, "after_filter_count": after_filter_count, \
            "rub_results": rub_results}))  #rub_resulte放垃圾文本的字段



features:每类的词，可以成词云    ratio:按比例分的词——饼图    sentiratio:按情绪分的词——饼图    
cluster_dump_dict:每个类的微博，包括权重
rub_results

 "params": {"cluster_eva_min_size": 5, "calculation_label": 1, "cluster_num": -1, "vsm": "v1", "taskid": "aoyunhui"}, "features": {"6a40fbe1-d065-4cd9-9c1a-dbecc189f1af": ["\u77e5\u8bc6", "\u5e7f\u5dde", "\u9009\u624b"]}, "sentiratio": {"\u79ef\u6781": 0.6666666666666666, "\u4e2d\u6027": 0.3333333333333333}, "ratio": {"\u77e5\u8bc6,\u5e7f\u5dde,\u9009\u624b": 1.0}, "
cluster_dump_dict": {"6a40fbe1-d065-4cd9-9c1a-dbecc189f1af": {"399962586770035
5": [{"comment": 0, "news_id": "news", "text_filter_ad": "//#\u8f7b\u677e\u4e0
0"\u523b#\u3010\u5173\u4e8e\u91cc\u7ea6\u5965\u8fd0\u4f1a\u76848\u4e2a\u51b7\u7"
"7e5\u8bc6\u3011", "weight": 0.061157177565710485, "sentiment": 1, "title": "",
 "content168": "//@\u6cb3\u5317\u9ad8\u9662: #\u8f7b\u677e\u4e00\u523b#\u3010\
u5173\u4e8e\u91cc\u7ea6\u5965\u8fd0\u4f1a\u76848\u4e2a\u51b7\u77e5\u8bc6\u3011"
", "clusterid": "6a40fbe1-d065-4cd9-9c1a-dbecc189f1af", "retweeted": 0, "same_
from_sentiment": "3999625867700355", "datetime": "2016-07-21 10:36:20", "conte
nt": "//#\u8f7b\u677e\u4e00\u523b#\u3010\u5173\u4e8e\u91cc\u7ea6\u5965\u8fd0\u
4f1a"\u76848\u4e2a\u51b7\u77e5\u8bc6\u3011", "duplicate": false, "news_content"
: "", "ad_label": 0, "duplicate_sentiment": false, "rub_label": 0, "text": "//"
"@\u6cb3\u5317\u9ad8\u9662: #\u8f7b\u677e\u4e00\u523b#\u3010\u5173\u4e8e\u91cc\
u7ea6\u5965\u8fd0\u4f1a\u76848\u4e2a\u51b7\u77e5\u8bc6\u3011", "same_from": "3"
999625867700355", "id": "3999625867700355"}], "3999705740934972": [{"comment":"

 "ratio": {"\u77e5\u8bc6,\u5e7f\u5dde,\u9009\u624b": 1.0},
  "features": {"6a40fbe1-d065-4cd9-9c1a-dbecc189f1af": ["\u77e5\u8bc6", "\u5e7f\u5dde", "\u9009\u624b"]}, "sentiratio": {"\u79ef\u6781": 0.6666666666666666, "\u4e2d\u6027": 0.
3333333333333333}

 "rub_results": [{"comment": 0, "news_id": "news", "sentiment": 0, "title": "", "content168": "\u53d1\u5e03\u4e86\u5934\u6761\u6587\u7ae0\uff1a\u300a\u3010\u805a\u7126\u3011\u51fa\u6218\u91cc\u7ea6\u5965\u8fd0\u4f1a \u9102\u5c14\u591a\u65af\u59d1\u5a18\u699c\u4e0a\u6709\u540d\u300b http://t.cn/RtAZvLQ", "news_content": "", "retweeted": 0, "same_from_sentiment": "3999707149656998", "datetime": "2016-07-21 15:59:18", "content": "\u53d1\u5e03\u4e86\u5934\u6761\u6587\u7ae0\uff1a\u300a\u3010\u805a\u7126\u3011\u51fa\u6218\u91cc\u7ea6\u5965\u8fd0\u4f1a \u9102\u5c14\u591a\u65af\u59d1\u5a18\u699c\u4e0a\u6709\u540d\u300b http://t.cn/RtAZvLQ", "duplicate": false, "text_filter_ad": "\u53d1\u5e03\u4e86\u5934\u6761\u6587\u7ae0\uff1a\u300a\u3010\u805a\u7126\u3011\u51fa\u6218\u91cc\u7ea6\u5965\u8fd0\u4f1a \u9102\u5c14\u591a\u65af\u59d1\u5a18\u699c\u4e0a\u6709\u540d\u300b http://t.cn/RtAZvLQ", "ad_label": 0, "duplicate_sentiment": false, "rub_label": 1, "same_from": "3999707149656998", "clusterid": "nonsense_rub", "text": "\u53d1\u5e03\u4e86\u5934\u6761\u6587\u7ae0\uff1a\u300a\u3010\u805a\u7126\u3011\u51fa\u6218\u91cc\u7ea6\u5965\u8fd0\u4f1a \u9102\u5c14\u591a\u65af\u59d1\u5a18\u699c\u4e0a\u6709\u540d\u300b http://t.cn/RtAZvLQ", "id": "3999707149656998"}, {"comment": 0, "news_id": "news", "text_filter_ad": "\u3010\u8fce\u91cc\u7ea6\u5965\u8fd0 \u4f20\u5929\u7ffc\u7ea2\u5305\u3011\u6fc0\u60c5\u590f\u65e5\uff0c\u8fce\u91cc\u7ea6\u9886\u7ea2\u5305\uff0c\u6700\u9ad8\u51cf\u514d15\u5143\uff0c\u6d3b\u52a8\u65f6\u95f4\uff1a7\u670815\u65e5-8\u67086\u65e5\u3002\u5929\u7ffc\u7ea2\u5305\uff0c\u6bcf\u65e510\u70b9\u300120\u70b9\u5f00\u62a2\uff0c\u6bcf\u65e5\u53d1\u653e20\u4e2a\u7ea2\u5305\uff01\u4e86\u89e3\u53ca\u53c2\u4e0e\u8be6\u60c5\u8fd8\u4e0d\u8d76\u5feb\u767b\u9646\u4e2d\u56fd\u7535\u4fe1\u7f51\u4e0a\u8425\u4e1a\u5385\u6b22go\u5b98\u65b9\u7f51\u7ad9\u6216\u76f4\u63a5\u70b9\u51fb\u767b\u9646\uff1ahttp://t.cn/R5129iH\u8fd8\u6709\u66f4\u591a\u7cbe\u5f69\u7684\uff1a\u878d\u5408\u5957\u9910\u30014G\u4efb\u6027\u5361\u3001\u70ed\u9500\u624b\u673a\u3001\u72


{'类ID'：[{'weight':0.4,'text':'a'},{'weight':0.6,'text':'b'}]}


filter过滤，score都一样，查的快，有缓存
查询的分不一样,要计算相关性得分，查的慢，没有缓存
原则上来说，使用查询语句做全文本搜索或其他需要进行相关性评分的时候，剩下的全部用过滤语句

{"query": {
    "bool": {
        "must": [{
            "bool": {
                "should": [
                {"wildcard": {"text": "*知识*"}}, 
                {"wildcard": {"text": "*广州*"}}
                
                 ]
            }
        }, 
        {"range": {"timestamp": {"lt": 1469289600, "gte": 1469203200}}}
        ]}
    }
}

{"query":{"bool":{"must":[{"wildcard":{"text":"*【*】*"}},{"range":{"timestamp":{"lt":1469708010,"gte":1469706647}}}]}}}


{"query":{                    
    "bool":{
    "must_not":[
        {"wildcard":{"text":"*【*】*"}}],
    "must":[
        {"range":{"timestamp":{"lt":1469708010,"gte":1469706647}}
    }]
    }}}


{"query": {"bool": {"must": [{"wildcard": {"text": "*\xe3\x80\x90*\xe3\x80\x91*"}}, {"range": {"timestamp": {"lt": 1468857600, "gte": 1471622400}}}]}}, "size": 100}

错误：
Traceback (most recent call last):
  File "count_keyword.py", line 18, in <module>
    from comment_module import comments_calculation_v2
  File "/home/ubuntu2/jiangln/socialconsume/socialconsume/cron/language/fix/../public/comment_module.py", line 18, in <module>
    from comment_clustering_tfidf_v7 import tfidf_v2, text_classify, \
  File "/home/ubuntu2/jiangln/socialconsume/socialconsume/cron/language/fix/../public/comment_clustering_tfidf_v7.py", line 13, in <module>
    from utils import cut_words, cut_words_noun
ImportError: cannot import name cut_words_noun
不能引包：包之间有互相引用、不同的路径下有一样的包

import utils
print utils.__file__


自己做个包  写个setup.py    然后python setup.py install装包  别的地方就可以引了


"\u4e00\u5929\u8981\u5c04"   unicode编码


git rm -r XXX  git上删除  -r删除文件夹
git add XXX

git remote rm origin  删除这个
Unix的哲学是“没有消息就是好消息”

git checkout命令加上-b参数表示创建并切换，相当于以下两条命令：
查看分支
$ git branch dev

$ git checkout dev
Switched to branch 'dev'
删除分支：
$ git branch -d feature-vulcan

pull jln main是把jln main拉取下来，然后当前分支和它合并 
push的时候假如远程分支和当前分支有不同的修改的话是push不了的，pull了之后就把远程分支和当前分支合并了

jln main和origin main是不同地方的两个分支
git pull origin main只拉取了origin main这个分支的修改，不能保证没有和jln main存在不同的修改

现在和origin main木有关系了
push到远程分支的时候，假如远程分支有本地分支上没有的修改(比如别人把他的代码push到那个远程分支了)，是不能push的。在push jln main之前要pull jln main一下，就是这个原因。之前可能是因为jln main上没有本地分支上没有的修改，所以没有pull也能push
至于要不要pull origin main，就看你自己想不想和origin main这个远程分支保持同步了

git remote -v
git remote rm origin
git remote add origin   https://github.com/jianjian0dandan/socialconsume.git   重加成这个branch

查看某一文件的修改历史
 git log --pretty=oneline cron_topic_identify.py
 》ddf049837f85357f65a663d760657638e8b48bda jln
4dad9568ce9082a7bd4058865595d1a2c6af5aef jln
cfb95007030ffd566c45d81c149335bb461bd2ff jln
ebdc89af58cf37bda1d9a3a189926b89dfc3d56d chenyz
061d3e30f04425dd1b0784f8079f0fbfc889f55d Update cron_topic_identify.py
8abc1fc484bcbc8996cde129121519a326d12f61 jln

查看这次提交修改了什么地方
git show ddf049837f85357f65a663d760657638e8b48bda


# 检查是单独执行还是被导入
if __name__ == '__main__':
      # Yes
      statements
else:
      # No (可能被作为模块导入)
      statements 

对于.py文件,当一个模块第一次被导入时,它就被汇编为字节代码,并将字节码写入一个同名的 .pyc文件.后来的导入操作会直接读取.pyc文件而不是.py文件.(除非.py文件的修改日期更新,这种情况会重新生成.pyc文件) 


包之间的引用：
每级下都有__init__.py，在里面声明import的东西，调用子目录


参数：
optparser = OptionParser()
optparser.add_option('-p', '--port', dest='port', help='Server Http Port Number', default=9001, type='int')
(options, args) = optparser.parse_args()

app = create_app()
app.run(host='0.0.0.0', port=options.port)



unsigned:增加数据长度
class SentimentCountRatio(db.Model):#情绪相对比例曲线--已改
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(20))#话题名
    end = db.Column(db.BigInteger(20, unsigned=True))#时间
    range = db.Column(db.BigInteger(10, unsigned=True))
    count = db.Column(db.BigInteger(20, unsigned=True))
    allcount = db.Column(db.BigInteger(20, unsigned=True))
    sentiment = db.Column(db.Integer(1, unsigned=True))#情绪类型（'happy','angry','sad'）

    def __init__(self, query, end, range, sentiment, count, allcount):
        self.query = query
        self.end = end
        self.range = range
        self.count = count
        self.allcount = allcount
        self.sentiment = sentiment


Python:数据库操作模块SQLAlchemy 

传说中的ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上。

q = session.query(Flow.dstIP, Flow.dstPort, func.count(Flow.id)).filter(Flow.trace_id == tid).group_by(Flow.dstIP, Flow.dstPort).all()

es删除
 curl -XDELETE 'http://219.224.134.211:9204/aoyunhui_*'

ps -ef|grep elasticsearch

es错误：
elasticsearch.exceptions.RequestError: TransportError(400, u'MapperParsingException[failed to parse [cluster_dump_dict]]; nested: ElasticsearchIllegalArgumentException[unknown property [4002306389199260]]; ')
存的时候要json.dumps

错误：
<type 'exceptions.Exception'> TransportError(400, u'MapperParsingException[object mapping for [subopinion] tried to parse field [ratio] as object, but got EOF, has a concrete value been provided to it?]')
第一次存了有数据，但mapping后来新加了了  再存就不行了

root@ubuntu2:~#
curl -XPUT 'http://219.224.134.211:9204/_cluster/settings' -d '{"transient":{"cluster.routing.allocation.disk.watermark.low":"95%","cluster.routing.allocation.disk.watermark.high":"30gb","cluster.info.update.internal":"1m"}}'

df -h linux查看空间大小


cmd = 'ps -ef|grep %s|grep -v "grep"' % p_name
grep——查看什么东西
-v  去掉什么东西
——去掉有grep的那些进程

cmd = 'ps -ef|grep %s|grep -v "grep"' % p_name
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
if p.wait() == 0:
    val = p.stdout.read()
    print val
    if p_name in val:
        print "ok - %s python process is running" % p_name
else:
    print "no process is running!"
    os.system("python ./%s &" % p_name)


github建库
在主目录下
$ ssh-keygen -t rsa -C "youremail@example.com"

在用户主目录里找到.ssh目录，里面有id_rsa和id_rsa.pub两个文件，这两个就是SSH Key的秘钥对，id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，可以放心地告诉任何人。

第2步：登陆GitHub，打开“Account settings”，“SSH Keys”页面：

然后，点“Add SSH Key”，填上任意Title，在Key文本框里粘贴id_rsa.pub文件的内容

在本地新建一个文件夹，再里面git init 
在github上新建一个仓库
在本地可以修改修改commit
在本地git remote add origin https://github.com/jianjian0dandan/info_consume.git
第一次提交的时候git push -u origin main


如下，我把src里的全部移除，但是本地文件还保留。

git rm -r -n --cached  */src/\*      //-n：加上这个参数，执行命令时，是不会删除任何文件，而是展示此命令要删除的文件列表预览。


git rm -r --cached  */src/\*      //最终执行命令.

错误：
error: Failed connect to github.com:443; Connection timed out while accessing https://jianjian0dandan@github.com/jianjian0dandan/info_consume.git/info/refs
fatal: HTTP request failed

多个github帐号的SSH key切换
http://www.tuicool.com/articles/7nMBVf

mod = Blueprint('topic_language_analyze',__name__,url_prefix='/topic_language_analyze')
@mod.route('/show_daily_trend/')   后面也有个斜杠！


__builtin__  内建模块

@xxx  修饰符，对下面的这个函数先用修饰符里的方法

def get_uid_list():
    uid_list = []
    f = open('./uid.txt','r')
    for line in f.readlines():
        uid_list.append(line.strip('\n\r'))
    return uid_list
读一个txt，把换行符去掉


你把所有涉及到绝对路径的地方都写成变量，写一个parameter.py文件，在这个文件里面放你所有绝对路径的变量。这样其他地方使用的时候就直接引用这个文件就好。而且也便于你后面在其他服务器上部署
flask 中的views
路径相对来说是运行那个文件入口路径
所以你要更改相对路径啊#   所以还是写绝对路径吧

我是说route加了斜杠的话。。 访问的时候 路径后面可以加/和不加/都能访问。。

不加的话  就只能匹配到不加的

flask: 
g.user.name     flask.g是flask里面的一个全局变量，在我们这里是用来存储当前登录的用户的，不用Import 0.0
http://flask.pocoo.org/docs/0.11/api/#flask.g
http://flask.pocoo.org/docs/0.11/templating/
flask学习之五：用户登录
http://www.tuicool.com/articles/bEJNjai


git add后又想撤回：git reset HEAD xxx.py
 Changes to be committed:
 (use "git reset HEAD <file>..." to unstage)

错误：json.loads时解码错误:
 return _default_decoder.decode(s)
编码格式的转换问题：
hashtag = hashtag.encode('utf8')
hashtag = json.loads(hashtag)

错误：/usr/local/lib/python2.7/dist-packages/sqlalchemy/engine/default.py:320: Warning: Data truncated for column 'weibos' at row 1
  cursor.execute(statement, parameters)


id和limit是联合主键：
只要id和limit唯一就行
limit不一定需要唯一


mysql:有时候会锁死
查看进程
show processlist
然后Kill XXX了
(比较粗暴)

falsk里的mysql操作
http://blog.csdn.net/happy_bigqiang/article/details/50935935

方法加括号啊！！！
    if item_exist:
        db.session.delete(item_exist)
    db.session.add(item)
db.session.commit()

show variables like '%time%';看有哪些


首先按-4排序  然后按-2  然后按-6
 sorted(results, key=operator.itemgetter(-4, -2, -6), reverse=True)



/etc/crontab文件    定时任务

错误：
 ! [remote rejected] main -> main (pre-receive hook declined)
error: failed to push some refs to 'https://github.com/jianjian0dandan/own_weibo.git'
原因；
可能是因为有超大文件搞的。。然后又没删掉，走投无路，把git文件删了，重新init了一个。。。然后只上传一个文件，可以了

错误：
fatal: Couldn't find remote ref main'
解决：
git remote rm origin 

----


github错误:
The requested URL returned error: 403 Forbidden while accessing

解决方案：

vim .git/config


修改

[plain] view plain copy print?在CODE上查看代码片派生到我的代码片
[remote "origin"]  
    url = https://github.com/wangz/example.git  
为：
[plain] view plain copy print?在CODE上查看代码片派生到我的代码片
[remote "origin"]  
    url = https://wangz@github.com/wangz/example.git  
再次git push，弹出框输入密码，即可提交


tmux ls 查看进程
tmux attach连接到上次连接的进程
tmux attach-session -t 1   连接到序号是1的进程

r
以读方式打开文件，可读取文件信息。
w
以写方式打开文件，可向文件写入信息。如文件存在，则清空该文件，再写入新内容
a
以追加模式打开文件（即一打开文件，文件指针自动移到文件末尾），如果文件不存在则创建
r+
以读写方式打开文件，可对文件进行读和写操作。
w+
消除文件内容，然后以读写方式打开文件。
a+
以读写方式打开文件，并把文件指针移到文件尾。
b
以二进制模式打开文件，而不是以文本模式。该模式只对Windows或Dos有效，类Unix的文件是用二进制模式进行操作的。


csc，csr,分别是按照列和行对数据进行存储的
如果矩阵的列数较大，即行数较少，用csr格式
如果矩阵的行数较大，即列数较少，用csc格式

稀疏表示形式是记录了矩阵中的位置和对应的值，其他位置默认为0

github有冲突：
Step 1: From your project repository, check out a new branch and test the changes.

git checkout -b Gloriajuice-main main
git pull https://github.com/Gloriajuice/info_consume.git main
Step 2: Merge the changes and update on GitHub.

git checkout main
git merge --no-ff Gloriajuice-main
git push origin main


igraph  
https://pypi.python.org/pypi/python-igraph
从官网下的包 解压 安装

错误：
from igraph._igraph import *
ImportError: No module named _igraph
原因：
我是在解压完的包的路径里直接python测试的，这时候igraph是个文件夹，它以为我直接从文件夹里引的，
应该出来这个路径，在别的地方试试就可以了  finally!

 g2=g.simplify() 简化图！！！去除重复边和自循环

sublime:
Cmd-n (Win: Ctrl-n) 打开编辑窗格：
然后Cmd-Shift-p (Win: Ctrl-Shift-p) 打开Command Palette，如果我想写ruby代码，我就敲ssru

shit+alt+2  开两列窗口

ipython

%timeit

这个命令用来测试一条命令执行的时间，一般而且，会重复100次运行这个命令，然后取出最好的3个结果取平均值。

试着执行下面的命令:

In[1]: %timeit [x*x for x in range(100000)]

dir(logging)
看logging都有什么方法、属性


igraph

>>> for e in g.es:
... print e.tuple   打印边

 g.vs[2]  第二个点
  g.vs[2]['name']第二个点的名字

  g.vs['name']

  g.vs[2,3,4]['name']取这几个点的名字

 for i in g.vs:打印出属性
    ...:     print i.attributes()


    for i in g.vs:
        if i['name']==12:
            print i.index

    g.vs.find(name="foo")

        for i in g.vs.select(name_in=clusters):   name是属性名，in是在这个里面
            print i.index

g.get_adjacency(attribute='weight').data   得到以weight值为权重的邻接矩阵的值，不写attribute的话默认都是1


    adj = nx.adjacency_matrix(graph)  生成邻接矩阵
    print adj.todense().tolist()   把邻接矩阵的csx_matrix的形式变成matrix再变成list

palette: the palette that can be used to map integer color indices
to colors when drawing vertices

比如Graph是g，已知边序号是0：
g.es[0].source
g.es[0].target
g.es[0].tuple
es边，vs点
igraph maintains an internal mapping from names to vertex IDs (just like the one you proposed) for the name vertex attribute, which is automatically updated whenever you add or delete vertices. If there are multiple vertices with the same name, the mapping selects an arbitrary vertex and then returns that one (consistently) for name lookups. Behind the scenes this is all done with a standard Python dictionary. So, you can safely do all the following:

use vertex names instead of vertex IDs whenever an igraph function or method requires a vertex ID
use g.vs.find("foo") to find an arbitrary vertex with name equal to "foo".

错误：
写了；seq['color'] = (1.0, 128/255.0, 0.0, 1.0)
 palette index used when no palette was given
应该是这样：
    pal = RainbowPalette(n=len(clusters))
    for i in range(0,len(clusters)):
        seq = graph.vs.select(clusters[i])
        seq['color'] = i   这写第几个
    plot(graph,name+'.png',palette=pal)  这写用的哪个palette


logging讲解：
http://blog.csdn.net/zyz511919766/article/details/25136485
import logging 

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO,filename='./log/tsai_comment.log',filemode='a')

logging.info("loop %s" % i)

logging库提供了多个组件：Logger、Handler、Filter、Formatter。Logger对象提供应用程序可直接使用的接口，Handler发送日志到适当的目的地，Filter提供了过滤日志信息的方法，Formatter指定日志显示格式。

python 输出重定向
http://www.jb51.net/article/90506.htm

如果在两个py文件里都import过logging，设置了basicconfig等信息，就会以第一个（最开始定义的Logging）为主，写在第一个的设置里
   
        print "\n# Walktrap Clustering:"
    dendrogram = graph.community_walktrap()
    clusters = dendrogram.as_clustering()
    print "---Walktrap Clustering found %s clusters ---" % len(clusters)
    print clusters.modularity
    #plot_graph(clusters)
    pal = ClusterColoringPalette(n=100)#RainbowPalette
    plot(clusters,'famous.png',palette = pal)   


cluto  vcluster  permission denied

要到对应的路径的chmod 777 vcluster

.sh文件 执行不了
http://chenzhou123520.iteye.com/blog/1832890

a = ['1','2','3']
b = ','.join(a)
print b
>>>'1,2,3'

在后台print 出来的代码有//u...或者是x235m这种的 不一定错，有可能是print过程中的编码问题，在内存里它还是原样

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
检查参数的类型  是不是int  float里的

所以，定义默认参数要牢记一点：默认参数必须指向不变对象！  （不能是list）


可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

函数的参数

阅读: 154842
定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。

Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

默认参数

我们仍以具体的例子来说明如何定义函数的默认参数。先写一个计算x2的函数：

def power(x):
    return x * x
当我们调用power函数时，必须传入有且仅有的一个参数x：

>>> power(5)
25
>>> power(15)
225
现在，如果我们要计算x3怎么办？可以再定义一个power3函数，但是如果要计算x4、x5……怎么办？我们不可能定义无限多个函数。

你也许想到了，可以把power(x)修改为power(x, n)，用来计算xn，说干就干：

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
对于这个修改后的power函数，可以计算任意n次方：

>>> power(5, 2)
25
>>> power(5, 3)
125
但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码无法正常调用：

>>> power(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: power() takes exactly 2 arguments (1 given)
这个时候，默认参数就排上用场了。由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
这样，当我们调用power(5)时，相当于调用power(5, 2)：

>>> power(5)
25
>>> power(5, 2)
25
而对于n > 2的其他情况，就必须明确地传入n，比如power(5, 3)。

从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：

一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

二是如何设置默认参数。

当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

使用默认参数有什么好处？最大的好处是能降低调用函数的难度。

举个例子，我们写个一年级小学生注册的函数，需要传入name和gender两个参数：

def enroll(name, gender):
    print 'name:', name
    print 'gender:', gender
这样，调用enroll()函数只需要传入两个参数：

>>> enroll('Sarah', 'F')
name: Sarah
gender: F
如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加。

我们可以把年龄和城市设为默认参数：

def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city
这样，大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数：

>>> enroll('Sarah', 'F')
Student:
name: Sarah
gender: F
age: 6
city: Beijing
只有与默认参数不符的学生才需要提供额外的信息：

enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')
可见，默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现。无论是简单调用还是复杂调用，函数只需要定义一个。

有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。

也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。

默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：

先定义一个函数，传入一个list，添加一个END再返回：

def add_end(L=[]):
    L.append('END')
    return L
当你正常调用时，结果似乎不错：

>>> add_end([1, 2, 3])
[1, 2, 3, 'END']
>>> add_end(['x', 'y', 'z'])
['x', 'y', 'z', 'END']
当你使用默认参数调用时，一开始结果也是对的：

>>> add_end()
['END']
但是，再次调用add_end()时，结果就不对了：

>>> add_end()
['END', 'END']
>>> add_end()
['END', 'END', 'END']
很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。

原因解释如下：

Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

所以，定义默认参数要牢记一点：默认参数必须指向不变对象！

要修改上面的例子，我们可以用None这个不变对象来实现：

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
现在，无论调用多少次，都不会有问题：

>>> add_end()
['END']
>>> add_end()
['END']
为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

可变参数

在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。

要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
但是调用的时候，需要先组装出一个list或tuple：

>>> calc([1, 2, 3])
14
>>> calc((1, 3, 5, 7))
84
如果利用可变参数，调用函数的方式可以简化成这样：

>>> calc(1, 2, 3)
14
>>> calc(1, 3, 5, 7)
84
所以，我们把函数的参数改为可变参数：

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：

>>> calc(1, 2)
5
>>> calc()
0
如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：

>>> nums = [1, 2, 3]
>>> calc(nums[0], nums[1], nums[2])
14
这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：

>>> nums = [1, 2, 3]
>>> calc(*nums)
14

关键词参数   **   自动组成了个字典
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

参数组合
在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

>>> func(1, 2)
a = 1 b = 2 c = 0 args = () kw = {}
>>> func(1, 2, c=3)
a = 1 b = 2 c = 3 args = () kw = {}
>>> func(1, 2, 3, 'a', 'b')
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
>>> func(1, 2, 3, 'a', 'b', x=99)
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}

尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。

>>> L[:10:2]
[0, 2, 4, 6, 8]

>>> from collections import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True

>>> for i, value in enumerate(['A', 'B', 'C']):  Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
...     print i, value
...
0 A
1 B
2 C

for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]

>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']


所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。
第一种：
>>> L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x104feab40>


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

首字母大写：
a = ['adam', 'LISA', 'barT']
print map(lambda x: x.capitalize(),a)
map 对后一个列表里的值都进行前面函数的操作
reduce 把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
a = [1,3,5,6,8,4,2,2]
print reduce(lambda x,y: x*y,a)

返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

import pdb
pdb.set_trace()
然后直接运行   进入到设置这个断点的地方
p xxx 打印出来
n 下一步
q 退出


print graph.get_adjacency().data


另一个函数 np.in1d ，测试一个数组的值和另一个的关系，返回一个布尔数组：

In [181]: values = np.array([6, 0, 0, 3, 2, 5, 6])
In [182]: np.in1d(values, [2, 3, 6])
Out[182]: array([ True, False, False, True, True, False, True], dtype=bool)

无向图的邻接矩阵是对称的


networkx

G.number_of_edges(),G.number_of_nodes()
g.edges()看有哪些边
g['7188']['9993']['weight']
g.adj  邻接矩阵，字典形式
  '9970': {'weight': 2.9775171065490005}},
 '7775': {'9889': {'weight': 15.8355839848},
  '9906': {'weight': 25.1593038822},
  '9931': {'weight': 24.454421908300002},
  '9950': {'weight': 27.407333783000006},
  '9955': {'weight': 20.105192690980004},
  '9956': {'weight': 21.78847212394},
  '9959': {'weight': 21.413525149660003},
  '9961': {'weight': 10.17659818113},
  '9977': {'weight': 17.905179158190002},
  '9988': {'weight': 10.7795235828},
  '9992': {'weight': 11.46514632279},
  '9996': {'weight': 4.83720079228}},

for i in g.adjacency_iter():
    print i
('8489', {'9938': {'weight': 11.05805459438}, '9979': {'weight': 12.0239491567}, '9996': {'weight': 7.6543851711}})
('7464', {'9905': {'weight': 11.744575796420001},'9996': {'weight': 5.5160876431100005}})

for n,nbrs in g.adjacency_iter():
    for nbr,eattr in nbrs.items():
        print (n,nbr,eattr['weight'])

 tu_g = Graph.TupleList(read_list,weights=True)  #igraph

生成e-r图     BRANDES--优化了方法   降低复杂度
erdos_renyi_graph(n,p)
fat_gnp_random_graph(n,p)

linux 
top   看cpu占用前几
htop m 按内存看
htop p 按cpu看

 vim跨文件多行复制
 1、用vim打开一个文件，例如：original.trace

2、在普通模式下，输入：":sp"（不含引号）横向切分一个窗口，或者":vsp"纵向切分一个窗口，敲入命令后，你将看到两个窗口打开的是同一个文件

3、在普通模式下，输入：":e new.trace"，在其中一个窗口里打开另一个文件

4、切换到含有源文件（original.trace）的窗口，在普通模式下，把光标移到你需要复制内容的起始行，然后输入你想复制的行的数量（从光标所在行往下计算），在行数后面接着输入yy，这样就将内容复制到临时寄存器里 了（在 普通模式下ctrl+w，再按一下w，可以在两个窗口之间切换）

5、切换到目标文件（new.trace）窗口，把光标移到你接收复制内容的起始行，按一下p，就完成复制了。 

替换：
 ：%s/vivian/sky/（等同于 ：g/vivian/s//sky/） 替换每一行的第一个 vivian 为 sky 

def load_graph(f, skip_rows=0,weight=False):
    g = nx.Graph()
    with open(f) as fo:
        lines = fo.readlines()[skip_rows:]
    for line in lines:
        try:
            a = line.strip('\n').split(' ')
            nodex = a[0]
            nodey = a[1]
            if weight == 'True':   在这里True要加引号，下面...×    
                weight = a[2]      weight表示不同的意思，这样就重复赋值了！低级错误

#!/usr/bin/env python
# -*- coding: utf-8 -*-
第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；

sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
运行python hello.py获得的sys.argv就是['hello.py']；

类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

Python有两个封装了setuptools的包管理工具：easy_install和pip。目前官方推荐使用pip。

如果我们要添加自己的搜索目录，有两种方法：

一是直接修改sys.path，添加要搜索的目录：

>>> import sys
>>> sys.path.append('/Users/michael/my_py_scripts')
这种方法是在运行时修改，运行结束后失效。

第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

从Python 2.7到Python 3.x就有不兼容的一些改动，比如2.x里的字符串用'xxx'表示str，Unicode字符串用u'xxx'表示unicode，而在3.x中，所有字符串都被视为unicode，因此，写u'xxx'和'xxx'是完全一致的，而在2.x中以'xxx'表示的str就必须写成b'xxx'，以此表示“二进制字符串”。

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，

需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
>>> bart._Student__name
'Bart Simpson'

判断一个变量是否是某个类型可以用isinstance()判断：

>>> isinstance(a, list)
True

找个方便的方法去尝试、学习（ipython    Liaoxuefeng）

如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法:dir('ABC')

>>> hasattr(obj, 'power') # 有属性'power'吗？
True
>>> getattr(obj, 'power') # 获取属性'power'
<bound method MyObject.power of <__main__.MyObject object at 0x108ca35d0>>
>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
>>> fn # fn指向obj.power
<bound method MyObject.power of <__main__.MyObject object at 0x108ca35d0>>
>>> fn() # 调用fn()与调用obj.power()是一样的
81

Student.set_score = MethodType(set_score, None, Student)给Student这个类绑定一个set_score的方法

Python内置的@property装饰器就是负责把一个方法变成属性调用的

@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter   #property自己含有的方法，还有score.getter得到值
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

class Bat(Mammal, Flyable):
    pass
通过多重继承，一个子类就可以同时获得多个父类的所有功能。

通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。

调试pdb


要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件：

>>> f = open('/Users/michael/gbk.txt', 'rb')
>>> u = f.read().decode('gbk')
>>> u
u'\u6d4b\u8bd5'
>>> print u
测试

如果每次都这么手动转换编码嫌麻烦（写程序怕麻烦是好事，不怕麻烦就会写出又长又难懂又没法维护的代码），Python还提供了一个codecs模块帮我们在读文件时自动转换编码，直接读出unicode：

import codecs
with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
    f.read() # u'\u6d4b\u8bd5'

>>> import os
>>> os.name # 操作系统名字
'posix'

# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，
# 首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')
同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')
os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：

>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')

必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：

>>> re.match(r'^(\d+?)(0*)$', '102300').groups()
('1023', '00')

a = ['234','123141','dfss','333']
for i in a:
    try :
        print re.match(r'[\d]{3}\Z', i).group()
    except:
        print 'no'

234
no
no
333        

加密and登陆login
#-*-coding:utf-8-*-
import hashlib

db = {}

def get_md5(uname):
    md5 = hashlib.md5()
    md5.update(uname)
    return md5.hexdigest()

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
    return db

def login(username, password):
    if db.has_key(username):
        if db[username]== get_md5(password + username + 'the-Salt'):
            print 'pass'
        else:
            print 'wrong password'
    else:
        print 'wrong name'


register('gina','aaa')
register('gina2','aaa')
login('gina4','aaa')
login('gina','bbb')
login('gina','aaa')

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))
# 发送数据:
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)
# 关闭连接:
s.close()
header, html = data.split('\r\n\r\n', 1)
print data

UDP的使用与TCP类似，但是不需要建立连接。此外，服务器绑定UDP端口和TCP端口互不冲突，也就是说，UDP的9999端口与TCP的9999端口可以各自绑定。

响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误；

from flask import Flask
from flask import request

run.py里有g    g.user=current_user
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()

这就是传说中的MVC：Model-View-Controller，中文名“模型-视图-控制器”。

Python处理URL的函数就是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等；

包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。

MVC中的Model在哪？Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据。

__enter__和__exit__配合起来用于实现with

with open(fn) as fp:
    pass


    # urls.py
from transwarp.web import get, view
from models import User, Blog, Comment

@view('test_users.html')
@get('/')
def test_users():
    users = User.find_all()
    return dict(users=users)!!!!!

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Test users - Awesome Python Webapp</title>
</head>
<body>
    <h1>All users</h1>
    {% for u in users %}!!!!!
    <p>{{ u.name }} / {{ u.email }}</p>
    {% endfor %}
</body>
</html>    

错误：
IndexError: invalid index to scalar variable.
索引不能找到值，我这里是字符串形式，不是数字，所以不能找到值

如何自定义Flask中的响应类
http://www.jianshu.com/p/b09e1884048a
from flask import make_response
    response = make_response(results)
    response.headers['Content-Type'] = 'text/xml'
    返回xml形式的数据

关于响应
视图函数的返回值会被自动转换为一个响应对象。如果返回值是一个字符串， 它被转换为该  字符串为主体的、状态码为 200 OK``的 、 MIME 类型是 ``text/html 的响应对象。Flask 把返回值转换为响应对象的逻辑是这样：
                                                                                    (response,       status,               headers)
如果返回的是一个合法的响应对象，它会从视图直接返回。
如果返回的是一个字符串，响应对象会用字符串数据和默认参数创建。
如果返回的是一个元组，且元组中的元素可以提供额外的信息。这样的元组必须是 (response, status, headers) 的形式，且至少包含一个元素。 status 值会覆盖状态代码， headers 可以是一个列表或字典，作为额外的消息标头值。
如果上述条件均不满足， Flask 会假设返回值是一个合法的 WSGI 应用程序，并转换为一个请求对象。

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp


from optparse import OptionParser 
parser = OptionParser() 
parser.add_option("-p", "--pdbk", action="store_true", 
                  dest="pdcl", 
                  default=False, 
                  help="write pdbk data to oracle db") 
add_option用来加入选项，action是有store，store_true，store_false等，dest是存储的变量，default是缺省值，help是帮助提示 



gensim:
错误：
: VisibleDeprecationWarning: non integer (and non boolean) array-likes will not be accepted as indices in the future
lda模型输入的不是词频，是tf-idf的时候报了错，要输入整数。。？

/usr/local/lib/python2.7/dist-packages/gensim/models/ldamodel.py:638: VisibleDeprecationWarning: using a non-integer number instead of an integer will result in an error in the future
  score += numpy.sum(cnt * logsumexp(Elogthetad + Elogbeta[:, id]) for id, cnt in doc)
638行   366行 大概     里面的id换成int(id)    取对应的列数

In [33]: print ~np.array([True, False])
[False  True]

a = np.array([[1,2],[2,3],[3,4]])

np.column_stack((a,a**2))
Out[8]: 
array([[ 1,  2,  1,  4],
       [ 2,  3,  4,  9],
       [ 3,  4,  9, 16]])
o Sunshine(408622796)  21:52:32
hstack和column_stack有什么区别吗
深圳-数据分析-self(779252758)  21:58:25
效果一样吧，而且
Equivalent to ``np.concatenate(tup, axis=1)``


矩阵的转置：单纯的行列换位置
np.dot(a,b)用来计算数组的点积；
要是直接把两个np.array类型 当做矩阵A*B的话，得到的只是对应位置的值相乘，要以矩阵的形式乘，要用dot

lda模型每次的参数都是随机的，要想稳定的话，可以用np.random.seed(10)这样

scipy   
from scipy.special import comb, perm

>> perm(3, 2)
6.0   全排列A
>> comb(3, 2) 
3.0    C
psi: gamma函数的对数倒数

In [60]: z=np.array([[1,2,3],[4,5,6]])

In [61]: y=np.array([1,1])

In [62]: z-y
ValueError: operands could not be broadcast together with shapes (2,3) (2,)
In [63]: z-y[:,np.newaxis]
Out[63]:
array([[0, 1, 2],
       [3, 4, 5]])


遍历某个文件夹的文件并读出来
walk = os.walk('./Reduced')
for root, dirs, files in walk:
    print root,dirs,files
    for name in files:
        f = open(os.path.join(root, name), 'r')
    raw = f.read()

crontab
#0,15,30,45 * * * * root cd /home/ubuntu2/jiangln/info_consume/user_portrait/user_portrait/cron/group/;./timer.sh

;表示一句话结束
*/15 * * * * root cd /home/ubuntu2/jiangln/info_consume/user_portrait/user_portrait/user_rank && python Keyword_task.py >> /home/log/keyword.log
每15分钟计算一次

转发树api
 

http://api.t.sina.com.cn/statuses/show/:id.(json%7cxml)

 http://api.t.sina.com.cn/statuses/show/3989700941171337.json?source=3105114937
 http://api.t.sina.com.cn/statuses/repost_timeline.json?source=3105114937&id=3989700941171337

url里有中文的画 可能会报编码错误  加编码
 request = urllib2.Request(url.encode('utf-8')) 


__file__
__file__ 是用来获得模块所在的路径的，这可能得到的是一个相对路径，比如在脚本test.py中写入：

#!/usr/bin/env python
print __file__

按相对路径./test.py来执行，则打印得到的是相对路径，
按绝对路径执行则得到的是绝对路径。
而按用户目录来执行（~/practice/test.py），则得到的也是绝对路径（~被展开）
所以为了得到绝对路径，我们需要 os.path.realpath(__file__)。
而在Python控制台下，直接使用print __file__是会导致  name ‘__file__’ is not defined错误的，因为这时没有在任何一个脚本下执行，自然没有 __file__的定义了。


类的专有方法：
__init__  构造函数，在生成对象时调用
__del__   析构函数，释放对象时使用
__repr__ 打印，转换
__setitem__按照索引赋值
__getitem__按照索引获取值
__len__获得长度
__cmp__比较运算
__call__函数调用

__add__加运算
__sub__减运算
__mul__乘运算
__div__除运算
__mod__求余运算
__pow__称方


行内函数:
attri_dict['low']=[round(k,3) for k in temp if k < mid]
||
||
\/
low=[round(k,3) if k < mid else 0 for k in temp]
attri_dict['low'] = filter(filter_zero,low)
def filter_zero(k):
    return k > 0

a = max(b)取最大值


决策树：
总熵  
熵i-每个维度下种类  -sum(p*log2(p))
信息增益   gian = total-sum((i的比例)*entropys[i])  选最大的
数值型：切n-1刀，得到其中gian最大的是它的gain

spyder step into 到函数里面  Ctrl+F11
继续   CTRL+F12到下一个断点的地方