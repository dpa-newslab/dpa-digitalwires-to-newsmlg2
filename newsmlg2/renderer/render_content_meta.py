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
from typing import Callable, Union

from newsmlg2 import DigitalwiresModel
from newsmlg2.utils import Category
from newsmlg2.utils.objects import Description


def render_content_created(
    dw_model: DigitalwiresModel, extractors: list[Callable[[DigitalwiresModel], str]]
) -> str:
    """Renders the content creation timestamp.

    :param dw_model: A model of the digitalwires message.
    :param extractors: A list of functions that extract parts of the timestamp from the
        context. These parts are concatenated into a single string. Functions returning
        `None` are ignored.
    :return: A string containing the rendered timestamp if at least one extracted part
        is non-empty, otherwise `None`.
    """
    creates = [extraction(dw_model) for extraction in extractors]
    creates = [create for create in creates if create is not None]
    return "".join(creates) if len(creates) > 0 else None


def render_located(
    dw_model: DigitalwiresModel,
    extractors: list[Callable[[DigitalwiresModel], list[Category]]],
) -> list[dict[str, str]]:
    """Renders location-related information.

    :param dw_model: A model of the digitalwires message.
    :param extractors: A list of functions that extract location details as tuples
        (name, qcode).
    :return: A list of dictionaries containing location information with 'name' and
        'qcode' keys.
    """
    locates = [locate for cat in extractors for locate in cat(dw_model)]
    return [{"name": locate.name, "qcode": locate.qcode} for locate in locates]


def render_infosource(
    dw_model: DigitalwiresModel,
    extractors: list[Callable[[DigitalwiresModel], list[Category]]],
) -> list[dict[str, str]]:
    """Renders information about the content source.

    :param dw_model: A model of the digitalwires message.
    :param extractors: A list of functions that extract source details as tuples (name,
        qcode, role).
    :return: A list of dictionaries containing source information. Entries with both
        'name' and 'qcode' as `None` are ignored.
    """
    infosources = [infosource for cat in extractors for infosource in cat(dw_model)]
    return [
        {"name": infosource.name, "qcode": infosource.qcode, "role": infosource.role}
        for infosource in infosources
        if infosource.name is not None or infosource.qcode is not None
    ]


def render_creator(
    dw_model: DigitalwiresModel,
    extractors: list[Callable[[DigitalwiresModel], list[Category]]],
) -> list[dict[str, str]]:
    """Renders information about the creator of the content.

    :param dw_model: A model of the digitalwires message.
    :param extractors: A list of functions that extract creator details as tuples (name,
        qcode, role).
    :return: A list of dictionaries containing creator information. Entries with both
        'name' and 'qcode' as `None` are ignored.
    """
    creators = [creator for cat in extractors for creator in cat(dw_model)]
    return [
        {"name": creator.name, "qcode": creator.qcode, "role": creator.role}
        for creator in creators
        if creator.name is not None or creator.qcode is not None
    ]


def render_contributor(
    dw_model: DigitalwiresModel,
    extractors: list[Callable[[DigitalwiresModel], list[Category]]],
) -> list[dict[str, str]]:
    """Renders information about contributors.

    :param dw_model: A model of the digitalwires message.
    :param extractors: A list of functions that extract contributor details as tuples
        (name, qcode, role).
    :return: A list of dictionaries containing contributor information. Entries with
        both 'name' and 'qcode' as `None` are ignored.
    """
    contributors = [contributor for cat in extractors for contributor in cat(dw_model)]
    return [
        {"name": creator.name, "qcode": creator.qcode, "role": creator.role}
        for creator in contributors
        if creator.name is not None or creator.qcode is not None
    ]


def render_genre(
    dw_model: DigitalwiresModel, extractor: Callable[[DigitalwiresModel], Category]
) -> dict[str, str]:
    """Renders genre information.

    :param dw_model: A model of the digitalwires message.
    :param extractor: A function that extracts genre details as a tuple (name, qcode).
    :return: A dictionary containing genre information.
    """
    genre = extractor(dw_model)
    return {"name": genre.name, "qcode": genre.qcode} if genre is not None else None


def render_subjects(
    dw_model: DigitalwiresModel,
    extractors: list[Callable[[DigitalwiresModel], list[Category]]],
) -> list[dict[str, str]]:
    """Renders subject-related information.

    :param dw_model: A model of the digitalwires message.
    :param extractors: A list of functions that extract subject details as tuples
        (type_qcode, name, qcode, rank).
    :return: A list of dictionaries containing subject information. Entries with a
        `None` type_qcode and both 'name' and 'qcode' as `None` are ignored.
    """
    subjects = [subject for extractor in extractors for subject in extractor(dw_model)]
    return [
        {
            "type": _map_subj_type(subject.category_type),
            "name": subject.name,
            "qcode": subject.qcode,
            "rank": str(subject.rank) if subject.rank else None,
        }
        for subject in subjects
        if subject.category_type is not None
        and (subject.qcode is not None or subject.name is not None)
    ]


def render_audience(
    dw_model: DigitalwiresModel,
    extractors: list[Callable[[DigitalwiresModel], list[Category]]],
) -> list[dict[str, str]]:
    """Renders audience-related information.

    :param dw_model: A model of the digitalwires message.
    :param extractors: A list of functions that extract audience details as tuples
        (name, qcode).
    :return: A list of dictionaries containing audience information. Entries with both
        'name' and 'qcode' as `None` are ignored.
    """
    audiences = [
        audience for extractor in extractors for audience in extractor(dw_model)
    ]
    return [
        {
            "name": audience.name,
            "qcode": audience.qcode,
        }
        for audience in audiences
        if audience.name is not None and audience.qcode is not None
    ]


def render_keywords(
    dw_model: DigitalwiresModel,
    extractors: list[Callable[[DigitalwiresModel], list[Category]]],
) -> list[dict[str, str]]:
    """Renders keyword-related information.

    :param dw_model: A model of the digitalwires message.
    :param extractors: A list of functions that extract keyword details as tuples (type,
        name, None, rank).
    :return: A list of dictionaries containing keyword information. Entries where 'name'
        is `None` are ignored.
    """
    keywords = [keyword for extractor in extractors for keyword in extractor(dw_model)]
    return [
        {
            "name": keyword.name,
            "rank": str(keyword.rank) if keyword.rank else None,
        }
        for keyword in keywords
    ]


def render_descriptions(
    dw_model: DigitalwiresModel,
    extractors: list[Callable[[DigitalwiresModel], list[Description]]],
) -> list[dict[str, str]]:
    """Renders description information.

    :param dw_model: A model of the digitalwires message.
    :param extractors: A list of function that extracts description details as a
        Description object.
    :return: A dictionary containing description information.
    """
    descriptions = [desc for extractor in extractors for desc in extractor(dw_model)]
    return [{"role": descr.role, "value": descr.description} for descr in descriptions]


def _map_subj_type(subj_type: str) -> Union[str, None]:
    if subj_type is None:
        return None
    classes = {
        "dnltype:dpasubject": "dpatype:dpasubject",
        "dnltype:geosubject": "cpnat:geoArea",
        "dnltype:desk": "dpatype:category",
    }
    return classes.get(subj_type, subj_type)
