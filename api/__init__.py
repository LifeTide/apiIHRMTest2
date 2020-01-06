import app
import logging

# 初始化日志
# 为什么要在api.__init__.py中初始化日
app.init_logging()

logging.info("TEST日志器能不能正常工作")
