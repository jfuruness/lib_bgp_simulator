from pathlib import Path

import pytest

from .engine_test_configs import Config001
from .engine_test_configs import Config002
from .engine_test_configs import Config011, Config012
from .engine_test_configs import Config013, Config014
from .engine_test_configs import Config015, Config016, Config017, Config018
from .engine_test_configs import Config019, Config020, Config021, Config022
from .engine_test_configs import Config023, Config024, Config025, Config026
from .utils import EngineTester
from .utils import EngineTestConfig


class TestEngine:
    """Performs a system test on the engine

    See README for in depth details
    """

    @pytest.mark.parametrize("conf",
    #                         [Cls() for Cls in EngineTestConfig.subclasses])
                             [Config001, Config002, Config011, Config012,
                              Config013, Config014, Config015, Config016,
                              Config017, Config018, Config019, Config020,
                              Config021, Config022, Config023, Config024,
                              Config025, Config026])
    def test_engine(self, conf: EngineTestConfig, overwrite: bool):
        """Performs a system test on the engine

        See README for in depth details
        """

        EngineTester(base_dir=self.base_dir,
                     conf=conf,
                     overwrite=overwrite).test_engine()

    @property
    def base_dir(self) -> Path:
        """Returns test output dir"""

        return Path(__file__).parent / "engine_test_outputs"
