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
from newsmlg2.utils import Link, Category, EdNote


def render_item_class(dw_model: DigitalwiresModel) -> dict[str, str]:
    """Renders the item class.

    :param dw_model: A model of the digitalwires message.
    :return: A dictionary with the item class name.
    """
    return {
        "qcode": dw_model.get_item_class(),
    }


def render_pubstatus(
    dw_model: DigitalwiresModel,
    extract_pubstatus_qcode: Callable[[DigitalwiresModel], str],
    extract_pubstatus_name: Callable[[DigitalwiresModel], str],
) -> dict[str, str]:
    """Renders publication status information.

    :param dw_model: A model of the digitalwires message.
    :param extract_pubstatus_qcode: A function that extracts the publication status
        qcode from the model.
    :param extract_pubstatus_name: A function that extracts the publication status name
        from the model.
    :return: A dictionary containing the publication status qcode and name.
    """
    return {
        "qcode": extract_pubstatus_qcode(dw_model),
        "name": extract_pubstatus_name(dw_model),
    }


def render_services(
    dw_model: DigitalwiresModel,
    extract_services: list[Callable[[DigitalwiresModel], list[Category]]],
) -> list[dict[str, str]]:
    """Renders service-related information.

    :param dw_model: A model of the digitalwires message.
    :param extract_services: A list of functions that extract service details as tuples
        (qcode, name).
    :return: A list of dictionaries containing service information.
    """
    services = [s for extractor in extract_services for s in extractor(dw_model)]
    return [{"qcode": service.qcode, "name": service.name} for service in services]


def render_ednotes(
    dw_model: DigitalwiresModel,
    extractors: list[Callable[[DigitalwiresModel], list[EdNote]]],
) -> list[dict[str, str]]:
    """Renders editorial notes.

    :param dw_model: A model of the digitalwires message.
    :param extractors: A list of functions that extract editorial note details as tuples
        (role, text, is_public).
    :return: A list of dictionaries containing editorial notes. Non-public notes are
        marked with a constraint.
    """
    ednotes = [e for extractor in extractors for e in extractor(dw_model)]
    return [
        {
            "role": note.role,
            "text": note.ednote,
            "constraint": (
                "dpapconstraint:nonpublic" if not note.is_publishable else None
            ),
        }
        for note in ednotes
        if note.ednote
    ]


def render_signal(
    dw_model: DigitalwiresModel,
    extract_signal: Callable[[DigitalwiresModel], list[str]],
) -> list[str]:
    """Renders signal-related information.

    :param dw_model: A model of the digitalwires message.
    :param extract_signal: A function that extracts signal details as a list of strings.
    :return: A list of signal strings, or None if empty.
    """
    signals = [s for s in extract_signal(dw_model) if s is not None and len(s) > 0]
    return signals if len(signals) > 0 else None


def render_links(
    dw_model: DigitalwiresModel,
    extractors: list[Callable[[DigitalwiresModel], list[Link]]],
) -> list[dict[str, str]]:
    """Renders link information.

    :param dw_model: A model of the digitalwires message.
    :param extractors: A list of functions that extract link objects.
    :return: A list of dictionaries containing link information.
    """
    if not dw_model.is_text_message():
        return []
    links = [a for extractor in extractors for a in extractor(dw_model)]
    return [
        {
            "urn": link.urn,
            "rank": str(i + 1),
            "href": link.url,
            "rel": link.rel,
            "version": link.version,
            "title": link.title,
            "itemClass": _map_type_to_item_class(link.assoc_type),
        }
        for i, link in enumerate(sorted(links, key=lambda l: l.rank))
    ]


def render_notepad(
    dw_model: DigitalwiresModel,
    extract_header: Callable[[DigitalwiresModel], Union[str, None]],
    extract_public: Callable[[DigitalwiresModel], Union[str, None]],
    extract_non_public: Callable[[DigitalwiresModel], Union[str, None]],
    extract_closingline: Callable[[DigitalwiresModel], Union[str, None]],
) -> dict[str, str]:
    """Renders notepad-related information.

    :param dw_model: A model of the digitalwires message.
    :param extract_header: A function that extracts the header text.
    :param extract_public: A function that extracts the public note text.
    :param extract_non_public: A function that extracts the non-public note text.
    :param extract_closingline: A function that extracts the closing line text.
    :return: A dictionary containing notepad information, or None if both public and
        non-public notes are missing.
    """
    public = extract_public(dw_model)
    non_public = extract_non_public(dw_model)
    closingline = extract_closingline(dw_model)
    return (
        {
            "header": extract_header(dw_model),
            "public": public,
            "non_public": non_public,
            "closingline": closingline,
        }
        if public is not None or non_public is not None
        else None
    )


def _map_type_to_item_class(assoc_type: str) -> Union[str, None]:
    if assoc_type is None:
        return None
    classes = {"image": "ninat:picture", "text": "ninat:text"}
    return classes.get(assoc_type, f"ninat:{assoc_type}")
