#coding=utf-8
#登录：手机号登录
from utils import util_request
import GVars
import unittest
from testcaseVTownV2 import tcExecute

"""
参数名	参数类型	必传	缺省值	描述
phone	char	Y		手机号
password	char	Y		密码
"""

class Test(unittest.TestCase):
    
    def setUp(self):
        self.path = "/v1/member/passport/login"
        pass
    
    def tearDown(self):
        pass
    
    def test_00(self):
        
        testcaseName = u"302-会员登录-00"
        dataDict = {"phone":"","password":""}
        testsetDict = {}
        testsetDict[testcaseName] = dataDict
        
        tcExecute.http_post(testsetDict,self.path)
        
if __name__ == "__main__":
    unittest.main()