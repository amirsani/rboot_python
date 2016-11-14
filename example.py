
import rboot
import numpy as np

bs_series = rboot.replacement_bootstrap(np.random.randn(100), bootstraps=100, seed=1978, replacement_percentage=0.25, replace=False, rho=0.10)