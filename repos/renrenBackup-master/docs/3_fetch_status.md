# 状态列表

直接去看个人的状态列表，第一页没看到 ajax 请求，想不会要做各种页面解析吧，翻了一页就看到还是 xhr 请求，这就简单了

请求参数非常简单

```python
params = {
    'userId': uid,      # 要抓取的用户 uid
    'curpage': page,    # 当前页码，从 0 开始编号
}
```

返回的数据结构比较大，有用的大概如下（部分数据已模糊化）

```python
ret = {
    "count": 999,           // 总共有多少条状态
    "doingArray": [         // 当前页的状态列表
        {
            "comment_count": 20,            # 评论数
            "content": "要的留邮箱",        # 内容
            "createTime": "1416289808000",  # 时间戳，后面还有个 dtime 用来显示，我们爬就不用了
            "id": 12345,                    # 编号，后续拿评论什么的都用的上
            "repeatCountTotal": 2,          # 转发数，还有个 repeatCount 不知道干嘛的（直接转发？）
            "rootContent": "谁有？",        # 转发原文（如果是转发，否则没这个和下面几个字段）
            "rootDoingUserId": 23456,       # 转发原用户 uid
            "rootDoingUserName": "张三",    # 转发原用户名
            "location": "静安中心",         # POI 地点名
            "locationUrl": "http://xxxxx",  # 地点链接
        },
    ],
    "likeInfoMap": {        # 点赞信息，还有个 likeMap 不知道干嘛的，跟页面对比是这个有用
        "status_12345": 1,                  # 格式是 status_{id}，用上面的来找就行了
    }
}
```

每页 20 条，页码从 0 开始，所以最大页码就是 `Math.ceil(count/20) - 1`，一路翻过去就好


## 转帖原文

转发的状态只能记住最原始的一个，在 `root***` 的字段里，如果不是转发则这几个字段会不存在，而不是为空，注意一下就好


## 地点信息

人人的状态可以加地点信息（这个似乎也是比较晚才有的），体现在数据的 `location***` 字段里，同转帖一样，没有地点信息的会不存在这个字段，而不是为空，一开始也没注意到有这个