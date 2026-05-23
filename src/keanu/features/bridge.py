import numpy as np
import inspect
import szxxx.common.tools as tools
from szxxx.features.features import FeaturesDto, Features
import shot.dataphora as dp

class KeanuDto(FeaturesDto):
    def __init__(self):
        super().__init__()
        self.FEATURES = self.BRID_, = ('brid_',)
        self.segment_len = 1
        self.dataphora = None

        if self.values_raw is not None:
            self.dataphora = dp.Bridge(
                timeshots=self.values_raw, 
                monotonic_duration=10, 
                vertical_range={dp.Direction.BWD: 150, dp.Direction.FWD: 100},
                snapshot_size={dp.Direction.BWD: 12, dp.Direction.FWD: 10},  
                adversity=0.5, sltp=90)
    
    def file_name(self):
        name = 'bridge;'
        for k, v in self.label.items():
            if not '#' in k:
                name += f'{k}-{v};'
        return name
 
    def get_segment(self, index=0):

# Here sequences of views are made. A view is a complete of features listed 
# in `self.FEATURES`. Views are grouped in sequences. 
# 
# Currently there is one element in the `self.FEATURES` list, namely 
# `self.BRID_`.

        if index + self.segment_len > len(self.data): 
            return None
        sequence, _ = self.dataphora.add_timeshot(self.data[index])

        return sequence
         
class Keanu(Features, KeanuDto):
    def __init__(self, data, warmup_len):
        super().__init__(data, warmup_len, pcs_var=0.05, msd_var=0.2,segment_size=None, index_step=1)
         
        self.dataphora = dp.Bridge(
                timeshots=self.data[:warmup_len], 
                monotonic_duration=10, 
                vertical_range={dp.Direction.BWD: 150, dp.Direction.FWD: 100},
                snapshot_size={dp.Direction.BWD: 12, dp.Direction.FWD: 10},  
                adversity=0.5, sltp=90)

        self.args = tools.args(inspect.currentframe()) 
        self.segment_len = 1
        self.label = { # keys with `#` char are not included in name
            'class#': 'bridge',
            'seg_size': self._segment_size,
        }

    def warmup_len(self):
        return self.ma_window

# python -m keanu.features.bridge
def main():
    from szxxx.common.hist_data import set_hist_data
    import szx81.config as config
    scope=(0, None)
    save = True
    prep = None

    # test
    scope=(0, 5000)
    save = True
    prep = '_test'

    warmup_len = 2*24*60 # warmup
    if len(scope) == 2:
        slice_ = slice(*(max(scope[0] - warmup_len, 0), scope[1]))
    else:
        slice_ = slice(*scope)

    DATA = set_hist_data(config=config)[slice_]
    Keanu.build_and_save(
        object = Keanu(
            data=DATA,
            warmup_len=warmup_len,
        ),
        save=save,
        prep=prep,
        verbose=True
    )

if __name__ == "__main__":
    main() 
