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

from newsmlg2 import DigitalwiresModel
from newsmlg2.extractor import get_descriptions
from newsmlg2.utils.objects import Description

logger = logging.getLogger()


def test_scope_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw = file
        dw_model = DigitalwiresModel(dw)
        result = get_descriptions(dw_model)

        logger.info(result)
        assert result is not None
        for scope in result:
            assert type(scope) == Description
            assert len(scope.description) > 0
            assert scope.role.count(":") == 1
