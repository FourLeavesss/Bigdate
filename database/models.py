from django.db import models
from django.utils.html import format_html


class PieData(models.Model):

    title = models.CharField(max_length=255,verbose_name="标题")
    tname = models.CharField(max_length=255,verbose_name="标签")
    short_link = models.CharField(max_length=255,verbose_name="链接")
    view = models.IntegerField(verbose_name="播放次数")
    author = models.CharField(max_length=255,verbose_name="作者")
    src = models.CharField(max_length=255,verbose_name="封面")
    danmaku = models.IntegerField(verbose_name="弹幕数")
    like = models.IntegerField(verbose_name="点赞数")
    share = models.IntegerField(verbose_name="分享数")
    favorite = models.IntegerField(verbose_name="收藏数")
    reply = models.IntegerField(verbose_name="评论数")
    pub_location = models.CharField(max_length=255,verbose_name="发布地区",null=True,blank=True)
    pubdate = models.DateField(verbose_name="日期",auto_now=False,null=True,blank=True)

    def __str__(self):
        return self.title

    def href_link(self):
        path = self.short_link
        button_html = "<a  href='{}'  >跳转观看</a>".format(path)
        return format_html(button_html)
    href_link.short_description = format_html("""<a  href='#' style="position: relative;left: -12px; target='_blank'  ">在线观看</a>""")

    def collection(self):
        button_html = "<a  href='/api/collection?name={}&url={}&src={}'  >点击收藏</a>".format(self.title,self.short_link,self.src)
        return format_html(button_html)
    collection.short_description = format_html("""<a  href='#' style="position: relative;left: -12px;">收藏</a>""")

    class Meta:
        verbose_name = "综合热门"
        verbose_name_plural = verbose_name
        db_table = 'PieData'




