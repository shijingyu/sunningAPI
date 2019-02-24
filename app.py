from flask import Flask
from socket import *
app = Flask(__name__)

import suning.api


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/suning/swap', methods=['GET'])
def sn_swap():
    request = suning.api.CustompromotionurlQueryRequest()
    request.adBookId = "195296"
    request.visitUrl = "https://product.suning.com/0000000000/690105206.html"
    domain = "https://open.suning.com"
    appKey = "*"
    appSecret = "*"
    request.setDomainInfo(domain, "80")
    request.setAppInfo(appKey, appSecret)
    try:
        result = request.getResponse()
    return(result)
    except Exception as e:
    return(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


