#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2025  dpa-IT Services GmbH
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import logging

from newsmlg2 import convert_to_g2

logger = logging.getLogger()


def test_single_g2_converter(test_data_json, result_data_g2):
    filename = "image.json"
    result = convert_to_g2(test_data_json[filename], templates="./newsmlg2/templates")
    logger.info(result)
    assert result is not None
    assert result_data_g2[filename.replace(".json", ".xml")] == result


def test_g2_converter(test_data_json, result_data_g2):
    results = [
        (filename, convert_to_g2(file, templates="./newsmlg2/templates"))
        for filename, file in test_data_json.items()
    ]

    for result in results:
        compare = result_data_g2[result[0].replace(".json", ".xml")]
        assert result[1] is not None
        assert result[1].startswith(
            '<?xml version="1.0" encoding="UTF-8"?>\n<newsMessage xmlns="http://iptc.org/std/nar/2006-10-01/"'
        )
        assert compare == result[1]