class BarData(models.Model):

    title = models.CharField(max_length=255, verbose_name="标题")
    tname = models.CharField(max_length=255, verbose_name="标签")
    short_link = models.CharField(max_length=255, verbose_name="链接")
    view = models.IntegerField(verbose_name="播放次数")
    author = models.CharField(max_length=255, verbose_name="作者")
    src = models.CharField(max_length=255, verbose_name="封面")
    danmaku = models.IntegerField(verbose_name="弹幕数")
    like = models.IntegerField(verbose_name="点赞数")
    share = models.IntegerField(verbose_name="分享数")
    favorite = models.IntegerField(verbose_name="收藏数")
    reply = models.IntegerField(verbose_name="评论数")
    pub_location = models.CharField(max_length=255,verbose_name="发布地区",null=True,blank=True)
    pubdate = models.DateField(verbose_name="发布时间", auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.title

    def href_link(self):
        path = self.short_link
        button_html = "<a  href='{}'  >跳转观看</a>".format(path)
        return format_html(button_html)

    href_link.short_description = format_html(
        """<a  href='#' style="position: relative;left: -12px; target='_blank'  ">在线观看</a>""")

    def collection(self):
        button_html = "<a  href='/api/collection?name={}&url={}&src={}'  >点击收藏</a>".format(self.title, self.short_link,self.src)
        return format_html(button_html)
    collection.short_description = format_html("""<a  href='#' style="position: relative;left: -12px;">收藏</a>""")


    class Meta:
        verbose_name = "每周必看"
        verbose_name_plural = verbose_name
        db_table = 'BarData'





class LintData(models.Model):

    title = models.CharField(max_length=255, verbose_name="标题")
    tname = models.CharField(max_length=255, verbose_name="标签")
    short_link = models.CharField(max_length=255, verbose_name="链接")
    view = models.IntegerField(verbose_name="播放次数")
    author = models.CharField(max_length=255, verbose_name="作者")
    src = models.CharField(max_length=255, verbose_name="封面")
    danmaku = models.IntegerField(verbose_name="弹幕数")
    like = models.IntegerField(verbose_name="点赞数")
    share = models.IntegerField(verbose_name="分享数")
    favorite = models.IntegerField(verbose_name="收藏数")
    reply = models.IntegerField(verbose_name="评论数")
    pub_location = models.CharField(max_length=255,verbose_name="发布地区",null=True,blank=True)
    pubdate = models.DateField(verbose_name="发布时间", auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.title

    def href_link(self):
        path = self.short_link
        button_html = "<a  href='{}'  >跳转观看</a>".format(path)
        return format_html(button_html)

    href_link.short_description = format_html(
        """<a  href='#' style="position: relative;left: -12px; target='_blank'  ">在线观看</a>""")

    def collection(self):
        button_html = "<a  href='/api/collection?name={}&url={}&src={}'  >点击收藏</a>".format(self.title, self.short_link,
                                                                                           self.src)
        return format_html(button_html)

    collection.short_description = format_html("""<a  href='#' style="position: relative;left: -12px;">收藏</a>""")

    class Meta:
        verbose_name = "入站必刷"
        verbose_name_plural = verbose_name
        db_table = 'LintData'




class BarsData(models.Model):

    title = models.CharField(max_length=255, verbose_name="标题")
    tname = models.CharField(max_length=255, verbose_name="标签")
    short_link = models.CharField(max_length=255, verbose_name="链接")
    view = models.IntegerField(verbose_name="播放次数")
    author = models.CharField(max_length=255, verbose_name="作者")
    src = models.CharField(max_length=255, verbose_name="封面")
    danmaku = models.IntegerField(verbose_name="弹幕数")
    like = models.IntegerField(verbose_name="点赞数")
    share = models.IntegerField(verbose_name="分享数")
    favorite = models.IntegerField(verbose_name="收藏数")
    reply = models.IntegerField(verbose_name="评论数")
    pub_location = models.CharField(max_length=255,verbose_name="发布地区",null=True,blank=True)
    pubdate = models.DateField(verbose_name="发布时间", auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.title

    def href_link(self):
        path = self.short_link
        button_html = "<a  href='{}'  >跳转观看</a>".format(path)
        return format_html(button_html)

    href_link.short_description = format_html(
        """<a  href='#' style="position: relative;left: -12px; target='_blank'  ">在线观看</a>""")

    def collection(self):
        button_html = "<a  href='/api/collection?name={}&url={}&src={}'  >点击收藏</a>".format(self.title, self.short_link,
                                                                                           self.src)
        return format_html(button_html)

    collection.short_description = format_html("""<a  href='#' style="position: relative;left: -12px;">收藏</a>""")

    class Meta:
        verbose_name = "热播排行"
        verbose_name_plural = verbose_name
        db_table = 'BarsData'








class History(models.Model):

    title = models.CharField(max_length=255, verbose_name="标题")
    tname = models.CharField(max_length=255, verbose_name="标签")
    short_link = models.CharField(max_length=255, verbose_name="链接")
    view = models.IntegerField(verbose_name="播放次数")
    author = models.CharField(max_length=255, verbose_name="作者")
    src = models.CharField(max_length=255, verbose_name="封面")
    danmaku = models.IntegerField(verbose_name="弹幕数")
    like = models.IntegerField(verbose_name="点赞数")
    share = models.IntegerField(verbose_name="分享数")
    favorite = models.IntegerField(verbose_name="收藏数")
    reply = models.IntegerField(verbose_name="评论数")
    pub_location = models.CharField(max_length=255,verbose_name="发布地区",null=True,blank=True)
    pubdate = models.DateField(verbose_name="发布时间", auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.title

    def href_link(self):
        path = self.short_link
        button_html = "<a  href='{}'  >跳转观看</a>".format(path)
        return format_html(button_html)

    href_link.short_description = format_html(
        """<a  href='#' style="position: relative;left: -12px; target='_blank'  ">在线观看</a>""")

    def collection(self):
        button_html = "<a  href='/api/collection?name={}&url={}&src={}'  >点击收藏</a>".format(self.title, self.short_link,
                                                                                           self.src)
        return format_html(button_html)

    collection.short_description = format_html("""<a  href='#' style="position: relative;left: -12px;">收藏</a>""")

    class Meta:
        verbose_name = "历史爬取"
        verbose_name_plural = verbose_name
        db_table = 'History'




class Colect(models.Model):

    co_title = models.CharField(verbose_name="收藏视频",max_length=255)
    co_down_link = models.CharField(verbose_name="链接",max_length=255)
    co_down_img = models.CharField(verbose_name="封面",max_length=255)

    def __str__(self):
        return self.co_title

    def href_link(self):
        path = self.co_down_link
        button_html = "<a  href='{}'  >跳转详情</a>".format(path)
        return format_html(button_html)
    href_link.short_description = format_html("""<a  href='#' style="position: relative;left: -12px; target='_blank'  ">跳转查看</a>""")

    class Meta:
        verbose_name = "收藏列表"
        verbose_name_plural = verbose_name
        db_table = 'Colect'
