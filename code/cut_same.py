#-*-coding:utf-8-*

def cut():
    content = []
    #f = open('/home/jiangln/own_weibo/raw_data/content/hue_wendong_lina_100content.txt','r')
    f = open('/home/jiangln/own_weibo/raw_data/content/hue_wendong_lina_focus_usercontent_limit100.txt','r')
    for line in f:
        content.append(line[11:27])
        #print line
        #print line[11:27]
    print len(content)
    con = list(set(content))
    print len(con)
    return con

def write(con):
    #f_w = open('/home/jiangln/own_weibo/raw_data/content/100content_cuted.txt','w')
    f_w = open('/home/jiangln/own_weibo/raw_data/content/allcontent_cuted.txt','w')
    for i in con:
        f_w.write(i+'\r\n')
    f_w.close()

con = []
con = cut()
write(con)

