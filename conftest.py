
from datetime import datetime
# import pymysql  # 使用pymysql作为示例，可根据实际数据库调整
import pytest
from typing import Generator, Any


import logging
import pytest

@pytest.fixture(autouse=True)
def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    yield



@pytest.fixture(scope='session')
def fixtt():
    print(datetime.now(),"我是套娃fixture")

    yield
    print(datetime.now(),"hahaha")

@pytest.fixture(autouse=True,scope='session')
def fixt():
    print(datetime.now(),"用例开始执行")

    yield
    print(datetime.now(),"用例执行结束")


# # 数据库配置信息（建议从环境变量或配置文件中读取）
# DB_CONFIG = {
#     'host': 'localhost',
#     'user': 'your_username',
#     'password': 'your_password',
#     'database': 'your_database',
#     'port': 3306,
#     'charset': 'utf8mb4'
# }


# @pytest.fixture(scope="session")
# def db_connection() -> Generator[Any, None, None]:
#     """
#     Session级别的fixture，用于在整个测试会话期间创建和关闭数据库连接
#     前置操作：建立数据库连接
#     后置操作：关闭数据库连接
#     """
#     connection = None
#     try:
#         # 前置操作：连接数据库
#         print("\n=== 建立数据库连接 ===")
#         connection = pymysql.connect(**DB_CONFIG)

#         # 返回连接对象给测试用例使用
#         yield connection

#     except Exception as e:
#         print(f"数据库连接失败: {e}")
#         pytest.fail(f"数据库连接异常: {e}")

#     finally:
#         # 后置操作：关闭数据库连接
#         if connection:
#             connection.close()
#             print("=== 关闭数据库连接 ===\n")


# # 如果需要事务自动回滚，可以使用以下fixture
# @pytest.fixture(scope="function")
# def db_transaction(db_connection) -> Generator[Any, None, None]:
#     """
#     函数级别的fixture，每个测试函数自动回滚事务
#     确保测试不会影响数据库状态
#     """
#     # 开始事务
#     db_connection.begin()

#     yield db_connection

#     # 测试完成后回滚事务
#     db_connection.rollback()
