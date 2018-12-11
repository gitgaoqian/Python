#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ros

class global_var:
    '''需要定义全局变量的放在这里，最好定义一个初始值'''
    name = 'my_name'

# 对于每个全局变量，都需要定义get_value和set_value接口
def set_name(name):
    global_var.name = name
def get_name():
    return global_var.name
