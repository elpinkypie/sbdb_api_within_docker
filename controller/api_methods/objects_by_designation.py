from controller.api_util.base_request import Base, BaseAssertion


class Objects(Base):
    def __init__(self, url):
        Base.__init__(self)
        self.url = url

    def get_object_by_designation(self, des, params=None):
        res = self.send_request(
            Base.RequestMethod.GET,
            custom_url=self.url + "?" + "des=" + str(
            des) + str(params)
        )
        return res

    def verify_payload_is_not_empty(self, res: Base.ResponseObject):
        return True if len(res.json) > 0 else False

