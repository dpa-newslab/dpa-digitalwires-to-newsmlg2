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

from newsmlg2 import DigitalwiresModel
from newsmlg2.utils import POI, Category, get_none_safe


def get_services(dw_model: DigitalwiresModel) -> list[Category]:
    """Returns all services from the categories given by ``"type": "dnltype:wire"``.

    :param dw_model: A model of the digitalwires message.
    :return: A list of category objects containing service qcodes and names from the
        categories.
    """
    return dw_model.category_items(cat_type="dnltype:wire", attrs=["qcode", "name"])


def get_dpa_subjects(dw_model: DigitalwiresModel) -> list[Category]:
    """Returns all dpa_subjects from the categories given by ``"type":
    "dnltype:dpasubject"``.

    :param dw_model: A model of the digitalwires message.
    :return: A list of category objects containing subjects from the categories.
    """
    return dw_model.category_items(
        cat_type="dnltype:dpasubject", attrs=["type", "name", "qcode", "rank"]
    )


def get_geo_subject(dw_model: DigitalwiresModel) -> list[Category]:
    """Returns all geo subjects from the categories given by ``"type":
    "dnltype:geosubject"``.

    :param dw_model: A model of the digitalwires message.
    :return: A list of category objects containing geo subject from the categories.
    """
    return dw_model.category_items(
        cat_type="dnltype:geosubject", attrs=["type", "name", "qcode", "rank"]
    )


def get_desk(dw_model: DigitalwiresModel) -> list[Category]:
    """Returns the desk categorie from the categories given by ``"type":
    "dnltype:desk"``.

    :param dw_model: A context object of the digitalwires message.
    :return: A list with the desk from the categories.
    """
    return dw_model.category_items(
        cat_type="dnltype:desk", attrs=["type", "name", "qcode"]
    )


def get_scope(dw_model: DigitalwiresModel) -> list[Category]:
    """Returns all scopes from the categories given by ``"type": "dnltype:scope"``.

    :param dw_model: A model of the digitalwires message.
    :return: A list of category objects containing the scope from the categories.
    """
    return dw_model.category_items(cat_type="dnltype:scope", attrs=["name", "qcode"])


def get_pubstatus_qcode(dw_model: DigitalwiresModel) -> str:
    """Returns the pustatus qcode from the categories given by ``"type":
    "dnltype:pubstatus"``.

    :param dw_model: A model of the digitalwires message.
    :return: The pubstatus qcode as a string. If there are more than one, only the first
        result is returned.
    """
    return next(
        iter(
            [
                cat.qcode
                for cat in dw_model.category_items(
                    cat_type="dnltype:pubstatus", attrs=["qcode"]
                )
            ]
        ),
        "",
    )


def get_pubstatus_name(dw_model: DigitalwiresModel) -> str:
    """Returns the pustatus name from the categories given by ``"type":
    "dnltype:pubstatus"``.

    :param dw_model: A model of the digitalwires message.
    :return: The pubstatus name as a string. If there are more than one, only the first
        result is returned.
    """
    return next(
        iter(
            cat.name
            for cat in dw_model.category_items(
                cat_type="dnltype:pubstatus", attrs=["name"]
            )
        ),
        "",
    )


def get_provider_qcode(dw_model: DigitalwiresModel) -> str:
    """Returns the provider qcode from the categories given by ``"type":
    "dnltype:provider"``.

    :param dw_model: A model of the digitalwires message.
    :return: The provider qcode as a string. If there are more than one, only the first
        result is returned.
    """
    return next(
        iter(
            cat.qcode
            for cat in dw_model.category_items(
                cat_type="dnltype:provider", attrs=["qcode"]
            )
        ),
        "",
    )


def get_provider_name(dw_model: DigitalwiresModel) -> str:
    """Returns the provider name from the categories given by ``"type":
    "dnltype:provider"``.

    :param dw_model: A model of the digitalwires message.
    :return: The provider name as a string. If there are more than one, only the first
        result is returned.
    """
    return next(
        iter(
            [
                cat.name
                for cat in dw_model.category_items(
                    cat_type="dnltype:provider", attrs=["name"]
                )
            ]
        ),
        "",
    )


