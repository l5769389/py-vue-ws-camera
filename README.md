# flask 启动

```
    python ./router.py
```

# 打包命令

```
 Pyinstaller -F ./router.py
```

# WSGI 启动

```
gunicorn router:app -b 192.168.1.122:8888
```

# 创建 venv 环境

```
python -m venv venv


# 安装依赖
```

pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

```

```
