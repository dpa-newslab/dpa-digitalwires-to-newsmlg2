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
import xml.etree.ElementTree as ETree

from newsmlg2 import DigitalwiresModel
from newsmlg2.utils import Link


def get_version_created(dw_model: DigitalwiresModel) -> str:
    """Returns the version created.

    :param dw_model: A model of the digitalwires message.
    :return: The version created as a string.
    """
    return dw_model.get("version_created", "")


def get_content_created(dw_model: DigitalwiresModel) -> str:
    """Returns the content created.

    :param dw_model: A model of the digitalwires message.
    :return: The content created as a string.
    """
    return dw_model.get("content_created", "")


def get_version(dw_model: DigitalwiresModel) -> str:
    """Returns the version.

    :param dw_model: A model of the digitalwires message.
    :return: The version as a string. Default: "1"
    """
    return dw_model.get("version", "1")


def get_dateline(dw_model: DigitalwiresModel) -> str:
    """Returns the dateline.

    :param dw_model: A model of the digitalwires message.
    :return: The dateline as a string.
    """
    return dw_model.get("dateline")


def get_creditline(dw_model: DigitalwiresModel) -> str:
    """Returns the creditline.

    :param dw_model: A model of the digitalwires message.
    :return: The creditline as a string.
    """
    return dw_model.get("creditline")


def get_urgency(dw_model: DigitalwiresModel) -> int:
    """Returns the urgency if there is one, otherwise ``3``.

    :param dw_model: A model of the digitalwires message.
    :return: The urgency as an Integer, ``3`` if there is no urgency.
    """
    return dw_model.get("urgency", 3)


def get_embargo(dw_model: DigitalwiresModel) -> str:
    """Returns the embargo date.

    :param dw_model: A model of the digitalwires message.
    :return: The embargo date as a string.
    """
    return dw_model.get("embargoed", None)


def get_byline(dw_model: DigitalwiresModel) -> str:
    """Returns the byline.

    :param dw_model: A model of the digitalwires message.
    :return: The byline as a string. Never ``None``.
    """
    byline = dw_model.get("byline", "")
    return byline if byline else ""


def get_urn(dw_model: DigitalwiresModel) -> str:
    """Returns the urn.

    :param dw_model: A model of the digitalwires message.
    :return: The urn as a string.
    """
    return dw_model.get("urn", "")


def get_copyright_notice(dw_model: DigitalwiresModel) -> str:
    """Returns the copyright notice.

    :param dw_model: A model of the digitalwires message.
    :return: The copyright notice as a string. Never ``None``.
    """
    notice = dw_model.get("copyrightnotice", "")
    return notice if notice else ""


def get_usageterms(dw_model: DigitalwiresModel) -> str:
    """Returns the usageterms.

    :param dw_model: A model of the digitalwires message.
    :return: The usageterms as a string.
    """
    return dw_model.get("usageterms")


def get_language(dw_model: DigitalwiresModel) -> str:
    """Returns the language.

    :param dw_model: A model of the digitalwires message.
    :return: The language as a string.
    """
    return dw_model.get("language")


def get_infobox(dw_model: DigitalwiresModel) -> str:
    """Returns the info box.

    :param dw_model: A model of the digitalwires message.
    :return: The info box as html string.
    """
    return dw_model.get("infobox_html")


def get_linkbox(dw_model: DigitalwiresModel) -> list[Link]:
    """Returns the links from the linkbox.

    :param dw_model: A model of the digitalwires message.
    :return: A list of link from the linkbox. Never ``None``.
    """
    linkbox = dw_model.get("linkbox_html")
    if not linkbox:
        return []
    section = ETree.fromstring(linkbox)

    links = sorted(
        [
            Link(
                url=a.attrib.get("href", ""),
                title=a.text,
                rel="irel:seeAlso",
                rank=i + 1,
            )
            for i, a in enumerate(section.findall("./ul/li/a"))
        ],
        key=lambda l: l.rank,
    )
    return links if links else []
