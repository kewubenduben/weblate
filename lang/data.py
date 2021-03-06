# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2013 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <http://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


# Extra languages not included in ttkit
EXTRALANGS = (
    (
        'ur',
        'Urdu',
        2,
        '(n != 1)',
    ),
    (
        'uz@latin',
        'Uzbek (latin)',
        1,
        '0',
    ),
    (
        'uz',
        'Uzbek',
        1,
        '0',
    ),
    (
        'sr@latin',
        'Serbian (latin)',
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && '
        '(n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'sr_RS@latin',
        'Serbian (latin)',
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && '
        '(n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'sr@cyrillic',
        'Serbian (cyrillic)',
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && '
        '(n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'sr_RS@cyrillic',
        'Serbian (cyrillic)',
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && '
        '(n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'be@latin',
        'Belarusian (latin)',
        3,
        'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && '
        '(n%100<10 || n%100>=20) ? 1 : 2',
    ),
    (
        'en_US',
        'English (United States)',
        2,
        'n != 1',
    ),
    (
        'nb_NO',
        'Norwegian Bokmål',
        2,
        'n != 1',
    ),
    (
        'pt_PT',
        'Portuguese (Portugal)',
        2,
        'n > 1',
    ),
    (
        'ckb',
        'Kurdish Sorani',
        2,
        'n != 1',
    ),
    (
        'vls',
        'West Flemish',
        2,
        'n != 1',
    ),
    (
        'zh',
        'Chinese',
        1,
        '0',
    ),
    (
        'tlh',
        'Klingon',
        1,
        '0',
    ),
    (
        'tlh-qaak',
        'Klingon (pIqaD)',
        1,
        '0',
    ),
)

# List of defaul languages - the ones, where using
# only language code should be same as this one
# Extracted from locale.alias
DEFAULT_LANGS = (
    'af_ZA',
    'am_ET',
    'ar_AA',
    'as_IN',
    'az_AZ',
    'be_BY',
    'bg_BG',
    'br_FR',
    'bs_BA',
    'ca_ES',
    'cs_CZ',
    'cy_GB',
    'da_DK',
    'de_DE',
    'ee_EE',
    'el_GR',
    'en_US',
    'eo_XX',
    'es_ES',
    'et_EE',
    'eu_ES',
    'fa_IR',
    'fi_FI',
    'fo_FO',
    'fr_FR',
    'ga_IE',
    'gd_GB',
    'gl_ES',
    'gv_GB',
    'he_IL',
    'hi_IN',
    'hr_HR',
    'hu_HU',
    'id_ID',
    'is_IS',
    'it_IT',
    'iu_CA',
    'ja_JP',
    'ka_GE',
    'kl_GL',
    'km_KH',
    'kn_IN',
    'ko_KR',
    'ks_IN',
    'kw_GB',
    'ky_KG',
    'lo_LA',
    'lt_LT',
    'lv_LV',
    'mi_NZ',
    'mk_MK',
    'ml_IN',
    'mr_IN',
    'ms_MY',
    'mt_MT',
    'nb_NO',
    'nl_NL',
    'nn_NO',
    'no_NO',
    'nr_ZA',
    'ny_NO',
    'oc_FR',
    'or_IN',
    'pa_IN',
    'pd_US',
    'ph_PH',
    'pl_PL',
    'pp_AN',
    'pt_PT',
    'ro_RO',
    'ru_RU',
    'rw_RW',
    'sd_IN',
    'si_LK',
    'sk_SK',
    'sl_SI',
    'sq_AL',
    'sr_RS',
    'ss_ZA',
    'st_ZA',
    'sv_SE',
    'ta_IN',
    'te_IN',
    'tg_TJ',
    'th_TH',
    'tl_PH',
    'tn_ZA',
    'tr_TR',
    'ts_ZA',
    'tt_RU',
    'uk_UA',
    'ur_IN',
    'uz_UZ',
    've_ZA',
    'vi_VN',
    'wa_BE',
    'xh_ZA',
    'yi_US',
    'zu_ZA',
)

# List of RTL languages
RTL_LANGS = set((
    'ar',
    'arc',
    'ckb',
    'dv',
    'fa',
    'ha',
    'he',
    'ks',
    'ku',
    'ps',
    'ug',
    'ur',
    'yi',
))


# Following variables are used to map Gettext plural equations
# to one/few/may/other like rules

ONE_OTHER_PLURALS = (
    'n==1 || n%10==1 ? 0 : 1',
    'n != 1',
    'n > 1',
    'n > 1',
)

TWO_OTHER_PLURALS = (
    '(n==2) ? 1 : 0',
)

ONE_FEW_OTHER_PLURALS = (
    'n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && '
    '(n%100<10 || n%100>=20) ? 1 : 2',
    '(n==1) ? 0 : (n>=2 && n<=4) ? 1 : 2',
    'n==1 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2',
    'n%10==1 && n%100!=11 ? 0 : n%10>=2 && (n%100<10 || n%100>=20) ? 1 : 2',
    'n==1 ? 0 : (n==0 || (n%100 > 0 && n%100 < 20)) ? 1 : 2',
)

ONE_TWO_OTHER_PLURALS = (
    'n==1 ? 0 : n==2 ? 1 : 2',
)

ONE_TWO_THREE_OTHER_PLURALS = (
    '(n==1) ? 0 : (n==2) ? 1 : (n == 3) ? 2 : 3',
)

ONE_TWO_FEW_OTHER_PLURALS = (
    '(n==1 || n==11) ? 0 : (n==2 || n==12) ? 1 : (n > 2 && n < 20) ? 2 : 3',
    'n%100==1 ? 0 : n%100==2 ? 1 : n%100==3 || n%100==4 ? 2 : 3',
)

ONE_TWO_FEW_MANY_OTHER_PLURALS = (
    'n==1 ? 0 : n==2 ? 1 : n<7 ? 2 : n<11 ? 3 : 4',
)

ONE_FEW_MANY_OTHER_PLURALS = (
    'n==1 ? 0 : n==0 || ( n%100>1 && n%100<11) ? 1 : '
    '(n%100>10 && n%100<20 ) ? 2 : 3'
)

ONE_OTHER_ZERO_PLURALS = (
    'n%10==1 && n%100!=11 ? 0 : n != 0 ? 1 : 2'
)
