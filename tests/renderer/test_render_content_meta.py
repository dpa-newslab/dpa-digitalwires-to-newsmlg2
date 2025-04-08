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
from newsmlg2.renderer import render_descriptions
from newsmlg2.renderer.render_content_meta import (
    render_content_created,
    render_located,
    render_genre,
    render_subjects,
    render_audience,
    render_keywords,
)
from newsmlg2.utils.objects import Category, Description


def test_render_content_created():
    result = render_content_created(None, [lambda c: "2024-11-21"])
    assert result is not None
    assert result == "2024-11-21"


def test_render_content_created_none():
    result = render_content_created(None, [lambda c: None])
    assert result is None


def test_render_content_created_parts():
    result = render_content_created(
        None, [lambda c: "2024-11-21", lambda c: "T", lambda c: "15:35:06+01:00"]
    )
    assert result is not None
    assert result == "2024-11-21T15:35:06+01:00"


def test_render_located():
    result = render_located(
        None, [lambda c: [Category(name="Hamburg", qcode="dpaarea:6")]]
    )
    assert result is not None
    assert len(result) == 1
    assert result[0]["name"] == "Hamburg"
    assert result[0]["qcode"] == "dpaarea:6"


def test_render_located_multiple():
    result = render_located(
        None,
        [
            lambda c: [
                Category(name="Hamburg", qcode="dpaarea:6"),
                Category(name="Berlin", qcode="dpaarea:3"),
            ]
        ],
    )
    assert result is not None
    assert len(result) == 2
    assert result[0]["name"] == "Hamburg"
    assert result[0]["qcode"] == "dpaarea:6"
    assert result[1]["name"] == "Berlin"
    assert result[1]["qcode"] == "dpaarea:3"


def test_render_located_no_qcode():
    result = render_located(None, [lambda c: [Category(name="Hamburg")]])
    assert result is not None
    assert len(result) == 1
    assert result[0]["name"] == "Hamburg"
    assert result[0]["qcode"] is None


def test_render_located_no_located():
    result = render_located(None, [lambda c: []])
    assert result is not None
    assert len(result) == 0


def test_render_genre():
    result = render_genre(
        None, lambda c: Category(name="Zusammenfassung", qcode="dpatextgenre:26")
    )
    assert result is not None
    assert len(result) == 2
    assert result["name"] == "Zusammenfassung"
    assert result["qcode"] == "dpatextgenre:26"


def test_render_dpasubjects():
    result = render_subjects(
        None,
        [
            lambda c: [
                Category(
                    category_type="dnltype:dpasubject",
                    name="Politik",
                    qcode="medtop:11000000",
                    rank=1,
                )
            ]
        ],
    )
    assert result is not None
    assert len(result) == 1
    assert result[0]["type"] == "dpatype:dpasubject"
    assert result[0]["name"] == "Politik"
    assert result[0]["qcode"] == "medtop:11000000"
    assert result[0]["rank"] == "1"


def test_render_dpasubjects_more_subjects():
    result = render_subjects(
        None,
        [
            lambda c: [
                Category(
                    category_type="dnltype:dpasubject",
                    name="Politik",
                    qcode="medtop:11000000",
                    rank=1,
                ),
                Category(
                    category_type="dnltype:dpasubject",
                    name="Vorschau",
                    qcode="dpasubject:432",
                    rank=2,
                ),
            ]
        ],
    )
    assert result is not None
    assert len(result) == 2
    assert result[0]["type"] == "dpatype:dpasubject"
    assert result[0]["name"] == "Politik"
    assert result[0]["qcode"] == "medtop:11000000"
    assert result[0]["rank"] == "1"
    assert result[1]["type"] == "dpatype:dpasubject"
    assert result[1]["name"] == "Vorschau"
    assert result[1]["qcode"] == "dpasubject:432"
    assert result[1]["rank"] == "2"


def test_render_dpasubjects_more_exttractor():
    result = render_subjects(
        None,
        [
            lambda c: [
                Category(
                    category_type="dnltype:dpasubject",
                    name="Politik",
                    qcode="medtop:11000000",
                    rank=1,
                ),
            ],
            lambda c: [
                Category(
                    category_type="dnltype:dpasubject",
                    name="Vorschau",
                    qcode="dpasubject:432",
                    rank=2,
                ),
            ],
        ],
    )
    assert result is not None
    assert len(result) == 2
    assert result[0]["type"] == "dpatype:dpasubject"
    assert result[0]["name"] == "Politik"
    assert result[0]["qcode"] == "medtop:11000000"
    assert result[0]["rank"] == "1"
    assert result[1]["type"] == "dpatype:dpasubject"
    assert result[1]["name"] == "Vorschau"
    assert result[1]["qcode"] == "dpasubject:432"
    assert result[1]["rank"] == "2"


