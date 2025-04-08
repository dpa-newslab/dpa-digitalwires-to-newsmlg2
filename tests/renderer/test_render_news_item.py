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

from newsmlg2.renderer.render_news_item import render_provider, render_version


def test_render_provider():
    result = render_provider(None, lambda c: "dnlprov:dpa", lambda c: "dpa")
    assert "qcode" in result
    assert "name" in result
    assert result["qcode"] == "dnlprov:dpa"
    assert result["name"] == "dpa"


def test_render_provider_no_name():
    result = render_provider(None, lambda c: "dnlprov:dpa", lambda c: None)
    assert "qcode" in result
    assert "name" in result
    assert result["qcode"] == "dnlprov:dpa"
    assert result["name"] is None


def test_render_version():
    result = render_version(None, lambda c: "1")
    assert result == 1
