#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2025 dpa-IT Services GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import re

import arrow

from newsmlg2 import DigitalwiresModel
from newsmlg2.extractor.meta_extractor import (
    get_dateline,
    get_version_created,
    get_content_created,
    get_urgency,
    get_embargo,
    get_byline,
    get_version,
    get_creditline,
    get_linkbox,
)

logger = logging.getLogger()


def test_version_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw_model = DigitalwiresModel(file)
        result = get_version(dw_model)

        logger.info(result)
        assert result is not None
        assert int(result) > 0


def test_dateline_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw_model = DigitalwiresModel(file)
        result = get_dateline(dw_model)

        logger.info(result)
        assert (
            re.search(r".+\s\(.+\)\s+-\s*", result) is not None
            if result is not None
            else True
        )


def test_creditline_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw_model = DigitalwiresModel(file)
        result = get_creditline(dw_model)

        logger.info(result)
        # No exception means it passed


def test_version_created_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw_model = DigitalwiresModel(file)
        result = get_version_created(dw_model)

        logger.info(result)
        assert len(result) > 0
        assert arrow.get(result) is not None


def test_content_created_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw_model = DigitalwiresModel(file)
        result = get_content_created(dw_model)

        logger.info(result)
        assert arrow.get(result) is not None if result is not None else True


def test_urgency_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw_model = DigitalwiresModel(file)
        result = get_urgency(dw_model)

        logger.info(result)
        assert result > 0


def test_embargo_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw_model = DigitalwiresModel(file)
        result = get_embargo(dw_model)

        logger.info(result)
        assert result is None or len(result) > 0
        assert arrow.get(result) is not None if result is not None else True


def test_byline_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw_model = DigitalwiresModel(file)
        result = get_byline(dw_model)

        logger.info(result)
        assert len(result) >= 0


def test_linkbox_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw_model = DigitalwiresModel(file)
        result = get_linkbox(dw_model)

        assert result is not None
        if len(result) > 0:
            logger.info([str(link) for link in result])
            assert [len(link.url) > 0 for link in result]
            assert [len(link.title) > 0 for link in result]
            assert [link.rel == "isrel:seeAlso" for link in result]
            assert [link.rank > 0 for link in result]
