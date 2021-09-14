from numpy import apply_along_axis
from sklearn.manifold import MDS

from ..array import normalize
from ..constant import RANDOM_SEED


def scale(di_po_po, n_di, ra=RANDOM_SEED, **ke_va):

    nu_po_di = MDS(
        n_components=n_di, random_state=ra, dissimilarity="precomputed", **ke_va
    ).fit_transform(di_po_po)

    return apply_along_axis(normalize, 0, nu_po_di, "0-1")