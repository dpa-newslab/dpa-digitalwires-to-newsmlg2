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

import json
import os

import pytest


@pytest.fixture(scope="module")
def test_data_json(test_data_filenames):
    test_jsons = dict()
    for filename in test_data_filenames:
        file_path = os.path.join(os.path.dirname(__file__), "data/input", filename)
        with open(file_path) as f:
            test_jsons[filename] = json.load(f)
    return test_jsons


@pytest.fixture(scope="module")
def result_data_g2(result_data_filenames):
    result_g2 = dict()
    for filename in result_data_filenames:
        file_path = os.path.join(os.path.dirname(__file__), "data/output", filename)
        with open(file_path) as f:
            result_g2[filename] = f.read()
    return result_g2


@pytest.fixture(scope="module")
def test_data_filenames():
    return [
        "audio.json",
        "dw-1.json",
        "eil.json",
        "embargoed.json",
        "empty_paragraph.json",
        "hoerfunk.json",
        "image.json",
        "lesestuecke.json",
        "no_content.json",
        "no_notepad.json",
        "nsb_n1.json",
        "rubix_multimedia_real.json",
        "rubix_multimedia_testartikel.json",
        "spe2.json",
        "spe_tab.json",
        "tvo_pol.json",
        "with_dateline.json",
        "with_infobox.json",
    ]


@pytest.fixture(scope="module")
def result_data_filenames():
    return [
        "audio.xml",
        "dw-1.xml",
        "eil.xml",
        "embargoed.xml",
        "empty_paragraph.xml",
        "hoerfunk.xml",
        "image.xml",
        "lesestuecke.xml",
        "no_content.xml",
        "no_notepad.xml",
        "nsb_n1.xml",
        "rubix_multimedia_real.xml",
        "rubix_multimedia_testartikel.xml",
        "spe2.xml",
        "spe_tab.xml",
        "tvo_pol.xml",
        "with_dateline.xml",
        "with_infobox.xml",
    ]
