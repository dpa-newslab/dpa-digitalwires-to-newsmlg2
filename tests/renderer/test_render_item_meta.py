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
import pytest

from newsmlg2 import DigitalwiresModel
from newsmlg2.renderer.render_item_meta import (
    render_pubstatus,
    render_services,
    render_ednotes,
    render_signal,
    render_links,
    render_notepad,
)
from newsmlg2.utils.objects import Link, Category, EdNote


def test_render_pubstatus():
    result = render_pubstatus(None, lambda c: "stat:usable", lambda c: "usable")
    assert "qcode" in result
    assert "name" in result
    assert result["qcode"] == "stat:usable"
    assert result["name"] == "usable"


def test_render_pubstatus_no_name():
    result = render_pubstatus(None, lambda c: "stat:usable", lambda c: None)
    assert "qcode" in result
    assert "name" in result
    assert result["qcode"] == "stat:usable"
    assert result["name"] is None


def test_render_services():
    result = render_services(
        None, [lambda c: [Category(qcode="dpasrv:bdt", name="bdt")]]
    )
    assert len(result) == 1
    assert "qcode" in result[0]
    assert "name" in result[0]
    assert result[0]["qcode"] == "dpasrv:bdt"
    assert result[0]["name"] == "bdt"


def test_render_services_multiple():
    result = render_services(
        None,
        [
            lambda c: [Category(qcode="dpasrv:bdt", name="bdt")],
            lambda c: [Category(qcode="dpasrv:nsb", name="nsb")],
        ],
    )
    assert len(result) == 2
    assert "qcode" in result[0]
    assert "name" in result[0]
    assert result[0]["qcode"] == "dpasrv:bdt"
    assert result[0]["name"] == "bdt"
    assert "qcode" in result[1]
    assert "name" in result[1]
    assert result[1]["qcode"] == "dpasrv:nsb"
    assert result[1]["name"] == "nsb"


def test_render_services_no_name():
    result = render_services(None, [lambda c: [Category(qcode="dpasrv:bdt")]])
    assert len(result) == 1
    assert "qcode" in result[0]
    assert "name" in result[0]
    assert result[0]["qcode"] == "dpasrv:bdt"
    assert result[0]["name"] is None


def test_render_ednotes():
    result = render_ednotes(
        None,
        [
            lambda c: [
                EdNote(
                    role="dpaednoterole:closingline",
                    ednote="dpa kre/su yysw a3 lön mda",
                ),
                EdNote(
                    role="dpaednoterole:editorialnote",
                    ednote="Zu diesem Text finden Sie Bilder mit folgendem Titel im dpa Bildangebot:",
                ),
                EdNote(
                    role="dpaednoterole:editorialnote",
                    ednote="Nahostkonflikt - Beirut",
                ),
            ]
        ],
    )
    assert len(result) == 3
    for ednote in result:
        assert "role" in ednote
        assert "text" in ednote
        assert ednote["role"].startswith("dpaednoterole")
        assert len(ednote["text"]) > 0


def test_render_ednotes_no_ednote():
    result = render_ednotes(
        None,
        [lambda c: []],
    )
    assert len(result) == 0


def test_render_ednotes_none_ednote():
    result = render_ednotes(
        None,
        [lambda c: [EdNote()]],
    )
    assert len(result) == 0


def test_render_signals():
    result = render_signal(
        None,
        lambda c: ["sig:correction"],
    )
    assert len(result) == 1
    assert result[0] == "sig:correction"


def test_render_signals_no_signal():
    result = render_signal(
        None,
        lambda c: [""],
    )
    assert result is None


def test_render_signals_none_signal():
    result = render_signal(
        None,
        lambda c: [None],
    )
    assert result is None


@pytest.fixture(scope="function")
def link1():
    return Link(
        urn="urn1",
        url="http://example.com",
        rank="1",
        rel="irel:seeAlso",
        version="1",
        assoc_type="image",
        title="Lorem ipsum dolor sit amet",
    )


@pytest.fixture(scope="function")
def link2():
    return Link(
        urn="urn2",
        url="http://example2.com",
        rank="2",
        rel="irel:seeAlso",
        version="1",
        assoc_type="image",
        title="Foo Bar",
    )


@pytest.fixture(scope="function")
def text_context():
    return DigitalwiresModel(
        {"article_html": '<section class="main"><p>Lorem ipsum</p></section>'}
    )


def test_render_link(text_context, link1):
    result = render_links(text_context, [lambda c: [link1]])
    assert len(result) == 1
    assert validate_link(result[0], link1, 1)


def test_render_link_multiple(text_context, link1, link2):
    result = render_links(text_context, [lambda c: [link1, link2]])
    assert len(result) == 2
    assert validate_link(result[0], link1, 1)
    assert validate_link(result[1], link2, 2)


def test_render_link_wrong_order(text_context, link1, link2):
    result = render_links(text_context, [lambda c: [link2, link1]])
    assert len(result) == 2
    assert validate_link(result[0], link1, 1)
    assert validate_link(result[1], link2, 2)


def validate_link(result, expected_link, idx):
    if result is None:
        return False
    return (
        result["urn"] == expected_link.urn
        and result["href"] == expected_link.url
        and result["rank"] == str(idx)
        and result["rel"] == expected_link.rel
        and result["version"] == expected_link.version
        and result["title"] == expected_link.title
        and result["itemClass"].startswith("ninat:")
    )


def test_render_notepad():
    result = render_notepad(
        None,
        extract_header=lambda c: "Foo",
        extract_public=lambda c: "Bar",
        extract_non_public=lambda c: "Baz",
        extract_closingline=lambda c: "dpa kre/su yysw a3 lön mda",
    )
    assert result is not None
    assert result["header"] == "Foo"
    assert result["public"] == "Bar"
    assert result["non_public"] == "Baz"
    assert result["closingline"] == "dpa kre/su yysw a3 lön mda"


def test_render_notepad_none():
    result = render_notepad(
        None,
        extract_header=lambda c: "Foo",
        extract_public=lambda c: None,
        extract_non_public=lambda c: None,
        extract_closingline=lambda c: "dpa kre/su yysw a3 lön mda",
    )
    assert result is None


def test_render_notepad_public_none():
    result = render_notepad(
        None,
        extract_header=lambda c: "Foo",
        extract_public=lambda c: None,
        extract_non_public=lambda c: "Baz",
        extract_closingline=lambda c: "dpa kre/su yysw a3 lön mda",
    )
    assert result is not None
    assert result["header"] == "Foo"
    assert result["public"] is None
    assert result["non_public"] == "Baz"
    assert result["closingline"] == "dpa kre/su yysw a3 lön mda"


def test_render_notepad_non_public_none():
    result = render_notepad(
        None,
        extract_header=lambda c: "Foo",
        extract_public=lambda c: "Bar",
        extract_non_public=lambda c: None,
        extract_closingline=lambda c: "dpa kre/su yysw a3 lön mda",
    )
    assert result is not None
    assert result["header"] == "Foo"
    assert result["public"] == "Bar"
    assert result["non_public"] is None
    assert result["closingline"] == "dpa kre/su yysw a3 lön mda"
