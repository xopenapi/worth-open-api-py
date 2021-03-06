# coding: utf-8

"""
    设备开放API

    worth open api  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import worth
from worth.models.gen_token_response import GenTokenResponse  # noqa: E501
from worth.rest import ApiException

class TestGenTokenResponse(unittest.TestCase):
    """GenTokenResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GenTokenResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = worth.models.gen_token_response.GenTokenResponse()  # noqa: E501
        if include_optional :
            return GenTokenResponse(
                message = '0', 
                code = '0', 
                data = None
            )
        else :
            return GenTokenResponse(
        )

    def testGenTokenResponse(self):
        """Test GenTokenResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
