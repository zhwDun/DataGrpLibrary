import logging
import requests
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('Listener')


# 来来来

class RobotListener(object):
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, product, sprint, tc_name, tc_type, tc_pri, tc_relate_app, exec_env, exec_stage, exec_atplatform,
                 executor):
        """

        :param product:产品
        :param sprint:迭代名称
        :param tc_name:用例名称
        :param tc_type:用例类型
        :param tc_pri:用例优先级
        :param tc_relate_app:用例关联应用
        :param exec_env:执行环境
        :param exec_stage:用例执行阶段
        :param exec_atplatform:执行该用例的自动化平台
        :param executor:执行人
        """
        self.product = product
        self.sprint = sprint
        self.tc_name = tc_name
        self.tc_type = tc_type
        self.tc_pri = tc_pri
        self.tc_relate_app = tc_relate_app
        self.exec_env = exec_env
        self.exec_stage = exec_stage
        self.exec_atplatform = exec_atplatform
        self.executor = executor

    # def start_suite(self, name, args):
    #     logger.info("Starting Suite : " + name + "  " + args['source'])
    #     logger.info('start_suite')
    #     self.starttime = args['starttime']

    def start_test(self, name, args):
        print('测试名称包括父套件: %s' % args['longname'])
        print('测试用例文档: %s' % args['doc'])
        print('测试用例标签作为字符串列表: %s' % args['tags'])
        print('是或否取决于测试被认为是否关键: %s' % args['critical'])
        print('包含用于测试的模板的名称: %s' % args['template'])
        print('执行开始时间: %s' % args['starttime'])
        str = args['starttime']
        print(type(str))
        # print('start_test')

        # if args['template']:
        #     logger.info('Template is : ' + args['template'])
        #     logger.info('start_test_args')
        #     print('start_test_args')

    def end_test(self, name, args):
        print('测试名称包括父套件: %s' % args['longname'])
        print('测试用例文档: %s' % args['doc'])
        print('测试用例标签作为字符串列表: %s' % args['tags'])
        print('是或否取决于测试被认为是否关键: %s' % args['critical'])
        print('包含用于测试的模板的名称: %s' % args['template'])
        print('执行开始时间: %s' % args['starttime'])
        print('执行结束时间: %s' % args['endtime'])
        print('以整数形式执行的时间（以毫秒为单位）: %s' % args['elapsedtime'])
        print('通过或失败: %s' % args['status'])
        print('状态消息，通常是错误消息或空字符串: %s' % args['message'])
        url = 'http://www.baidu.com'
        data = {
            'product': self.product,
            'sprint': self.sprint,
            'tc_name': self.tc_name
        }
        data_json = json.dumps(data)
        res = requests.post(url=url, json=data_json)
        logger.info('发送报告成功')

    # def log_message(self, message):
    #     logger.info( " :   " + message + " : " + messagedd)
    #     logger.info('message')
    #     print(log_message)
