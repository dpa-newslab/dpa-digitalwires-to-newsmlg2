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

from newsmlg2.digitalwires_model import DigitalwiresModel
from newsmlg2.utils import Link


def get_associations(dw_model: DigitalwiresModel) -> list[Link]:
    """Returns all associations as a list of Link objects.These objects will be returned
    in order of ascending rank.

    :param dw_model: A model of the digitalwires message.
    :return: A list of Link objects.
    """
    return sorted(
        [
            Link(
                urn=a["urn"],
                rank=int(a["rank"]),
                version=a["version"],
                title=a["headline"],
                assoc_type=a["type"],
                rel="irel:seeAlso",
                height=rend["height"] if "height" in rend else None,
                width=rend["width"] if "width" in rend else None,
                bitrate=rend["audiobitrate"] if "audiobitrate" in rend else None,
                samplerate=(
                    rend["audiosamplerate"] if "audiosamplerate" in rend else None
                ),
                url=rend["url"],
                content_type=rend["mimetype"],
            )
            for a in dw_model.get("associations", [])
            for rend in a.get("renditions", [])
            if a["urn"] is not None
        ],
        key=lambda l: l.rank,
    )
