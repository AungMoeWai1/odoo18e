import re

from odoo.tests import HttpCase


# This checksum is based on the contents of the scale related
# files (full list defined in controllers/checksum.py)
# Any change to these files will require re-certification with LNE.
# DO NOT CHANGE IT WITHOUT CONTACTING THE POS TEAM FIRST!
EXPECTED_CHECKSUM = "7b86e58ab7501124c3ac6ac0977a6ff8cf090268560791ffc1a1c51131c623e4"


class TestScaleChecksum(HttpCase):
    def test_checksum_matches_expected(self):
        self.authenticate("admin", "admin")

        response = self.url_open("/scale_checksum")
        self.assertEqual(response.status_code, 200)

        checksum_match = re.search(r"GLOBAL HASH: (\S+)", response.text)
        self.assertIsNotNone(checksum_match)
        self.assertEqual(checksum_match[1], EXPECTED_CHECKSUM)
