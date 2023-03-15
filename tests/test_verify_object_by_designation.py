"""Tests to verify response accordingly to changes for one parameter "des" in URL.
Other parameters like data will stay hardcoded. Positive and negative cases should be covered.
"""
from controller.api_methods.objects_by_designation import *
import pytest


class TestVerifyObjectByDesignation:

    des = ("des", [433, "141P", "2015%20AB"])
    params = ("params", ["&date-min=1900-01-01&date-max=2100-01-01&dist-max=0.2"])

    @pytest.mark.parametrize(*des)
    @pytest.mark.parametrize(*params)
    def test_get_object_by_des(self, setup_base_url, des, params):
        objects = Objects(setup_base_url)
        response = objects.get_object_by_designation(des=des, params=params)
        print(response)
        BaseAssertion.verify_general_response_code_200(response)
        assert objects.verify_payload_is_not_empty(response)
