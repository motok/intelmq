# -*- coding: utf-8 -*-
"""
Testing asn_lookup.

see asn_lookup README for how to download database
It is expected at /opt/intelmq/var/lib/bots/asn_lookup/ipasn.dat by default
"""
from __future__ import unicode_literals

import json
import os
import unittest

import intelmq.lib.test as test
from intelmq.bots.experts.asn_lookup.expert import ASNLookupExpertBot


ASN_DB = '/opt/intelmq/var/lib/bots/asn_lookup/ipasn.dat'
EXAMPLE_INPUT = {"__type": "Event",
                 "source.ip": "93.184.216.34",  # example.com
                 "destination.ip": "192.0.43.8",  # iana.org
                 "time.observation": "2015-01-01T00:00:00+00:00",
                 }
EXAMPLE_OUTPUT = {"__type": "Event",
                  "source.ip": "93.184.216.34",
                  "source.asn": 15133,
                  "source.network": "93.184.216.0/24",
                  "destination.ip": "192.0.43.8",
                  "time.observation": "2015-01-01T00:00:00+00:00",
                  "destination.asn": 16876,
                  "destination.network": "192.0.43.0/24",
                  }
EXAMPLE_INPUT6 = {"__type": "Event",
                  "source.ip": "2001:500:88:200::7",  # iana.org
                  "time.observation": "2015-01-01T00:00:00+00:00",
                  }
EXAMPLE_OUTPUT6 = {"__type": "Event",
                   "source.ip": "2001:500:88:200::7",
                   "time.observation": "2015-01-01T00:00:00+00:00",
                   "source.asn": 16876,
                   "source.network": "2001:500:88::/48",
                   }


@unittest.skipUnless(os.path.exists(ASN_DB), 'asn-lookup database does not'
                                             'exist in {}.'.format(ASN_DB))
class TestASNLookupExpertBot(test.BotTestCase, unittest.TestCase):
    """
    A TestCase for AbusixExpertBot.
    """

    @classmethod
    def set_bot(self):
        self.bot_reference = ASNLookupExpertBot
        self.sysconfig = {'database': ASN_DB}
        self.default_input_message = {'__type': 'Report'}

    def test_ipv4_lookup(self):
        self.input_message = EXAMPLE_INPUT
        self.run_bot()
        self.assertMessageEqual(0, EXAMPLE_OUTPUT)

    @unittest.expectedFailure
    def test_ipv6_lookup(self):
        self.input_message = EXAMPLE_INPUT6
        self.run_bot()
        self.assertMessageEqual(0, EXAMPLE_OUTPUT6)


if __name__ == '__main__':
    unittest.main()
