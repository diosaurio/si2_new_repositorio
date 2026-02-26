VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

.PHONY: venv migrations populate_db run clean

# 1. 创建虚拟环境并安装依赖
venv:
	@echo "正在创建虚拟环境..."
	python3 -m venv $(VENV)
	@echo "正在升级 pip 并安装依赖..."
	$(PIP) install --upgrade pip
	@if [ -f requirements.txt ]; then $(PIP) install -r requirements.txt; fi
	@echo "虚拟环境准备就绪。"

# 2. 执行 Django 迁移
migrations:
	@echo "正在生成并应用数据库迁移..."
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate

# 3. 填充数据库
populate_db:
	@echo "正在初始化数据库数据..."
	# 这里替换成你实际的数据填充命令，例如 loaddata 或自定义脚本
	$(PYTHON) manage.py populate

# 4. 运行开发服务器
run:
	$(PYTHON) manage.py runserver

# 清理环境
clean:
	rm -rf $(VENV)
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete