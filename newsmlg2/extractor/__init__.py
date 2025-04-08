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

from .association_extractor import get_associations
from .category_extractor import (
    get_provider_name,
    get_provider_qcode,
    get_pubstatus_qcode,
    get_pubstatus_name,
    get_poi,
    get_creator,
    get_located,
    get_keywords,
    get_services,
    get_infosource,
    get_contributor,
    get_geo_subject,
    get_dpa_subjects,
    get_scope,
    get_genre,
    get_desk,
    get_signal_qcodes,
)
from .content_extractor import get_article, get_headline, get_teaser, get_kicker
from .description_extractor import get_descriptions
from .meta_extractor import (
    get_linkbox,
    get_urn,
    get_byline,
    get_embargo,
    get_copyright_notice,
    get_dateline,
    get_language,
    get_urgency,
    get_creditline,
    get_content_created,
    get_version_created,
    get_version,
    get_infobox,
    get_usageterms,
)
from .notepad_extractor import (
    get_embargo_notice,
    get_embargo_note,
    get_genre_note,
    get_non_public_notepad,
    get_notepad_header,
    get_picture_ednote_de,
    get_public_notepad,
    get_ednotes,
    get_closing_line,
    get_correction,
)
