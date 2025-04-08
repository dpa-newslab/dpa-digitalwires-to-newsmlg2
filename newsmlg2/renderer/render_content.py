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
import re
import xml.etree.ElementTree as ETree
from typing import Callable, AnyStr, Union

from newsmlg2 import DigitalwiresModel
from newsmlg2.utils import Category, Link, element_to_string


def render_slugline(
    dw_model: DigitalwiresModel,
    extractors: list[Callable[[DigitalwiresModel], list[Category]]],
) -> list[dict[str, str]]:
    """Renders subjects into a dictionary for the slugline.

    :param dw_model: A model of the digitalwires message.
    :param extractors: An extractor function, which takes a context object and returns a
        tuple with the following elements: [type_qcode, name, qcode, rank]
    :return: A list of dictionary for the slugline.
    """

    def map_kind(type_qcode: str) -> str:
        if "dnltype:dpasubject" == type_qcode:
            return "subject"
        elif "dnltype:geosubject" == type_qcode:
            return "geo"
        elif "dnltype:keyword" == type_qcode:
            return "keyword"
        else:
            return type_qcode

    subjects = [subject for extractor in extractors for subject in extractor(dw_model)]
    return [
        {
            "kind": map_kind(subject.category_type),
            "name": subject.name,
            "qcode": subject.qcode,
        }
        for subject in subjects
        if subject.category_type is not None and subject.name is not None
    ]


def render_infobox(
    dw_model: DigitalwiresModel, extractor: Callable[[DigitalwiresModel], str]
) -> Union[str, None]:
    """Renders the infobox by surounding it with `<div class="infobox">`.

    :param dw_model: A model of the digitalwires message.
    :param extractor: An extractor function, which takes a context object and returnshe
        infobox as a string.
    :return: The infobox html as a string or None if there is no infobox.
    """
    infobox = extractor(dw_model)
    if infobox is None:
        return None

    section = ETree.fromstring(infobox)

    div = ETree.Element("div", attrib={"class": "INFOBOX"})
    for child in section:
        div.append(child)

    return element_to_string(div)


def render_article(
    dw_model: DigitalwiresModel,
    extract_dateline: Callable[[DigitalwiresModel], str],
    extract_article: Callable[[DigitalwiresModel], str],
) -> Union[list[str], None]:
    """Renders the main section of a newsmlg2 article.

    :param dw_model: A model of the digitalwires message.
    :param extract_dateline: An extractor function, which takes a context object and
        returns the dateline as a string.
    :param extract_article: An extractor function, which takes a context object and
        returns the article as a string.
    :return: A list of the child elements from the article as strings or None if there
        is no article. If there is a dateline from `extract_dateline` and there is no
        dateline in the article, the dateline is inserted into the first element of the
        list.
    """
    article = extract_article(dw_model)
    dateline = extract_dateline(dw_model)
    if article is None:
        return None

    section = ETree.fromstring(article)

    if dateline is not None and _has_no_dateline(section):
        insert_dateline(dateline, section)
    return [element_to_string(p) for p in section]


def insert_dateline(dateline, section):
    if len(section) <= 0:
        return

    dateline_ele = ETree.Element("span", attrib={"class": "dateline"})
    parts = _extract_parts(dateline)
    if parts is None:
        return

    dateline_ele.text, credit = parts
    credit_elem = ETree.Element("span", attrib={"class": "credit"})
    credit_elem.text = credit
    credit_elem.tail = " - "
    dateline_ele.append(credit_elem)
    dateline_ele.tail = section[0].text
    new_p = ETree.Element("p")
    new_p.append(dateline_ele)
    section[0] = new_p


def render_remote_content(
    dw_model: DigitalwiresModel,
    extractors: list[Callable[[DigitalwiresModel], list[Link]]],
) -> list[dict[str, str]]:
    """Renders the association as a dict for the remote content.

    :param dw_model: A model of the digitalwires message.
    :param extractors: An extractor function, which takes a context object and returns a
        list of Link objects.
    :return: A list of dictionaries for link elements.
    """
    links = [a for extractor in extractors for a in extractor(dw_model)]
    return [
        {
            "href": link.url,
            "contenttype": link.content_type,
            "width": link.width,
            "height": link.height,
            "samplerate": link.samplerate,
            "bitrate": link.bitrate,
        }
        for link in links
    ]


def _has_no_dateline(section):
    return section.find(".//span[@class = 'dateline']") is None


def _extract_parts(dateline: str) -> Union[tuple[AnyStr, AnyStr], None]:
    regex = re.compile(
        r"^(?P<located>.+)(?P<credit>\(.+\))\s*[-\u2010\u2011\u2012\u2013\u2014\u2015\uFE58\uFE63\uFF0D]\s*"
    )
    parsed_dateline = re.match(regex, dateline)
    if parsed_dateline is None:
        return None
    return parsed_dateline.group("located"), parsed_dateline.group("credit")
