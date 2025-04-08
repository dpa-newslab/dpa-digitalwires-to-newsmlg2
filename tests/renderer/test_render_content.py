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

from newsmlg2.renderer.render_content import (
    render_article,
    render_slugline,
    render_infobox,
)
from newsmlg2.utils.objects import Category


def test_render_article():
    result = render_article(
        None,
        lambda c: "Hamburg (dpa) - ",
        lambda c: '<section class="main"><p>Lorem ipsum</p></section>',
    )

    assert result is not None
    assert len(result) > 0
    assert (
        result[0]
        == '<p><span class="dateline">Hamburg <span class="credit">(dpa)</span> - </span>Lorem ipsum</p>'
    )


def test_render_article_has_dateline():
    result = render_article(
        None,
        lambda c: "Berlin (dpa) - ",
        lambda c: '<section class="main"><p><span class="dateline">Hamburg <span class="credit">(dpa)</span> - </span>Lorem ipsum</p></section>',
    )

    assert result is not None
    assert len(result) > 0
    assert (
        result[0]
        == '<p><span class="dateline">Hamburg <span class="credit">(dpa)</span> - </span>Lorem ipsum</p>'
    )


def test_render_article_no_dateline():
    result = render_article(
        None,
        lambda c: None,
        lambda c: '<section class="main"><p>Lorem ipsum</p></section>',
    )

    assert result is not None
    assert len(result) > 0
    assert result[0] == "<p>Lorem ipsum</p>"


def test_render_article_no_content():
    result = render_article(
        None,
        lambda c: "Berlin (dpa) - ",
        lambda c: '<section class="main"></section>',
    )

    assert result is not None
    assert len(result) == 0


