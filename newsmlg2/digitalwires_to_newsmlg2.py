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
import arrow
from jinja2 import Environment, FileSystemLoader

from newsmlg2 import DigitalwiresModel
from newsmlg2.builder.to_g2_converter import DwToG2Converter


def datetime_format(value, format="%H:%M %d-%m-%y"):
    return arrow.get(value).strftime(format)


def convert_to_g2(
    digitalwires: dict, templates: str = "./newsmlg2/templates", jinja_args: dict = None
) -> str:
    """This function takes the dict representation of a digitalwires message and creates
    a newmlg2 message.

    For more details on how a newsmlg2 message is structured, have a look here
    https://www.iptc.org/std/NewsML-G2/2.32/specification/NewsML-G2-2.32-specification.html
    :param digitalwires: The parsed json representation of a digitalwires message.
    :param templates: A path to a jinja templates folder conatining a file called
        `g2_tamplate.j2`.
    :param jinja_args: Optional arguments to pass to jinja2.Environment.
    :return: a list of newsmlg2 messages for each service
    """
    dw_model = DigitalwiresModel(digitalwires)
    if jinja_args is None:
        jinja_args = {
            "lstrip_blocks": True,
            "trim_blocks": True,
            "keep_trailing_newline": False,
            "autoescape": True,
        }
    env = Environment(
        loader=FileSystemLoader(templates),
        **jinja_args,
    )
    env.filters["datetimeformat"] = datetime_format

    entry = DwToG2Converter().convert(dw_model)
    g2 = env.get_template("g2_template.j2").render(**entry)
    return g2
