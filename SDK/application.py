from SDK import is_offline
import SDK as apiSDK

class Application(object):
    def __init__(self, wrapper):
        self.api_wrapper = wrapper

    def findAppInfo(self,id = 0):
        if is_offline():
            apiSDK.throw_error("Cannot check balance in offline mode.", NetworkException)
            return 0
        try:
            resp = self.api_wrapper.request('/manager/app/findAppInfo?id=%s' % id)
            return resp['data']
        except Exception as ex:
            msg = "Failed to get balance. ({})".format(ex)
            return 0