def test_render_dpasubjects_invalid_subjects():
    result = render_subjects(
        None,
        [
            lambda c: [
                Category(
                    category_type="dnltype:dpasubject",
                    name="Politik",
                    qcode="medtop:11000000",
                    rank=1,
                ),
                Category(category_type="dnltype:dpasubject", rank=2),
            ]
        ],
    )
    assert result is not None
    assert len(result) == 1
    assert result[0]["type"] == "dpatype:dpasubject"
    assert result[0]["name"] == "Politik"
    assert result[0]["qcode"] == "medtop:11000000"
    assert result[0]["rank"] == "1"


def test_render_dpasubjects_with_desk():
    result = render_subjects(
        None,
        [
            lambda c: [
                Category(category_type="dnltype:desk", name="sp", qcode="dpacat:sp"),
            ],
            lambda c: [
                Category(
                    category_type="dnltype:dpasubject",
                    name="Vorschau",
                    qcode="dpasubject:432",
                    rank=1,
                ),
            ],
        ],
    )
    assert result is not None
    assert len(result) == 2
    assert result[0]["type"] == "dpatype:category"
    assert result[0]["name"] == "sp"
    assert result[0]["qcode"] == "dpacat:sp"
    assert result[0]["rank"] is None
    assert result[1]["type"] == "dpatype:dpasubject"
    assert result[1]["name"] == "Vorschau"
    assert result[1]["qcode"] == "dpasubject:432"
    assert result[1]["rank"] == "1"


def test_render_audience():
    result = render_audience(
        None, [lambda c: [Category(name="Hamburg", qcode="dpaaudience:hamburg")]]
    )
    assert result is not None
    assert len(result) == 1
    assert result[0]["name"] == "Hamburg"
    assert result[0]["qcode"] == "dpaaudience:hamburg"


def test_render_audience_multiple():
    result = render_audience(
        None,
        [
            lambda c: [
                Category(name="Hamburg", qcode="dpaaudience:hamburg"),
                Category(name="Niedersachsen", qcode="dpaaudience:niedersachsen"),
            ]
        ],
    )
    assert result is not None
    assert len(result) == 2
    assert result[0]["name"] == "Hamburg"
    assert result[0]["qcode"] == "dpaaudience:hamburg"
    assert result[1]["name"] == "Niedersachsen"
    assert result[1]["qcode"] == "dpaaudience:niedersachsen"


def test_render_audience_empty():
    result = render_audience(None, [lambda c: []])
    assert result is not None
    assert len(result) == 0


def test_render_audience_invalid_scope():
    result = render_audience(
        None,
        [
            lambda c: [
                Category(name="Hamburg", qcode="dpaaudience:hamburg"),
                Category(),
            ]
        ],
    )
    assert result is not None
    assert len(result) == 1
    assert result[0]["name"] == "Hamburg"
    assert result[0]["qcode"] == "dpaaudience:hamburg"


def test_render_keywords():
    result = render_keywords(
        None,
        [
            lambda c: [
                Category(category_type="dnltype:keyword", name="Politik", rank=1),
                Category(category_type="dnltype:keyword", name="Krieg", rank=2),
            ]
        ],
    )
    assert result is not None
    assert len(result) == 2
    assert result[0]["name"] == "Politik"
    assert result[0]["rank"] == "1"
    assert result[1]["name"] == "Krieg"
    assert result[1]["rank"] == "2"


def test_render_keywords_no_rank():
    result = render_keywords(
        None,
        [
            lambda c: [
                Category(category_type="dnltype:keyword", name="Politik"),
            ]
        ],
    )
    assert result is not None
    assert len(result) == 1
    assert result[0]["name"] == "Politik"
    assert result[0]["rank"] is None


def test_render_keywords_same_order():
    result = render_keywords(
        None,
        [
            lambda c: [
                Category(category_type="dnltype:keyword", name="Krieg", rank=2),
                Category(category_type="dnltype:keyword", name="Politik", rank=1),
            ]
        ],
    )
    assert result is not None
    assert len(result) == 2
    assert result[0]["name"] == "Krieg"
    assert result[0]["rank"] == "2"
    assert result[1]["name"] == "Politik"
    assert result[1]["rank"] == "1"


def test_render_descriptions():
    result = render_descriptions(
        None,
        [
            lambda c: [
                Description(role="drol:caption", description="Lorem Ipsum"),
            ]
        ],
    )
    assert result is not None
    assert len(result) == 1
    assert result[0]["role"] == "drol:caption"
    assert result[0]["value"] == "Lorem Ipsum"
