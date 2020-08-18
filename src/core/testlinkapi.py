import os
import testlink
from core.settings import Settings
from testlink.testlinkerrors import TLResponseError


class TestlinkAPI:

    def __init__(self):
        self.config = {
            'username': 'samuel.santos',
            'api_key': 'bae5852b0e4a8ac7faa16befb5216c2d',
            'url': 'http://127.0.0.1/testlink/lib/api/xmlrpc/v1/xmlrpc.php',
            'project_id': '0',
            'plan_id': '0',
            'platform_id': '0',
            'build_id': '0',
            'build_name': ''
        }
        os.environ["TESTLINK_API_PYTHON_SERVER_URL"] = self.config['url']
        os.environ["TESTLINK_API_PYTHON_DEVKEY"] = self.config['api_key']
        self.setting = Settings('testlink.cfg')
        try:
            self.tlh = testlink.TestLinkHelper()
            self.tls = self.tlh.connect(testlink.TestlinkAPIClient)
        except TLResponseError as err:
            print(err)

    def getProjects(self):
        try:
            return self.tls.getProjects()
        except TLResponseError as err:
            print(err)

    def getPlans(self, project_id):
        try:
            return self.tls.getProjectTestPlans(project_id)
        except TLResponseError as err:
            print(err)

    def getBuilds(self, plan_id):
        try:
            return self.tls.getBuildsForTestPlan(plan_id)
        except TLResponseError as err:
            print(err)

    def getPlatforms(self, project_id):
        try:
            return self.tls.getProjectPlatforms(project_id)
        except TLResponseError as err:
            print(err)

    def reportTCResult(self, internal_id, plan, buildname, status, notes, user, platform, external_id):
        try:
            self.tls.reportTCResult(internal_id, plan, buildname, status, notes, user=user, platformid=platform,
                           testcaseexternalid=external_id)
        except TLResponseError as err:
            print(err)

    def getUsername(self):
        return self.config['username']

    def getApiKey(self):
        return self.config['api_key']

    def getUrl(self):
        return self.config['url']