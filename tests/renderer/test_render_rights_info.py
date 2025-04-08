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

from newsmlg2.renderer.render_rights_info import (
    render_copyright_notice,
    render_usageterms,
)


def test_render_copyright_notice():
    result = render_copyright_notice(None, lambda c: "All rights reserved.")
    assert len(result) > 0
    assert result == "All rights reserved."


def test_render_usageterms():
    result = render_usageterms(None, [lambda c: "No AI training."])
    assert len(result) == 1
    assert len(result[0]) > 0
    assert result[0] == "No AI training."


def test_render_usageterms_multiple():
    result = render_usageterms(
        None, [lambda c: "No AI training.", lambda c: "Only according to contract."]
    )
    assert len(result) == 2
    assert len(result[0]) > 0
    assert len(result[1]) > 0
    assert result[0] == "No AI training."
    assert result[1] == "Only according to contract."


def test_render_usageterms_none():
    result = render_usageterms(None, [lambda c: None])
    assert len(result) == 1
    assert result[0] is None
