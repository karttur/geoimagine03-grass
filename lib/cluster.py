'''Wrapper for cluster.h

Generated with:
./ctypesgen.py --cpp gcc -E -I/Applications/GRASS-7.8.app/Contents/Resources/include  -D_Nullable=     -I/Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include -I/Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include -D__GLIBC_HAVE_LONG_LONG -lgrass_cluster.7.8 /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/cluster.h /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h -o OBJ.x86_64-apple-darwin18.7.0/cluster.py

Do not modify this file.
'''

__docformat__ = 'restructuredtext'


_libs = {}
_libdirs = []

from .ctypes_preamble import *
from .ctypes_preamble import _variadic_function
from .ctypes_loader import *

add_library_search_dirs([])

# Begin libraries

_libs["grass_cluster.7.8"] = load_library("grass_cluster.7.8")

# 1 libraries
# End libraries

# No modules

DCELL = c_double # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/gis.h: 596

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/imagery.h: 52
class struct_One_Sig(Structure):
    pass

struct_One_Sig.__slots__ = [
    'desc',
    'npoints',
    'mean',
    'var',
    'status',
    'r',
    'g',
    'b',
    'have_color',
]
struct_One_Sig._fields_ = [
    ('desc', c_char * 100),
    ('npoints', c_int),
    ('mean', POINTER(c_double)),
    ('var', POINTER(POINTER(c_double))),
    ('status', c_int),
    ('r', c_float),
    ('g', c_float),
    ('b', c_float),
    ('have_color', c_int),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/imagery.h: 63
class struct_Signature(Structure):
    pass

struct_Signature.__slots__ = [
    'nbands',
    'nsigs',
    'title',
    'sig',
]
struct_Signature._fields_ = [
    ('nbands', c_int),
    ('nsigs', c_int),
    ('title', c_char * 100),
    ('sig', POINTER(struct_One_Sig)),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/cluster.h: 7
class struct_Cluster(Structure):
    pass

struct_Cluster.__slots__ = [
    'nbands',
    'npoints',
    'points',
    'np',
    'band_sum',
    'band_sum2',
    '_class',
    'reclass',
    'count',
    'countdiff',
    'sum',
    'sumdiff',
    'sum2',
    'mean',
    'S',
    'nclasses',
    'merge1',
    'merge2',
    'iteration',
    'percent_stable',
]
struct_Cluster._fields_ = [
    ('nbands', c_int),
    ('npoints', c_int),
    ('points', POINTER(POINTER(DCELL))),
    ('np', c_int),
    ('band_sum', POINTER(c_double)),
    ('band_sum2', POINTER(c_double)),
    ('_class', POINTER(c_int)),
    ('reclass', POINTER(c_int)),
    ('count', POINTER(c_int)),
    ('countdiff', POINTER(c_int)),
    ('sum', POINTER(POINTER(c_double))),
    ('sumdiff', POINTER(POINTER(c_double))),
    ('sum2', POINTER(POINTER(c_double))),
    ('mean', POINTER(POINTER(c_double))),
    ('S', struct_Signature),
    ('nclasses', c_int),
    ('merge1', c_int),
    ('merge2', c_int),
    ('iteration', c_int),
    ('percent_stable', c_double),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 5
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_assign'):
        continue
    I_cluster_assign = _lib.I_cluster_assign
    I_cluster_assign.argtypes = [POINTER(struct_Cluster), POINTER(c_int)]
    I_cluster_assign.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 8
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_begin'):
        continue
    I_cluster_begin = _lib.I_cluster_begin
    I_cluster_begin.argtypes = [POINTER(struct_Cluster), c_int]
    I_cluster_begin.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 11
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_clear'):
        continue
    I_cluster_clear = _lib.I_cluster_clear
    I_cluster_clear.argtypes = [POINTER(struct_Cluster)]
    I_cluster_clear.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 14
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_distinct'):
        continue
    I_cluster_distinct = _lib.I_cluster_distinct
    I_cluster_distinct.argtypes = [POINTER(struct_Cluster), c_double]
    I_cluster_distinct.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 17
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_exec'):
        continue
    I_cluster_exec = _lib.I_cluster_exec
    I_cluster_exec.argtypes = [POINTER(struct_Cluster), c_int, c_int, c_double, c_double, c_int, CFUNCTYPE(UNCHECKED(c_int), ), POINTER(c_int)]
    I_cluster_exec.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 20
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_exec_allocate'):
        continue
    I_cluster_exec_allocate = _lib.I_cluster_exec_allocate
    I_cluster_exec_allocate.argtypes = [POINTER(struct_Cluster)]
    I_cluster_exec_allocate.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 21
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_exec_free'):
        continue
    I_cluster_exec_free = _lib.I_cluster_exec_free
    I_cluster_exec_free.argtypes = [POINTER(struct_Cluster)]
    I_cluster_exec_free.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 24
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_means'):
        continue
    I_cluster_means = _lib.I_cluster_means
    I_cluster_means.argtypes = [POINTER(struct_Cluster)]
    I_cluster_means.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 27
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_merge'):
        continue
    I_cluster_merge = _lib.I_cluster_merge
    I_cluster_merge.argtypes = [POINTER(struct_Cluster)]
    I_cluster_merge.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 30
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_nclasses'):
        continue
    I_cluster_nclasses = _lib.I_cluster_nclasses
    I_cluster_nclasses.argtypes = [POINTER(struct_Cluster), c_int]
    I_cluster_nclasses.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 33
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_point'):
        continue
    I_cluster_point = _lib.I_cluster_point
    I_cluster_point.argtypes = [POINTER(struct_Cluster), POINTER(DCELL)]
    I_cluster_point.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 34
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_begin_point_set'):
        continue
    I_cluster_begin_point_set = _lib.I_cluster_begin_point_set
    I_cluster_begin_point_set.argtypes = [POINTER(struct_Cluster), c_int]
    I_cluster_begin_point_set.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 35
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_point_part'):
        continue
    I_cluster_point_part = _lib.I_cluster_point_part
    I_cluster_point_part.argtypes = [POINTER(struct_Cluster), DCELL, c_int, c_int]
    I_cluster_point_part.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 36
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_end_point_set'):
        continue
    I_cluster_end_point_set = _lib.I_cluster_end_point_set
    I_cluster_end_point_set.argtypes = [POINTER(struct_Cluster), c_int]
    I_cluster_end_point_set.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 39
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_reassign'):
        continue
    I_cluster_reassign = _lib.I_cluster_reassign
    I_cluster_reassign.argtypes = [POINTER(struct_Cluster), POINTER(c_int)]
    I_cluster_reassign.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 42
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_reclass'):
        continue
    I_cluster_reclass = _lib.I_cluster_reclass
    I_cluster_reclass.argtypes = [POINTER(struct_Cluster), c_int]
    I_cluster_reclass.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 45
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_separation'):
        continue
    I_cluster_separation = _lib.I_cluster_separation
    I_cluster_separation.argtypes = [POINTER(struct_Cluster), c_int, c_int]
    I_cluster_separation.restype = c_double
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 48
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_signatures'):
        continue
    I_cluster_signatures = _lib.I_cluster_signatures
    I_cluster_signatures.argtypes = [POINTER(struct_Cluster)]
    I_cluster_signatures.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/cluster.h: 51
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'I_cluster_sum2'):
        continue
    I_cluster_sum2 = _lib.I_cluster_sum2
    I_cluster_sum2.argtypes = [POINTER(struct_Cluster)]
    I_cluster_sum2.restype = c_int
    break

Cluster = struct_Cluster # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/cluster.h: 7

# No inserted files

