# -*- coding:utf8 -*-
# !/usr/bin/env python
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
from future.standard_library import install_aliases

install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/', methods=['POST, GET'])
def index():
    return "Forbidden"


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def make_sizing(reqParam, dmz):
    # Initial data
    model = None
    datasheet_link = None
    #
    # fill data from request
    inetSpeed = reqParam.get("inet_speed")
    users = reqParam.get("users")
    #
    print(reqParam)
    return "Думаю тебе отлично подойдет вот эта модель - " + model + " смотри какая штука  - " + datasheet_link + " \n Но стоит уточнить у @russia"



def processRequest(req):
    if req.get("result").get("action") == "yahooWeatherForecast":
        return {}
    ##
    # baseurl = "https://query.yahooapis.com/v1/public/yql?"
    result = None
    reqParam = req.get("result").get("parameters")
    if req.get("result").get("action") == "dmz-sizing":
        speech = make_sizing(reqParam, False)
    elif req.get("result").get("action") == "nondmz-sizing":
        speech = make_sizing(reqParam, True)

    else:
        return {}
    res = speech
    return res





if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
