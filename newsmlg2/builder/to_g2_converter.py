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
from abc import ABC, abstractmethod

from newsmlg2.digitalwires_model import DigitalwiresModel
from newsmlg2.extractor.association_extractor import get_associations
from newsmlg2.extractor.category_extractor import (
    get_pubstatus_qcode,
    get_pubstatus_name,
    get_provider_qcode,
    get_provider_name,
    get_services,
    get_signal_qcodes,
    get_located,
    get_infosource,
    get_creator,
    get_genre,
    get_geo_subject,
    get_dpa_subjects,
    get_scope,
    get_desk,
    get_keywords,
    get_poi,
    get_contributor,
)
from newsmlg2.extractor.content_extractor import (
    get_headline,
    get_kicker,
    get_teaser,
    get_article,
)
from newsmlg2.extractor.description_extractor import get_descriptions
from newsmlg2.extractor.meta_extractor import (
    get_embargo,
    get_urn,
    get_version,
    get_copyright_notice,
    get_usageterms,
    get_version_created,
    get_urgency,
    get_content_created,
    get_language,
    get_byline,
    get_dateline,
    get_creditline,
    get_linkbox,
    get_infobox,
)
from newsmlg2.extractor.notepad_extractor import (
    get_ednotes,
    get_notepad_header,
    get_public_notepad,
    get_non_public_notepad,
    get_closing_line,
    get_embargo_notice,
)
from newsmlg2.renderer import render_item_class
from newsmlg2.renderer.render_content import (
    render_slugline,
    render_article,
    render_infobox,
    render_remote_content,
)
from newsmlg2.renderer.render_content_meta import (
    render_content_created,
    render_located,
    render_infosource,
    render_creator,
    render_genre,
    render_subjects,
    render_audience,
    render_keywords,
    render_contributor,
    render_descriptions,
)
from newsmlg2.renderer.render_item_meta import (
    render_pubstatus,
    render_services,
    render_ednotes,
    render_signal,
    render_links,
    render_notepad,
)
from newsmlg2.renderer.render_news_item import render_version, render_provider
from newsmlg2.renderer.render_poi import render_pois
from newsmlg2.renderer.render_rights_info import (
    render_copyright_notice,
    render_usageterms,
)


class Converter(ABC):
    @abstractmethod
    def convert(self, article):
        pass


class DwToG2Converter(Converter):
    name = "dpa-digitalwires-to-newsmlg2"
    role = "dnlgenerator:dw2newsmlg2"
    version = "0.0.1"

    def convert(self, dw_model: DigitalwiresModel):

        return {
            # newsItem
            "urn": get_urn(dw_model),
            "version": render_version(dw_model, get_version),
            # rightsInfo
            "copyright_notice": render_copyright_notice(dw_model, get_copyright_notice),
            "usageterms": render_usageterms(dw_model, [get_usageterms]),
            # itemMeta
            "item_class": render_item_class(dw_model),
            "provider": render_provider(
                dw_model, get_provider_qcode, get_provider_name
            ),
            "version_created": get_version_created(dw_model),
            "embargoed": get_embargo(dw_model),
            "pubstatus": render_pubstatus(
                dw_model, get_pubstatus_qcode, get_pubstatus_name
            ),
            "generator": {
                "name": self.name,
                "role": self.role,
                "version": self.version,
            },
            "services": render_services(dw_model, [get_services]),
            "ednotes": render_ednotes(dw_model, [get_ednotes]),
            "notepad": render_notepad(
                dw_model,
                get_notepad_header,
                get_public_notepad,
                get_non_public_notepad,
                get_closing_line,
            ),
            "signals": render_signal(dw_model, get_signal_qcodes),
            "association_links": render_links(
                dw_model, [get_associations, get_linkbox]
            ),
            # contentMeta
            "urgency": get_urgency(dw_model),
            "content_created": render_content_created(dw_model, [get_content_created]),
            "located_list": render_located(dw_model, [get_located]),
            "info_sources": render_infosource(dw_model, [get_infosource]),
            "creators": render_creator(dw_model, [get_creator]),
            "contributors": render_contributor(dw_model, [get_contributor]),
            "genre": render_genre(dw_model, get_genre),
            "subjects": render_subjects(
                dw_model, [get_desk, get_geo_subject, get_dpa_subjects]
            ),
            "audiences": render_audience(dw_model, [get_scope]),
            "language": get_language(dw_model),
            "keywords": render_keywords(dw_model, [get_keywords]),
            "headline": get_headline(dw_model),
            "byline": get_byline(dw_model),
            "dateline": get_dateline(dw_model),
            "credit": get_creditline(dw_model),
            "descriptions": render_descriptions(dw_model, [get_descriptions]),
            # pois
            "pois": render_pois(dw_model, [get_poi]),
            # contentSet
            "kicker": get_kicker(dw_model),
            "teaser": get_teaser(dw_model),
            "embargo_notice": get_embargo_notice(dw_model),
            "sluglines": render_slugline(
                dw_model, [get_dpa_subjects, get_geo_subject, get_keywords]
            ),
            "article_html": (
                render_article(dw_model, get_dateline, get_article)
                if dw_model.is_text_message()
                else None
            ),
            "infobox": render_infobox(dw_model, get_infobox),
            "remote_contents": (
                render_remote_content(dw_model, [get_associations])
                if not dw_model.is_text_message()
                else None
            ),
        }
