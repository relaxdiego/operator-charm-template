# Standard Library imports go here
import unittest
from unittest.mock import (
    patch
)

# Operator Frmework imports go here
from ops.testing import Harness

# Imports of your charm's modules go here
from src.charm import ChangeMeCharm


class ChangeMeCharmTest(unittest.TestCase):

    def setUp(self):
        self.harness = Harness(ChangeMeCharm)

    def test__init__runs_succesfully(self):
        # Setup
        harness = self.harness

        # Exercise
        harness.begin()

        # Assert
        # No assertions needed for this test

    @patch('src.charm.on_start_handler', spec_set=True, autospec=True)
    def test__on_start_delegator__calls_on_start_handler(self, mock_handler):
        # Setup
        harness = self.harness
        harness.disable_hooks()
        harness.add_oci_resource('changeme-image')
        harness.begin()

        # Exercise
        harness.charm.on.start.emit()

        # Assert
        assert mock_handler.call_count == 1


class OnStartHandlerTest(unittest.TestCase):

    def test_it_does_not_run_if_it_is_not_the_leader(self):
        pass
