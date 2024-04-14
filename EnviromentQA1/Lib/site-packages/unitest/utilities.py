import json
import logging
import os

import requests
import pytest
from FunctionalTests.FunctionalParam import FunctionalParam
import curlify

functionalParm = FunctionalParam()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
IS_LOG_CURL = bool(os.getenv('IS_LOG_CURL', False))

try:
    from Config.Defaultheader import Defaultheader

    header = Defaultheader()
except:
    pass

stagelink = "ifi/151613/"
endpoint = "https://plutus.mum1-stage.zeta.in/plutus-onboarding/send/otp"
file_name = "endPointUserConf.json"


def get_stage():
    with open(file_name) as json_file:
        properties = json.load(json_file)
        env = properties["testingEndPoint"]["env"]
    print(env)
    return env


class Utilities(object):
    response = None

    def __init__(self):
        pass

    def generate_token(self, phonenumber, otp, endpoint):
        endpoint = endpoint

        requests.request("GET", endpoint, headers=functionalParm.getHeader("defaultUser"))

    def check_status_code_turbo(self,
                                endPoint=None,
                                requestMethod="GET",
                                user="Captain_America",
                                params=None,
                                expectedStatusCode=requests.codes.ok,
                                jsonPayload=None,
                                token=None, envFile=None):
        if token != None:
            headers = {'Content-Type': 'application/json',
                       'X-Zeta-AuthToken': token}
        elif user == "userAuthToken":
            headers = functionalParm.getHeaderClearRateLImit(user, envFile)
        elif user == "userStaticToken":
            headers = functionalParm.getTokenCardApplication(user, envFile)
        elif user == "user3":
            headers = header.createIDHeaders(envFile)
        elif user == "UpdateStatusUser":
            headers = header.updateStatusHeaders(envFile)
        elif user == "ganymedeUser":
            headers = header.ganymedeHeaders(envFile)
        elif user != 'null':
            headers = functionalParm.getHeader(user, envFile)
        else:
            headers = None

        if endPoint.find("ifi/151613") == -1 and get_stage() == "beta":
            endPoint = endPoint.replace("ifi/151613", "fi/13")
        response = requests.request(requestMethod, endPoint, headers=headers, params=params, json=jsonPayload)
        # print(curlify.to_curl(response.request))
        Utilities.response = response
        if IS_LOG_CURL:
            Utilities.log_curl_req(response)

        assert response.status_code == expectedStatusCode, \
            f"Expected Status Code {expectedStatusCode} and Actual status {response.status_code} code did not match"
        logger.info(response.json())
        return response
        pass

    def check_status_code_no_response_body(self,
                                           endPoint=None,
                                           requestMethod="GET",
                                           user="Captain_America",
                                           params=None,
                                           expectedStatusCode=requests.codes.ok,
                                           jsonPayload=None, token=None, envFile=None):
        if token != None:
            headers = {'Content-Type': 'application/json',
                       'X-Zeta-AuthToken': token}
        elif user == "userStaticToken":
            headers = functionalParm.getTokenCardApplication(user, envFile)
        elif user != 'null':
            headers = functionalParm.getHeader(user, envFile)
        else:
            headers = None

        if endPoint.find("ifi/151613") == -1 and get_stage() == "beta":
            endPoint = endPoint.replace("ifi/151613", "fi/13")
        response = requests.request(requestMethod, endPoint, headers=headers, params=params, json=jsonPayload)
        Utilities.response = response
        if IS_LOG_CURL:
            Utilities.log_curl_req(response)

        assert response.status_code == expectedStatusCode, \
            f"Expected Status Code {expectedStatusCode} and Actual status {response.status_code} code did not match"

    def assert_error_message(self, response, errorKey, errorMessage):
        if response:
            assert response.json().get(errorKey) == errorMessage

    def check_status_code(self,
                          endPoint=None,
                          requestMethod="GET",
                          user="Captain_America",
                          params=None,
                          expectedStatusCode=requests.codes.ok,
                          jsonPayload=None):
        if user != 'null':
            headers = functionalParm.getHeader(user)
        else:
            headers = None

        if (endPoint.find(stagelink) != -1) and (get_stage() == 'beta'):
            endPoint = endPoint.replace("ifi/151613", "ifi/13")
        elif (endPoint.find(stagelink) != -1) and (get_stage() == 'LZ'):
            endPoint = endPoint.replace("ifi/151613", "ifi/1")
        response = requests.request(requestMethod, endPoint, headers=headers, params=params, json=jsonPayload)
        Utilities.response = response
        if IS_LOG_CURL:
            Utilities.log_curl_req(response)
        try:
            assert response.status_code == expectedStatusCode, \
                f"Expected Status Code {expectedStatusCode} and Actual status {response.status_code} code did not match"
            return response
        except:
            logger.error(response.headers)
            pytest.fail(
                f"Expected Status Code {expectedStatusCode} and Actual status {response.status_code} code did not match and response is {response.json()}")

    def check_user_authentication(self,
                                  endPoint,
                                  requestMethod="GET",
                                  user="DeadPool",
                                  params=None,
                                  expectedStatusCode=requests.codes.unauthorized,
                                  jsonPayload=None):
        if user != 'null':
            headers = functionalParm.getHeader(user)
        else:
            headers = None

        if (endPoint.find(stagelink) != -1) and (get_stage() == 'beta'):
            endPoint = endPoint.replace("ifi/151613", "ifi/13")
        response = requests.request(requestMethod, endPoint, headers=headers, params=params, json=jsonPayload)
        Utilities.response = response
        if IS_LOG_CURL:
            Utilities.log_curl_req(response)

        assert response.status_code == expectedStatusCode, \
            "Expected and Actual status code did not match"
        logger.info(response.json())
        return response
        pass

    def null_check(self, ):
        raise NotImplementedError("not implemented")

    def empty_check(self):
        raise NotImplementedError("not implemented")

    def schema_validation(self):
        raise NotImplementedError("not implemented")

    def db_validation(self):
        raise NotImplementedError("not implemented")

    def check_status_code_with_custom_header(self,
                                             endPoint=None,
                                             requestMethod="GET",
                                             headers=None,
                                             params=None,
                                             expectedStatusCode=requests.codes.ok,
                                             jsonPayload=None):

        if (endPoint.find(stagelink) != -1) and (get_stage() == 'beta'):
            endPoint = endPoint.replace("ifi/151613", "ifi/13")
        elif (endPoint.find(stagelink) != -1) and (get_stage() == 'LZ'):
            endPoint = endPoint.replace("ifi/151613", "ifi/1")
        response = requests.request(requestMethod, endPoint, headers=headers, params=params, json=jsonPayload)
        Utilities.response = response
        if IS_LOG_CURL:
            Utilities.log_curl_req(response)

        try:
            assert response.status_code == expectedStatusCode, \
                f"Expected Status Code {expectedStatusCode} and Actual status {response.status_code} code did not match with failure reason {response.json()}"
            return response
        except:
            logger.error(response.headers)
            pytest.fail(
                f"Expected Status Code {expectedStatusCode} and Actual status {response.status_code} code did not match and response is {response.json()}")

    @staticmethod
    def log_curl_req(response):
        logger.info("----------CURLIFY START----------------")
        logger.info("                                       ")
        logger.info("***********REQUEST CURL****************")
        logger.info("                                       ")
        logger.info(curlify.to_curl(response.request))
        logger.info("                                       ")
        logger.info("***********RESPONSE MESSAGE************")
        logger.info("                                       ")
        logger.info(f"Response :{response.text}")
        logger.info("                                       ")
        logger.info("***************************************")
        logger.info("***** Response Time is:" + str(response.elapsed.total_seconds()))
        logger.info("----------CURLIFY ENDS-----------------")
        logger.info("                                       ")
        logger.info(f"status code{response.status_code}")
