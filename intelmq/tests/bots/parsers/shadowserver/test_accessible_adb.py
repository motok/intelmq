# -*- coding: utf-8 -*-

import os
import unittest

import intelmq.lib.test as test
import intelmq.lib.utils as utils
from intelmq.bots.parsers.shadowserver.parser import ShadowserverParserBot

with open(os.path.join(os.path.dirname(__file__),
                       'accessible-adb.csv')) as handle:
    EXAMPLE_FILE = handle.read()
EXAMPLE_LINES = EXAMPLE_FILE.splitlines()

with open(os.path.join(os.path.dirname(__file__),
                       'accessible-adb_reconstructed.csv')) as handle:
    RECONSTRUCTED_FILE = handle.read()
RECONSTRUCTED_LINES = RECONSTRUCTED_FILE.splitlines()

EXAMPLE_REPORT = {"feed.name": "ShadowServer Accessible-ADB",
                  "raw": utils.base64_encode(EXAMPLE_FILE),
                  "__type": "Report",
                  "time.observation": "2018-07-30T00:00:00+00:00",
                  }
EVENTS = [{'__type': 'Event',
           'feed.name': 'ShadowServer Accessible-ADB',
           'time.observation': '2018-07-30T00:00:00+00:00',
           'time.source': '2018-07-26T02:07:16+00:00'},
           'classification.taxonomy': 'vulnerable',
           'classification.type': 'vulnerable service',
           'classification.identifier': 'accessible-adb',
           'protocol.application': 'adb',
           'protocol.transport': 'tcp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[1], ''])),
           'source.asn': 3462,
           'source.geolocation.cc': 'TW',
           'source.geolocation.city': 'TAOYUAN COUNTY',
           'source.geolocation.region': 'TAOYUAN CITY',
           'source.ip': '36.239.124.210',
           'source.port': 5555,
           'extra.name': 'hlteuc',
           'extra.model': 'SAMSUNG-SM-N900A',
           'extra.device': 'hlteatt',
          {'__type': 'Event',
           'feed.name': 'ShadowServer Accessible-ADB',
           'time.observation': '2018-07-30T00:00:00+00:00',
           'time.source': '2018-07-26T02:07:16+00:00'},
           'classification.taxonomy': 'vulnerable',
           'classification.type': 'vulnerable service',
           'classification.identifier': 'accessible-adb',
           'protocol.application': 'adb',
           'protocol.transport': 'tcp',
           'raw': utils.base64_encode('\n'.join([RECONSTRUCTED_LINES[0],
                                                 RECONSTRUCTED_LINES[2], ''])),
           'source.asn': 3462,
           'source.geolocation.cc': 'TW',
           'source.geolocation.city': 'TAIPEI CITY',
           'source.geolocation.region': 'TAIPEI',
           'source.ip': '36.236.108.107',
           'source.port': 5555,
           'extra.name': 'marlin',
           'extra.model': 'Pixel XL',
           'extra.device': 'marlin',
           'extra.features': 'cmd,shell_v2',
          ]


class TestShadowserverParserBot(test.BotTestCase, unittest.TestCase):
    """
    A TestCase for a ShadowserverParserBot.
    """

    @classmethod
    def set_bot(cls):
        cls.bot_reference = ShadowserverParserBot
        cls.default_input_message = EXAMPLE_REPORT
        cls.sysconfig = {'feedname': 'Accessible-ADB'}

    def test_event(self):
        """ Test if correct Event has been produced. """
        self.run_bot()
        for i, EVENT in enumerate(EVENTS):
            self.assertMessageEqual(i, EVENT)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()