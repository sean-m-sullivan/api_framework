# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Sean Sullivan <@sean-m-sullivan>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):

    # Ansible Galaxy documentation fragment
    DOCUMENTATION = r"""
options:
  host:
    description:
    - URL to Host instance.
    - If value not set, will try environment variable C(HOST)
    - If value not specified by any means, the value of C(127.0.0.1) will be used
    type: str
  username:
    description:
    - Username for your Host instance.
    - If value not set, will try environment variable C(USERNAME)
    type: str
  password:
    description:
    - Password for your Host instance.
    - If value not set, will try environment variable C(PASSWORD)
    type: str
  token:
    description:
    - The Host API token to use.
    - This value can be in one of two formats.
    - A string which is the token itself. (i.e. bqV5txm97wqJqtkxlMkhQz0pKhRMMX)
    - A dictionary structure as returned by the token module.
    - If value not set, will try environment variable C(API_TOKEN)
    type: raw
  validate_certs:
    description:
    - Whether to allow insecure connections to Galaxy or Automation Hub Server.
    - If C(no), SSL certificates will not be validated.
    - This should only be used on personally controlled sites using self-signed certificates.
    - If value not set, will try environment variable C(VERIFY_SSL)
    type: bool
    aliases: [ verify_ssl ]
"""
