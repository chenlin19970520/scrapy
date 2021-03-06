# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from scrapy.exceptions import DropItem
import re
class GirlPipeline(ImagesPipeline):
    #
    # def file_path(self, request, response=None, info=None):
    #     """
    #     :param request: 每一个图片下载管道请求
    #     :param response:
    #     :param info:
    #     :param strip :清洗Windows系统的文件夹非法字符，避免无法创建目录
    #     :return: 每套图的分类目录
    #     """
    #     item = request.meta['item']
    #     folder = item['name']
    #
    #     folder_strip = re.sub(r'[？\\*|“<>:/]', '', str(folder))
    #     image_guid = request.url.split('/')[-1]
    #     filename = u'full/{0}/{1}'.format(folder_strip, image_guid)
    #     return filename
    def get_media_requests(self,item,info):
        for image_url in item['imgurl']:
            image_url = re.sub(r'\/\w\/','/pic/',image_url)
            print(image_url)
            yield Request(image_url,meta={'item':item['name']})
    
    def file_path(self,request,response=None,info=None):
        name = request.meta['item']
        name = re.sub(r'[？\\*|“<>:/()0123456789]', '', name)
        image_guid = request.url.split('/')[-1]
        filename = u'full/{0}/{1}'.format(name,image_guid)
        return filename
    # def item_completed(self,results,item,info):
    #     image_path=[x['path'] for ok , x is results if ok]
    #     if not image_path:
    #         raise DropItem('Item contains no images')
    #     item['image_paths']=image_path
    #     return item
    
    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['image_paths'] = image_path
        return item