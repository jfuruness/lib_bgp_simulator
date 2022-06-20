import time
import csv
import os
import sys
from pathlib import Path
from datetime import datetime

from lib_bgp_simulator.simulator import Simulator
from lib_bgp_simulator.simulator.graph.graph import Graph
from lib_bgp_simulator.simulator.mp_method import MPMethod
from lib_bgp_simulator.engine import BGPAS
from lib_bgp_simulator.engine import ROVAS
from lib_bgp_simulator.engine_input import SubprefixHijack


class Settings:
    """
    Just a convenient class to capture the settings of the
    benchmark simulator being run.
    """
    def __init__(self,
                 percent_adoptions=[0, 5, 10, 20, 30, 60, 80, 100],
                 adopt_as_classes=[ROVAS],
                 EngineInputCls=SubprefixHijack,
                 num_trials=1,
                 BaseASCls=BGPAS,
                 mp_method=MPMethod.SINGLE_PROCESS):
        self.percent_adoptions = percent_adoptions
        self.adopt_as_classes = adopt_as_classes
        self.EngineInputCls = EngineInputCls
        self.num_trials = num_trials
        self.BaseASCls = BaseASCls
        self.mp_method = mp_method

    def as_dict(self):
        adict = {
            'percent_adoptions': str(self.percent_adoptions),
            'adopt_as_classes': str(self.adopt_as_classes),
            'EngineInputCls': str(self.EngineInputCls),
            'num_trials': str(self.num_trials),
            'BaseASCls': str(self.BaseASCls),
            'mp_method': str(self.mp_method)
        }
        return adict



def main(benchmark_settings):
    settings = benchmark_settings
    Simulator.run(
                graphs=[Graph(percent_adoptions=settings.percent_adoptions,
                              adopt_as_classes=settings.adopt_as_classes,
                              EngineInputCls=settings.EngineInputCls,
                              num_trials=settings.num_trials,
                              BaseASCls=settings.BaseASCls)],
                graph_path=Path("/tmp/benchmark_graphs.tar.gz"),
                mp_method=settings.mp_method,
    )

if __name__ == '__main__':
    # Track some run time information and print to stdout
    # Track when this was computed
    timestamp = datetime.now().isoformat()
    tsv_start_time = time.perf_counter()
    print("Start Time: ", timestamp)

    # Running Main
    # -----------------------------------------------------------
    settings = Settings()
    main()
    # -----------------------------------------------------------

    # Capture runtime and share with stdout
    runtime = time.perf_counter() - tsv_start_time
    print("End Time: ", datetime.now().isoformat())
    print("Elapsed Time: ", time.perf_counter() - tsv_start_time)
    print("Writing benchmark results to TSV")

    # Check if a tag for this benchmark was provided
    tag = None
    if len(sys.argv) == 2:
        tag = sys.argv[1]

    # Save the results of the benchmark to TSV
    with open('benchmark_results.tsv', 'a') as tsvfile:
        fieldnames = ['machine_name', 'timestamp', 'runtime', 'tag', 'mp_method',
                      'num_trials', 'adopt_as_classes', 'engine']
        writer = csv.DictWriter(tsvfile, delimiter='\t', fieldnames=fieldnames)
        # Get the benchmark settings
        settings_dict = settings.as_dict()
        row = {
            'machine_name': os.uname().nodename,
            'timestamp': timestamp,
            'runtime': runtime,
            'tag': tag,
            'mp_method': settings_dict.mp_method,
            'num_trials': settings_dict.num_trials,
            'adopt_as_classes': settings_dict.adopt_as_classes,
            'engine': settings_dict.EngineInputCls
        }
        writer.writerow(row)
    print("Results written")
