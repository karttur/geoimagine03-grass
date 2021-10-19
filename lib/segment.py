'''Wrapper for segment.h

Generated with:
./ctypesgen.py --cpp gcc -E -I/Applications/GRASS-7.8.app/Contents/Resources/include  -D_Nullable=     -I/Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include -I/Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include -D__GLIBC_HAVE_LONG_LONG -lgrass_segment.7.8 /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/segment.h /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/segment.h -o OBJ.x86_64-apple-darwin18.7.0/segment.py

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

_libs["grass_segment.7.8"] = load_library("grass_segment.7.8")

# 1 libraries
# End libraries

# No modules

__int64_t = c_longlong # /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 46

__darwin_off_t = __int64_t # /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 71

off_t = __darwin_off_t # /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_off_t.h: 31

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/segment.h: 14
class struct_aq(Structure):
    pass

struct_aq.__slots__ = [
    'cur',
    'younger',
    'older',
]
struct_aq._fields_ = [
    ('cur', c_int),
    ('younger', POINTER(struct_aq)),
    ('older', POINTER(struct_aq)),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/segment.h: 45
class struct_scb(Structure):
    pass

struct_scb.__slots__ = [
    'buf',
    'dirty',
    'age',
    'n',
]
struct_scb._fields_ = [
    ('buf', String),
    ('dirty', c_char),
    ('age', POINTER(struct_aq)),
    ('n', c_int),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/segment.h: 63
class struct_anon_7(Structure):
    pass

struct_anon_7.__slots__ = [
    'open',
    'nrows',
    'ncols',
    'len',
    'srows',
    'scols',
    'srowscols',
    'size',
    'spr',
    'spill',
    'fast_adrs',
    'scolbits',
    'srowbits',
    'segbits',
    'fast_seek',
    'lenbits',
    'sizebits',
    'address',
    'seek',
    'fname',
    'fd',
    'scb',
    'load_idx',
    'nfreeslots',
    'freeslot',
    'agequeue',
    'youngest',
    'oldest',
    'nseg',
    'cur',
    'offset',
    'cache',
]
struct_anon_7._fields_ = [
    ('open', c_int),
    ('nrows', off_t),
    ('ncols', off_t),
    ('len', c_int),
    ('srows', c_int),
    ('scols', c_int),
    ('srowscols', c_int),
    ('size', c_int),
    ('spr', c_int),
    ('spill', c_int),
    ('fast_adrs', c_int),
    ('scolbits', off_t),
    ('srowbits', off_t),
    ('segbits', off_t),
    ('fast_seek', c_int),
    ('lenbits', c_int),
    ('sizebits', c_int),
    ('address', CFUNCTYPE(UNCHECKED(c_int), )),
    ('seek', CFUNCTYPE(UNCHECKED(c_int), )),
    ('fname', String),
    ('fd', c_int),
    ('scb', POINTER(struct_scb)),
    ('load_idx', POINTER(c_int)),
    ('nfreeslots', c_int),
    ('freeslot', POINTER(c_int)),
    ('agequeue', POINTER(struct_aq)),
    ('youngest', POINTER(struct_aq)),
    ('oldest', POINTER(struct_aq)),
    ('nseg', c_int),
    ('cur', c_int),
    ('offset', c_int),
    ('cache', String),
]

SEGMENT = struct_anon_7 # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/segment.h: 63

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/segment.h: 4
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_open'):
        continue
    Segment_open = _lib.Segment_open
    Segment_open.argtypes = [POINTER(SEGMENT), String, off_t, off_t, c_int, c_int, c_int, c_int]
    Segment_open.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/segment.h: 5
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_close'):
        continue
    Segment_close = _lib.Segment_close
    Segment_close.argtypes = [POINTER(SEGMENT)]
    Segment_close.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/segment.h: 6
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_flush'):
        continue
    Segment_flush = _lib.Segment_flush
    Segment_flush.argtypes = [POINTER(SEGMENT)]
    Segment_flush.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/segment.h: 7
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_format'):
        continue
    Segment_format = _lib.Segment_format
    Segment_format.argtypes = [c_int, off_t, off_t, c_int, c_int, c_int]
    Segment_format.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/segment.h: 8
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_format_nofill'):
        continue
    Segment_format_nofill = _lib.Segment_format_nofill
    Segment_format_nofill.argtypes = [c_int, off_t, off_t, c_int, c_int, c_int]
    Segment_format_nofill.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/segment.h: 9
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_get'):
        continue
    Segment_get = _lib.Segment_get
    Segment_get.argtypes = [POINTER(SEGMENT), POINTER(None), off_t, off_t]
    Segment_get.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/segment.h: 10
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_get_row'):
        continue
    Segment_get_row = _lib.Segment_get_row
    Segment_get_row.argtypes = [POINTER(SEGMENT), POINTER(None), off_t]
    Segment_get_row.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/segment.h: 11
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_init'):
        continue
    Segment_init = _lib.Segment_init
    Segment_init.argtypes = [POINTER(SEGMENT), c_int, c_int]
    Segment_init.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/segment.h: 12
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_put'):
        continue
    Segment_put = _lib.Segment_put
    Segment_put.argtypes = [POINTER(SEGMENT), POINTER(None), off_t, off_t]
    Segment_put.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/segment.h: 13
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_put_row'):
        continue
    Segment_put_row = _lib.Segment_put_row
    Segment_put_row.argtypes = [POINTER(SEGMENT), POINTER(None), off_t]
    Segment_put_row.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/segment.h: 14
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Segment_release'):
        continue
    Segment_release = _lib.Segment_release
    Segment_release.argtypes = [POINTER(SEGMENT)]
    Segment_release.restype = c_int
    break

aq = struct_aq # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/segment.h: 14

scb = struct_scb # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/segment.h: 45

# No inserted files

