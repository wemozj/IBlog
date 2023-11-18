# !/usr/bin/env python3 
# -*- coding: UTF-8 -*-
"""
@File     : init_db.py
@Author   : jun.zhu
@Date     : 2023/11/18 10:29
@Desc     :
"""
import sqlite3

conn = sqlite3.connect("database_db")

with open("db.sql") as f:
    conn.executescript(f.read())

# 创建一个执行句柄，用来执行后面的语句
cur = conn.cursor()

# 插入两条文章
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ("学习 Flask 1", "学习 Flask 第一部分")
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ("学习 Flask 2", "学习 Flask 第二部分")
            )

conn.commit()
conn.close()
