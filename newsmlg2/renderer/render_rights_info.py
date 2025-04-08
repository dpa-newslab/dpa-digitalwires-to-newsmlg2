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


def render_copyright_notice(
    dw_model: DigitalwiresModel, extractor: Callable[[DigitalwiresModel], str]
) -> str:
    """Renders copyright notice.

    :param dw_model: A model of the digitalwires message.
    :param extractor: A function that extracts the copyright notice.
    :return: The rendered copyright notice.
    """
    return extractor(dw_model)


def render_usageterms(
    dw_model: DigitalwiresModel, extractors: list[Callable[[DigitalwiresModel], str]]
) -> list[str]:
    """Renders usage terms.

    :param dw_model: A model of the digitalwires message.
    :param extractors: A list of functions that extract the usage terms.
    :return: A list of rendered usage terms.
    """
    return [extractor(dw_model) for extractor in extractors]