def get_signal_qcodes(dw_model: DigitalwiresModel) -> list[str]:
    """Returns all signal qcodes from the categories given by ``"type":
    "dnltype:signal"``.

    :param dw_model: A context object of the digitalwires message.
    :return: A list of signal qcodes as strings.
    """
    return [
        cat.qcode
        for cat in dw_model.category_items(cat_type="dnltype:signal", attrs=["qcode"])
    ]


def get_located(dw_model: DigitalwiresModel) -> list[Category]:
    """Returns all located from the categories given by ``"type": "dnltype:located"``.

    :param dw_model: A model of the digitalwires message.
    :return: A list of category objects containing located infos from the categories.
    """
    return dw_model.category_items(cat_type="dnltype:located", attrs=["name", "qcode"])


def get_infosource(dw_model: DigitalwiresModel) -> list[Category]:
    """Returns all info sources from the categories given by ``"type":
    "dnltype:infosource"``.

    :param dw_model: A model of the digitalwires message.
    :return: A list of category objects containing info sources from the categories.
    """
    return dw_model.category_items(
        cat_type="dnltype:infosource", attrs=["name", "qcode", "role"]
    )


def get_creator(dw_model: DigitalwiresModel) -> list[Category]:
    """Returns all creators from the categories given by ``"type": "dnltype:creator"``.

    :param dw_model: A model of the digitalwires message.
    :return: A list of category objects containing creator info from the categories.
    """
    return dw_model.category_items(
        cat_type="dnltype:creator", attrs=["name", "qcode", "role"]
    )


def get_contributor(dw_model: DigitalwiresModel) -> list[Category]:
    """Returns all contributors from the categories given by ``"type":
    "dnltype:contributor"``.

    :param dw_model: A model of the digitalwires message.
    :return: A list of category objects containing contributors info from the
        categories.
    """
    return dw_model.category_items(
        cat_type="dnltype:contributor", attrs=["name", "qcode", "role"]
    )


def get_genre(dw_model: DigitalwiresModel) -> Category:
    """Returns all genre from the categories given by ``"type": "dnltype:genre"``.

    :param dw_model: A model of the digitalwires message.
    :return: A category object containing genre names and qcodes from the categories.
    """
    return next(
        iter(
            dw_model.category_items(cat_type="dnltype:genre", attrs=["name", "qcode"])
        ),
        None,
    )


def get_keywords(dw_model: DigitalwiresModel) -> list[Category]:
    """Returns all keywords from the categories given by ``"type": "dnltype:keyword"``.

    :param dw_model: A model of the digitalwires message.
    :return: A list of category objects containing keywords from the categories.
    """
    return dw_model.category_items(
        cat_type="dnltype:keyword", attrs=["type", "name", "qcode", "rank"]
    )


def get_poi(dw_model: DigitalwiresModel) -> list[POI]:
    """Returns all POIs from the categories given by ``"type": "dnltype:poi"``.

    :param dw_model: A model of the digitalwires message.
    :return: A list of POIs from the categories.
    """
    return [
        POI(
            name=cat.get("geojson", {}).get("properties", {}).get("name"),
            formatted_address=cat.get("geojson", {})
            .get("properties", {})
            .get("formatted_address"),
            city=cat.get("geojson", {}).get("properties", {}).get("locality"),
            country=cat.get("geojson", {}).get("properties", {}).get("country"),
            longitude=cat.get("geojson", {})
            .get("geometry", {})
            .get("coordinates", [None, None])[0],
            latitude=cat.get("geojson", {})
            .get("geometry", {})
            .get("coordinates", [None, None])[1],
        )
        for cat in get_none_safe(dw_model, "categories", [])
        if cat.get("type", "") == "dnltype:poi"
    ]
