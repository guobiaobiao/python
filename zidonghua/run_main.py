import pytest
from conftest import cases_path,max_fail
from base.logger import Logger
import os

logger=Logger('root').getlog()
if __name__=='__main__':
    pytest.main(["-s","--alluredir","./report/xml","--maxfail",max_fail])
    os.system('allure generate report/xml/ -o report/html --clean')
    logger.info("test end! Generate test report")