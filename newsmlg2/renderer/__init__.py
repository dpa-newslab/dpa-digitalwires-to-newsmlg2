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

from .render_content import (
    render_remote_content,
    render_slugline,
    render_article,
    render_infobox,
)
from .render_content_meta import (
    render_content_created,
    render_creator,
    render_contributor,
    render_genre,
    render_infosource,
    render_descriptions,
    render_located,
    render_audience,
    render_subjects,
    render_keywords,
)
from .render_item_meta import (
    render_item_class,
    render_links,
    render_notepad,
    render_pubstatus,
    render_services,
    render_signal,
    render_ednotes,
)
from .render_news_item import render_provider, render_version
from .render_poi import render_pois
from .render_rights_info import render_usageterms, render_copyright_notice
