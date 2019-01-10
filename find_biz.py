#!/usr/bin/env python
# coding:utf8
__author__ = 'xiamao'
__time__ = '2019/1/10 下午9:26'

import requests
import re


def get_biz_from_url(url):
    resp_ = requests.get(url).content
    title = re.findall('var nickname = "(.*?)"', resp_)
    biz = re.findall(r'var biz = ""\|\|"(.*?)"', resp_)
    accounta = re.findall('<span class="profile_meta_value">(.*?)</span>', resp_)
    biz = biz[0] if biz else ''
    title = title[0] if title else ''
    if len(accounta) >= 2:
        account = accounta[0] if accounta else ''
        desc = accounta[1] if accounta else ''
    elif len(accounta) == 1:
        account = accounta[0]
        desc = ''
    else:
        account = ''
        desc = ''
    return title, account, biz, desc


def read_biz_dict():
    biz_dict = {}
    with open('result.txt', 'r') as f:
        for line in f:
            name, acc, biz, desc = line.strip().split('###')
            if acc not in biz_dict:
                biz_dict[acc] = ''
            biz_dict[acc] = biz
    return biz_dict


def crawl_biz(keyword):
    """
    可以通过名称或者ID来获取biz
    :param keyword:
    :return:
    """
    mp_base = "http://weixin.sogou.com/weixin?type=2&s_from=input&query=%s"
    base_url = mp_base % keyword
    resp_ = requests.get(base_url)
    urls = re.findall('target="_blank" href="(.*?)"', resp_.content)
    url = urls[0].replace('&amp;', '&')
    title, account, biz, desc = get_biz_from_url(url)
    print biz
    return {'name': title, 'acc': account, 'biz': biz, 'desc': desc}


def update_biz_file(item):
    old_file = open('result.txt', 'r')
    lines = old_file.readlines()
    old_file.close()
    lines.append(item['name'] + '###' + item['acc'] + '###' + item['biz'] + '###' + item['desc'] + '\n')
    new_file = open('new.txt', 'w')
    new_file.writelines(lines)
    new_file.close()


if __name__ == '__main__':
    b_dict = read_biz_dict()
    accs = b_dict.keys()
    acc = 'newsbro'
    if acc in accs:
        print b_dict[acc]
    else:
        item = crawl_biz(acc)
        # 这里需要做一件事情，更新现有的biz映射关系，不断丰富。
        if item:
            update_biz_file(item)
