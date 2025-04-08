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

from newsmlg2 import DigitalwiresModel
from newsmlg2.extractor.category_extractor import (
    get_dpa_subjects,
    get_geo_subject,
    get_genre,
    get_services,
    get_signal_qcodes,
    get_scope,
    get_desk,
    get_keywords,
)
from newsmlg2.utils.objects import Category

logger = logging.getLogger()


def test_desk_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw = file
        dw_model = DigitalwiresModel(dw)
        result = get_desk(dw_model)

        logger.info(result)
        assert result is not None
        assert len(result) == 1
        for desk in result:
            assert type(desk) is Category
            assert desk.category_type == "dnltype:desk"
            assert desk.qcode is not None or desk.name is not None
            assert desk.qcode.count(":") > 0  # qcode
            assert desk.qcode.startswith("dpacat:")
            assert desk.rank is None


def test_dpa_subject_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw = file
        dw_model = DigitalwiresModel(dw)
        result = get_dpa_subjects(dw_model)

        logger.info(result)
        assert result is not None
        for subject in result:
            assert type(subject) is Category
            assert subject.qcode is not None or subject.name is not None
            assert subject.category_type.count(":") > 0
            assert subject.category_type == "dnltype:dpasubject"
            assert subject.qcode.count(":") > 0


def test_geo_subject_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw = file
        dw_model = DigitalwiresModel(dw)
        result = get_geo_subject(dw_model)

        logger.info(result)
        assert result is not None
        for subject in result:
            assert type(subject) is Category
            assert subject.qcode is not None or subject.name is not None
            assert subject.category_type.count(":") > 0
            assert subject.category_type == "dnltype:geosubject"
            assert subject.qcode.count(":") > 0


def test_dpa_and_geo_subject_extractor_are_disjoint(test_data_json):
    for filename, file in test_data_json.items():
        dw = file
        dw_model = DigitalwiresModel(dw)
        result = get_geo_subject(dw_model)

        logger.info(result)
        assert result is not None
        assert set(result).isdisjoint(get_dpa_subjects(dw_model))


def test_service_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw = file
        dw_model = DigitalwiresModel(dw)
        result = get_services(dw_model)

        logger.info(result)
        assert len(result) > 0
        for service in result:
            assert type(service) == Category
            assert service.qcode.startswith(("dpasrv:", "dnlsrv:"))


def test_signal_qcode_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw = file
        dw_model = DigitalwiresModel(dw)
        result = get_signal_qcodes(dw_model)

        logger.info(result)
        assert result[0].count(":") == 1 if len(result) > 0 else True


def test_genre_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw = file
        dw_model = DigitalwiresModel(dw)
        result = get_genre(dw_model)

        logger.info(result)
        if result is not None:
            assert type(result) == Category
            assert len(result.name) > 0
            assert result.qcode.count(":") == 1


def test_scope_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw = file
        dw_model = DigitalwiresModel(dw)
        result = get_scope(dw_model)

        logger.info(result)
        assert result is not None
        for scope in result:
            assert type(scope) == Category
            assert len(scope.name) > 0
            assert scope.qcode.count(":") == 1


def test_keywords_extractor(test_data_json):
    for filename, file in test_data_json.items():
        dw = file
        dw_model = DigitalwiresModel(dw)
        result = get_keywords(dw_model)

        logger.info(result)
        assert result is not None
        last_rank = 0
        for keyword in result:
            assert type(keyword) == Category
            assert len(keyword.category_type) > 0
            assert len(keyword.name) > 0
            assert keyword.qcode is None
            if keyword.rank is not None:
                assert int(keyword.rank) > 0
                assert last_rank < int(keyword.rank)
                last_rank = int(keyword.rank)
