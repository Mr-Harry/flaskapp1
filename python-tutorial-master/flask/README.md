```py
if __name__ == '__main__':
    app.run()
```

最后我们用 run() 函数来让应用运行在本地服务器上。 其中 if __name__ == '__main__': 确保服务器只会在该脚本被 Python 解释器直接执行的时候才会运行，而不是作为模块导入的时候