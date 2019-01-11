#!/usr/bin/env python
# coding:utf8
__author__ = 'xiamao'
__time__ = '2019/1/11 上午9:56'
import requests
import json
import time
import random

CATEGORY = 1
PER_PAGE = 20
PAGE_NO = 1
HEADERS = {
    'cookie': 'aliyungf_tc=AQAAAB1UExVZagkAis54ao59RZZWVQ0w; visit-wxb-id=9c85267d520ffe4471dca8d093b78b96; wxb_fp_id=1531789978; PHPSESSID=5f7a056b737fe0d05784c9cd7f0d1d1e; Hm_lvt_5859c7e2fd49a1739a0b0f5a28532d91=1547096730; Hm_lpvt_5859c7e2fd49a1739a0b0f5a28532d91=1547171689',
    'Host': 'data.wxb.com', 'Referer': 'https://data.wxb.com/rank?category=1&page=49',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'}
BASE_URL = 'https://data.wxb.com/rank/day/2019-01-09/{0}?sort=&page={1}&page_size=20'
C_DICT = {'1': '时事资讯', '2': '数码科技', '3': '汽车', '4': '房产家居', '5': '职场招聘', '6': '财经理财',
          '7': '生活',
          '8': '情感励志',
          '9': '女性时尚',
          '10': '旅行',
          '11': '运动健康',
          '12': '餐饮美食',
          '13': '搞笑娱乐',
          '14': '明星影视',
          '15': '母婴',
          '16': '文化教育',
          '17': '创业管理',
          '18': '政务',
          '19': '企业',
          '20': '地方',
          '21': '其他'}


def parse(json_data, f_name):
    lines = [json.dumps(l) + '\n' for l in json_data]
    with open(f_name, 'a') as f:
        f.writelines(lines)


def loop_category():
    for c in range(6, 22):
        for p in range(1, 51):
            url = BASE_URL.format(str(c), str(p))
            resp = requests.get(url, headers=HEADERS)
            data = json.loads(resp.content).get('data')
            time.sleep(random.uniform(1, 3))
            if data:
                print C_DICT[str(c)], p
                parse(data, C_DICT[str(c)])
            else:
                break


if __name__ == '__main__':
    loop_category()