def test_render_infobox():
    result = render_infobox(
        None,
        lambda c: '<section class="infobox"><h2>Links</h2><p><a class="externalLink" href="https://www.dw.com/de/faktencheck-energiewaffen-sind-nicht-ursache-f%C3%BCr-waldbr%C3%A4nde-in-maui/a-66558463">DW-Faktencheck zu Bränden auf Hawaii</a> (<a class="externalLink" href="https://archive.today/cf9TN">archiviert</a>)</p><p><a class="externalLink" href="https://dpa-factchecking.com/germany/230811-99-807254/">dpa-Faktencheck zu Bränden auf Hawaii</a></p><p><a class="externalLink" href="https://dpa-factchecking.com/germany/230831-99-26871/">dpa-Faktencheck zu Bränden in Paradise</a></p><p><a class="externalLink" href="https://www.medienanstalt-nrw.de/fileadmin/user_upload/NeueWebsite_0120/Presse/Pressemitteilung/230303-HandbuchVerifikation_final">Informationen zur Bilderrückwärtssuche</a> (<a class="externalLink" href="https://archive.today/DFwrO">archiviert</a>)</p><p><a class="externalLink" href="https://www.google.com/maps/place/Paradise,+Kalifornien+95969,+USA/@37.2728542,-119.9763303,7.96z/data=!4m6!3m5!1s0x80832bd49578303f:0x50c92f9d6b33aa70!8m2!3d39.7596061!4d-121.6219177!16zL20vMHF5OHQ?entry=ttu&amp;g_ep=EgoyMDI1MDExNS4wIKXMDSoASAFQAw%3D%3D">Standort von kalifornischer Stadt Paradise</a> (<a class="externalLink" href="https://archive.today/b3dbz">archiviert</a>)</p><p><a class="externalLink" href="https://www.cbsnews.com/news/palisades-fire-los-angeles-california-blazes-images/#textThe20Palisades20Fire20ravagesAP20PHOTOETHAN20SWOPE">Fotos der Brände in Los Angeles I</a> (<a class="externalLink" href="https://archive.today/oABtu">archiviert</a>)</p><p><a class="externalLink" href="https://www.nbcdfw.com/news/national-international/images-palisades-fire-as-seen-from-around-southern-california/3735568/#:~:text=A%20palm%20tree%20burns%20during%20the%20Palisades%20Fire%20in%20the%20Pacific%20Palisades%20neighborhood%20on%20Jan.%207%2C%202025.">Fotos der Brände in Los Angeles II</a> (<a class="externalLink" href="https://archive.today/hPOtp">archiviert</a>)</p><p><a class="externalLink" href="https://www.theatlantic.com/photo/2025/01/photos-palisades-fire-los-angeles-california/681241/">Fotos der Brände in Los Angeles III</a> (<a class="externalLink" href="https://archive.today/d5lDa">archiviert</a>)</p><p><a class="externalLink" href="https://unidir.org/directed-energy-weapons-a-new-look-at-an-old-technology/">Informationen über DEW</a> (<a class="externalLink" href="https://web.archive.org/web/20250114193231/https://unidir.org/directed-energy-weapons-a-new-look-at-an-old-technology/">archiviert</a>)</p><p><a class="externalLink" href="https://www.spiegel.de/wissenschaft/natur/kalifornien-satellitenbilder-zeigen-paradise-vor-und-nach-waldbraenden-a-1239554.html">Spiegel über Brände in Paradise im Jahr 2018</a> (<a class="externalLink" href="https://web.archive.org/web/20240104061848/https://www.spiegel.de/wissenschaft/natur/kalifornien-satellitenbilder-zeigen-paradise-vor-und-nach-waldbraenden-a-1239554.html">archiviert</a>)</p><p><a class="externalLink" href="https://www.cbc.ca/news/world/los-angeles-wildfire-trees-1.7428870">CBC News-Artikel über Bäume bei den Bränden</a> (<a class="externalLink" href="https://archive.today/nX2I2">archiviert</a>)</p><p><a class="externalLink" href="https://www.escondido.gov/DocumentCenter/View/4330/Palm-Trees-as-Fire-Hazards-PDF">Informationen zur Entflammbarkeit von Palmen</a> (<a class="externalLink" href="https://web.archive.org/web/20250114102435/https://www.escondido.gov/DocumentCenter/View/4330/Palm-Trees-as-Fire-Hazards-PDF">archiviert</a>)</p><p><a class="externalLink" href="https://www.latimes.com/environment/story/2023-11-08/its-been-5-years-since-californias-deadliest-wildfire-can-we-stop-it-from-happening-again">LA Times-Artikel zu Bränden in Paradise in 2018</a> (<a class="externalLink" href="https://archive.today/7RcHc">archiviert</a>)</p><p><a class="externalLink" href="https://www.fire.ca.gov/incidents/2025/1/7/palisades-fire">Betroffenes Gebiet der Brände in Los Angeles</a> (<a class="externalLink" href="https://perma.cc/F9X6-ECV6">archiviert</a>)</p><p><a class="externalLink" href="https://www.sueddeutsche.de/panorama/waldbraende-los-angeles-loeschen-li.3182076">SZ-Interview zu Ursachen der Brände in Los Angeles</a> (<a class="externalLink" href="https://archive.vn/6F2Jj">archiviert</a>)</p><p><a class="externalLink" href="https://www.nist.gov/news-events/news/2021/02/new-timeline-deadliest-california-wildfire-could-guide-lifesaving-research">Bericht über Brände in Paradise im Jahr 2018</a> (<a class="externalLink" href="https://web.archive.org/web/20250117234023/https://www.nist.gov/news-events/news/2021/02/new-timeline-deadliest-california-wildfire-could-guide-lifesaving-research">archiviert</a>)</p><p><a class="externalLink" href="https://www.zdf.de/nachrichten/panorama/klima-kalifornien-los-angeles-feuer-100.html">ZDF-Artikel zu Ursachen der Brände in Los Angeles</a> (<a class="externalLink" href="https://web.archive.org/web/20250114210102/https://www.zdf.de/nachrichten/panorama/klima-kalifornien-los-angeles-feuer-100.html">archiviert</a>)</p><p><a class="externalLink" href="https://www.tagesspiegel.de/wissen/erneut-feuerwetter-in-los-angeles-klimawandel-erhoht-die-wahrscheinlichkeit-sich-schnell-ausbreitender-brande-13049464.html">Tagesspiegel zu Ursachen der Brände in Los Angeles</a> (<a class="externalLink" href="https://web.archive.org/web/20250122135930/https://www.tagesspiegel.de/wissen/erneut-feuerwetter-in-los-angeles-klimawandel-erhoht-die-wahrscheinlichkeit-sich-schnell-ausbreitender-brande-13049464.html">archiviert</a>)</p><p><a class="externalLink" href="https://www.n-tv.de/der_tag/Vorher-nachher-Bilder-aus-Paradise-article20730271.html">ntv-Artikel mit Satellitenaufnahme aus 2018</a> (<a class="externalLink" href="https://archive.today/nv0mm">archiviert</a>)</p><p><a class="externalLink" href="https://www.facebook.com/jojo.ungar.9/posts/pfbid02d1bKUJjPYbqJ4zVX9UectEVgNSrnTmqLCiZQuF269pmjVjnvGaYvgTfE7yNHUcLYl">Facebook-Post</a> (<a class="externalLink" href="https://ghostarchive.org/archive/e2OJL">archiviert</a>)</p></section>',
    )

    assert result is not None
    assert len(result) > 0
    assert result.startswith('<div class="INFOBOX">')
    assert result.endswith("</div>")


