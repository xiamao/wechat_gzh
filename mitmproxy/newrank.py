#!/usr/bin/env python
# coding:utf8
__author__ = 'xiamao'
__time__ = '2019/1/10 下午9:28'
import os
import json
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


def response(flow):
    if flow.request.pretty_url.startswith("https://www.newrank.cn/xdnphb/list/"):
        with open(PATH("xinbang.tmp"), "a") as fout:
            obj = json.loads(flow.response.content)["value"]["datas"]
            for x in obj:
                fout.write("{name}###{media_id}###{biz}###{logo}\n".format(
                    name=x["name"],
                    media_id=x["account"],
                    biz=x["biz_info"],
                    logo=x["head_image_url"]
                ))
    pass