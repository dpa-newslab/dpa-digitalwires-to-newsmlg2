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


def render_version(
    dw_model: DigitalwiresModel, extractor: Callable[[DigitalwiresModel], str]
) -> int:
    """Renders the version.

    :param dw_model: A model of the digitalwires message.
    :param extractor: A function that extracts the version from the message.
    :return: The version as an int.
    """
    return int(extractor(dw_model))


def render_provider(
    dw_model: DigitalwiresModel,
    extract_qcode: Callable[[DigitalwiresModel], str],
    extract_name: Callable[[DigitalwiresModel], str],
) -> dict[str, str]:
    """Renders provider-related information.

    :param dw_model: A model of the digitalwires message.
    :param extract_qcode: A function that extracts the provider qcode.
    :param extract_name: A function that extracts the provider name.
    :return: A dictionary containing provider information with 'qcode' and 'name' keys.
    """
    return {
        "qcode": extract_qcode(dw_model),
        "name": extract_name(dw_model),
    }