def test_render_infobox_none():
    result = render_infobox(
        None,
        lambda c: None,
    )

    assert result is None


def test_render_slugline_subject():
    result = render_slugline(
        None,
        [
            lambda c: [
                Category(
                    category_type="dnltype:dpasubject",
                    name="Foo",
                    qcode="dpasubject:foo",
                    rank=None,
                ),
            ]
        ],
    )
    assert result is not None
    assert len(result) == 1
    assert result[0]["kind"] == "subject"
    assert result[0]["name"] == "Foo"
    assert result[0]["qcode"] == "dpasubject:foo"


def test_render_slugline_geo():
    result = render_slugline(
        None,
        [
            lambda c: [
                Category(
                    category_type="dnltype:geosubject",
                    name="Bar",
                    qcode="geosubject:bar",
                    rank=None,
                ),
            ]
        ],
    )
    assert result is not None
    assert len(result) == 1
    assert result[0]["kind"] == "geo"
    assert result[0]["name"] == "Bar"
    assert result[0]["qcode"] == "geosubject:bar"


def test_render_slugline_keywords():
    result = render_slugline(
        None,
        [
            lambda c: [
                Category(
                    category_type="dnltype:keyword",
                    name="Baz",
                    qcode="geosubject:baz",
                    rank=None,
                ),
            ]
        ],
    )
    assert result is not None
    assert len(result) == 1
    assert result[0]["kind"] == "keyword"
    assert result[0]["name"] == "Baz"
    assert result[0]["qcode"] == "geosubject:baz"


def test_render_slugline_multiple():
    result = render_slugline(
        None,
        [
            lambda c: [
                Category(
                    category_type="dnltype:dpasubject",
                    name="Foo",
                    qcode="dpasubject:foo",
                    rank=None,
                ),
                Category(
                    category_type="dnltype:geosubject",
                    name="Bar",
                    qcode="geosubject:bar",
                    rank=None,
                ),
                Category(
                    category_type="dnltype:keyword",
                    name="Baz",
                    qcode="geosubject:baz",
                    rank=None,
                ),
            ]
        ],
    )
    assert result is not None
    assert len(result) == 3
    assert result[0]["kind"] == "subject"
    assert result[0]["name"] == "Foo"
    assert result[0]["qcode"] == "dpasubject:foo"
    assert result[1]["kind"] == "geo"
    assert result[1]["name"] == "Bar"
    assert result[1]["qcode"] == "geosubject:bar"
    assert result[2]["kind"] == "keyword"
    assert result[2]["name"] == "Baz"
    assert result[2]["qcode"] == "geosubject:baz"


def test_render_slugline_none():
    result = render_slugline(
        None,
        [
            lambda c: [
                Category(category_type="dnltype:dpasubject"),
            ]
        ],
    )
    assert result is not None
    assert len(result) == 0


def test_render_slugline_reduced():
    result = render_slugline(
        None,
        [
            lambda c: [
                Category(category_type="dnltype:dpasubject", name="Foo"),
            ]
        ],
    )
    assert result is not None
    assert len(result) == 1
    assert result[0]["kind"] == "subject"
    assert result[0]["name"] == "Foo"
