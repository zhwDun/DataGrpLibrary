import logging
import requests
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('Listener')


def reporting_results(func):
    """
    上报结果装饰器
    """

    def inner1(self, *args, **kwargs):
        data = func(self, *args, **kwargs)
        print(data)
        print("这是装饰器一结束")

    return inner1


class RobotListener(object):
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, product, tc_typ, executor='automation'):
        """
        :param product:产品
        :param sprint:迭代名称
        :param tc_id:用例ID
        :param tc_name:用例名称
        :param tc_type:用例类型
        :param tc_pri:用例优先级
        :param tc_relate_app:用例关联应用
        :param exec_env:执行环境
        :param exec_scheme:所属场景名称
        :param exec_stage:用例执行阶段
        :param exec_atplatform:执行该用例的自动化平台
        :param exec_date:执行时间 YYYY-mm-dd HH:MM:SS
        :param exec_dure:执行时长毫秒
        :param exec_rlt:执行结果 失败 通过
        :param executor:执行人
        """
        self.data_dic = [{'product': product, 'sprint': None, 'tc_id': 0, 'tc_name': None,
                          'tc_typ': int(tc_typ), 'tc_pri': None, 'tc_relate_app': None,
                          'exec_env': None, 'exec_scheme': None, 'exec_stage': 'uat',
                          'exec_atplatform': 'RobotFramework', 'exec_date': None,
                          'exec_dura': None,
                          'exec_rlt': None, 'executor': executor}]

    def start_suite(self, name, attributes):
        """
         start_suite:测试集合开始执行调用
        """
        print('start_suite')

    def end_suite(self, name, attributes):
        """
         end_suite:测试集合执行结束调用
        """
        print('end_suite')

    def start_test(self, name, attributes):
        """
         start_test:测试用例开始执行调用
        """
        print('start_test')

    def end_test(self, name, attributes):
        """
         end_test:测试用例执行结束调用
        """
        print('end_test')

    def start_keyword(self, name, attributes):
        """
         start_keyword:关键字开始执行调用
        """
        print('start_keyword')
        return '1234567890'

    @reporting_results
    def end_keyword(self, name, attributes):
        """
        end_keword：关键字执行结束调用
        """
        # print('该关键字执行时间: %s' % attributes['elapsedtim'])
        logger.info('太刺激了')
        print('该关键字的名字： %s' % name)
        # print('该关键字的名字： %s' % attributes['kwname'])
        return self.data_dic


if __name__ == '__main__':
    a = RobotListener('核心系统', '2')
    b = a.end_keyword('1234', '222')
