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

from newsmlg2 import DigitalwiresModel
from newsmlg2.utils.objects import Description


def get_descriptions(dw_model: DigitalwiresModel) -> list[Description]:
    """Returns the descriptions with its role.

    :param dw_model: A model of the digitalwires message.
    :return: A list of Description objects with role and description.
    """
    attrs = ["role", "description"]
    return [
        Description(**dict(zip(attrs, descr)))
        for descr in dw_model.get_sorted_list(attrs, "descriptions", None)
    ]
