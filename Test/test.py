from SDK import Application
import SDK as apiSDK

if __name__ == '__main__':
    wrapper = apiSDK.create_api_wrapper()
    app = Application(wrapper)
    print(app.findAppInfo(1))