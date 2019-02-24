# -*- coding: utf-8 -*-

import numpy as np
from pycuda import gpuarray

"""Check for solution blowup in single-species systems"""
class DGFSNaNCheckBi():
    
    def __init__(self, cfg, cfgsect):

        self.nsteps = cfg.lookupint(cfgsect, 'nsteps')

    def __call__(self, tcurr, nsteps, sols):
        if nsteps % self.nsteps == 0: 
            if np.any([np.isnan(gpuarray.sum(v).get()) for v in sols]):
                raise RuntimeError('NaNs detected at t = {0}'
                                   .format(tcurr))  