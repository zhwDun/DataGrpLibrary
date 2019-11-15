import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('Listener')


class RobotListener(object):
    ROBOT_LISTENER_API_VERSION = 2

    def start_suite(self, name, args):
        logger.info("Starting Suite : " + name + "  " + args['source'])
        logger.info('start_suite')
        self.starttime = args['starttime']
        print(self.starttime)

    def start_test(self, name, args):
        logger.info("Starting test : " + name)
        logger.info('start_test')
        print('start_test')

        if args['template']:
            logger.info('Template is : ' + args['template'])
            logger.info('start_test_args')
            print('start_test_args')

    def end_test(self, name, args):
        logger.info("Ending test:  " + args['longname'])
        logger.info('end_test')
        print('end_test')
        self.endtime = args['endtime']
        exec_date = self.endtime - self.starttime
        print(exec_date)

        logger.info("Test Result is : " + args['status'])

        logger.info("Test Time is: " + str(args['elapsedtime']))

    # def log_message(self, message):
    #     logger.info( " :   " + message + " : " + messagedd)
    #     logger.info('message')
    #     print(log_message)
