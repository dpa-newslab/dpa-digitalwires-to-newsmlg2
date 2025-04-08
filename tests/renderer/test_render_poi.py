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

import pytest

from newsmlg2.renderer.render_poi import render_pois
from newsmlg2.utils.objects import POI


@pytest.fixture(scope="function")
def poi1():
    return POI(
        name="dpa Hamburg",
        city="Hamburg",
        country="Germany",
        formatted_address="Mittelweg 38, 20148 Hamburg",
        longitude="53.56965284324411",
        latitude="9.994512382326773",
    )


@pytest.fixture(scope="function")
def poi2():
    return POI(
        name="dpa Berlin",
        city="Berlin",
        country="Germany",
        formatted_address="Rudi-Dutschke-Straße 2, 10969 Berlin",
        longitude="52.507386350047476",
        latitude="13.39605153388193",
    )


def test_render_pois(poi1):
    result = render_pois(None, [lambda c: [poi1]])

    assert result is not None
    assert len(result) == 1
    assert validate_poi(result[0], poi1, 0)


def test_render_pois_return_multiple(poi1, poi2):
    result = render_pois(None, [lambda c: [poi1, poi2]])

    assert result is not None
    assert len(result) == 2
    assert validate_poi(result[0], poi1, 0)
    assert validate_poi(result[1], poi2, 1)


def test_render_pois_multiple_extractor(poi1, poi2):
    result = render_pois(None, [lambda c: [poi1], lambda c: [poi2]])

    assert result is not None
    assert len(result) == 2
    assert validate_poi(result[0], poi1, 0)
    assert validate_poi(result[1], poi2, 1)


def test_render_pois_empty():
    result = render_pois(None, [lambda c: []])

    assert result is not None
    assert len(result) == 0


def validate_poi(result, expected_poi, idx):
    if expected_poi is None:
        return False
    return (
        result["literal"] == f"poiID{idx}"
        and result["name"] == expected_poi.name
        and result["address"] == expected_poi.formatted_address
        and result["city"] == expected_poi.city
        and result["country"] == expected_poi.country
        and result["latitude"] == expected_poi.latitude
        and result["longitude"] == expected_poi.longitude
    )
