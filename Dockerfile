# 选择基础镜像：官方 Python 3.10 轻量版
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 将依赖文件先拷贝进容器，并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 再将项目代码拷贝进来
COPY . .

# 指定容器启动时执行的命令
# 假设你的入口脚本是 main.py
CMD ["streamlit","run", "./src/streamlit.py"]