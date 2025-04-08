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
from typing import Callable

from newsmlg2 import DigitalwiresModel
from newsmlg2.utils import POI


def render_pois(
    dw_model: DigitalwiresModel,
    extractors: list[Callable[[DigitalwiresModel], list[POI]]],
) -> list[dict[str, str]]:
    """Renders points of interest (POI) information.

    :param dw_model: A model of the digitalwires message.
    :param extractors: A list of functions that extract POI details from the context.
    :return: A list of dictionaries containing POI information, including name, address,
        city, country, longitude, and latitude. Each POI entry is assigned a unique
        identifier (`literal`) and ranked sequentially.
    """
    poi = [poi for extractor in extractors for poi in extractor(dw_model)]
    return [
        {
            "name": poi.name,
            "literal": f"poiID{i}",
            "rank": str(i + 1),
            "address": poi.formatted_address,
            "city": poi.city,
            "country": poi.country,
            "longitude": poi.longitude,
            "latitude": poi.latitude,
        }
        for i, poi in enumerate(poi)
    ]
