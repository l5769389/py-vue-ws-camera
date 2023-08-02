# flask 启动
```
    python ./router.py
```

# 打包命令
```
 Pyinstaller -F ./router.py 
```


# WSGI启动

```
gunicorn router:app -b 192.168.1.122:8888
```

