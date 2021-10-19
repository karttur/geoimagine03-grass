'''Wrapper for datetime.h

Generated with:
./ctypesgen.py --cpp gcc -E -I/Applications/GRASS-7.8.app/Contents/Resources/include  -D_Nullable=     -I/Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include -I/Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include -D__GLIBC_HAVE_LONG_LONG -lgrass_datetime.7.8 /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/datetime.h /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h -o OBJ.x86_64-apple-darwin18.7.0/date.py

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

_libs["grass_datetime.7.8"] = load_library("grass_datetime.7.8")

# 1 libraries
# End libraries

# No modules

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/datetime.h: 27
class struct_DateTime(Structure):
    pass

struct_DateTime.__slots__ = [
    'mode',
    '_from',
    'to',
    'fracsec',
    'year',
    'month',
    'day',
    'hour',
    'minute',
    'second',
    'positive',
    'tz',
]
struct_DateTime._fields_ = [
    ('mode', c_int),
    ('_from', c_int),
    ('to', c_int),
    ('fracsec', c_int),
    ('year', c_int),
    ('month', c_int),
    ('day', c_int),
    ('hour', c_int),
    ('minute', c_int),
    ('second', c_double),
    ('positive', c_int),
    ('tz', c_int),
]

DateTime = struct_DateTime # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/datetime.h: 27

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 5
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_is_between'):
        continue
    datetime_is_between = _lib.datetime_is_between
    datetime_is_between.argtypes = [c_int, c_int, c_int]
    datetime_is_between.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 8
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_change_from_to'):
        continue
    datetime_change_from_to = _lib.datetime_change_from_to
    datetime_change_from_to.argtypes = [POINTER(DateTime), c_int, c_int, c_int]
    datetime_change_from_to.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 11
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_copy'):
        continue
    datetime_copy = _lib.datetime_copy
    datetime_copy.argtypes = [POINTER(DateTime), POINTER(DateTime)]
    datetime_copy.restype = None
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 14
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_difference'):
        continue
    datetime_difference = _lib.datetime_difference
    datetime_difference.argtypes = [POINTER(DateTime), POINTER(DateTime), POINTER(DateTime)]
    datetime_difference.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 18
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_error'):
        continue
    datetime_error = _lib.datetime_error
    datetime_error.argtypes = [c_int, String]
    datetime_error.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 19
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_error_code'):
        continue
    datetime_error_code = _lib.datetime_error_code
    datetime_error_code.argtypes = []
    datetime_error_code.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 20
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_error_msg'):
        continue
    datetime_error_msg = _lib.datetime_error_msg
    datetime_error_msg.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        datetime_error_msg.restype = ReturnString
    else:
        datetime_error_msg.restype = String
        datetime_error_msg.errcheck = ReturnString
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 21
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_clear_error'):
        continue
    datetime_clear_error = _lib.datetime_clear_error
    datetime_clear_error.argtypes = []
    datetime_clear_error.restype = None
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 24
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_format'):
        continue
    datetime_format = _lib.datetime_format
    datetime_format.argtypes = [POINTER(DateTime), String]
    datetime_format.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 27
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_increment'):
        continue
    datetime_increment = _lib.datetime_increment
    datetime_increment.argtypes = [POINTER(DateTime), POINTER(DateTime)]
    datetime_increment.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 30
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_is_valid_increment'):
        continue
    datetime_is_valid_increment = _lib.datetime_is_valid_increment
    datetime_is_valid_increment.argtypes = [POINTER(DateTime), POINTER(DateTime)]
    datetime_is_valid_increment.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 31
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_check_increment'):
        continue
    datetime_check_increment = _lib.datetime_check_increment
    datetime_check_increment.argtypes = [POINTER(DateTime), POINTER(DateTime)]
    datetime_check_increment.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 34
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_get_increment_type'):
        continue
    datetime_get_increment_type = _lib.datetime_get_increment_type
    datetime_get_increment_type.argtypes = [POINTER(DateTime), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    datetime_get_increment_type.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 36
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_set_increment_type'):
        continue
    datetime_set_increment_type = _lib.datetime_set_increment_type
    datetime_set_increment_type.argtypes = [POINTER(DateTime), POINTER(DateTime)]
    datetime_set_increment_type.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 39
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_get_local_timezone'):
        continue
    datetime_get_local_timezone = _lib.datetime_get_local_timezone
    datetime_get_local_timezone.argtypes = [POINTER(c_int)]
    datetime_get_local_timezone.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 40
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_get_local_time'):
        continue
    datetime_get_local_time = _lib.datetime_get_local_time
    datetime_get_local_time.argtypes = [POINTER(DateTime)]
    datetime_get_local_time.restype = None
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 43
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_days_in_month'):
        continue
    datetime_days_in_month = _lib.datetime_days_in_month
    datetime_days_in_month.argtypes = [c_int, c_int, c_int]
    datetime_days_in_month.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 44
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_is_leap_year'):
        continue
    datetime_is_leap_year = _lib.datetime_is_leap_year
    datetime_is_leap_year.argtypes = [c_int, c_int]
    datetime_is_leap_year.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 45
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_days_in_year'):
        continue
    datetime_days_in_year = _lib.datetime_days_in_year
    datetime_days_in_year.argtypes = [c_int, c_int]
    datetime_days_in_year.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 48
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_is_same'):
        continue
    datetime_is_same = _lib.datetime_is_same
    datetime_is_same.argtypes = [POINTER(DateTime), POINTER(DateTime)]
    datetime_is_same.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 51
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_scan'):
        continue
    datetime_scan = _lib.datetime_scan
    datetime_scan.argtypes = [POINTER(DateTime), String]
    datetime_scan.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 54
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_is_positive'):
        continue
    datetime_is_positive = _lib.datetime_is_positive
    datetime_is_positive.argtypes = [POINTER(DateTime)]
    datetime_is_positive.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 55
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_is_negative'):
        continue
    datetime_is_negative = _lib.datetime_is_negative
    datetime_is_negative.argtypes = [POINTER(DateTime)]
    datetime_is_negative.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 56
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_set_positive'):
        continue
    datetime_set_positive = _lib.datetime_set_positive
    datetime_set_positive.argtypes = [POINTER(DateTime)]
    datetime_set_positive.restype = None
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 57
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_set_negative'):
        continue
    datetime_set_negative = _lib.datetime_set_negative
    datetime_set_negative.argtypes = [POINTER(DateTime)]
    datetime_set_negative.restype = None
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 58
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_invert_sign'):
        continue
    datetime_invert_sign = _lib.datetime_invert_sign
    datetime_invert_sign.argtypes = [POINTER(DateTime)]
    datetime_invert_sign.restype = None
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 61
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_set_type'):
        continue
    datetime_set_type = _lib.datetime_set_type
    datetime_set_type.argtypes = [POINTER(DateTime), c_int, c_int, c_int, c_int]
    datetime_set_type.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 62
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_get_type'):
        continue
    datetime_get_type = _lib.datetime_get_type
    datetime_get_type.argtypes = [POINTER(DateTime), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    datetime_get_type.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 64
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_is_valid_type'):
        continue
    datetime_is_valid_type = _lib.datetime_is_valid_type
    datetime_is_valid_type.argtypes = [POINTER(DateTime)]
    datetime_is_valid_type.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 65
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_check_type'):
        continue
    datetime_check_type = _lib.datetime_check_type
    datetime_check_type.argtypes = [POINTER(DateTime)]
    datetime_check_type.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 66
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_in_interval_year_month'):
        continue
    datetime_in_interval_year_month = _lib.datetime_in_interval_year_month
    datetime_in_interval_year_month.argtypes = [c_int]
    datetime_in_interval_year_month.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 67
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_in_interval_day_second'):
        continue
    datetime_in_interval_day_second = _lib.datetime_in_interval_day_second
    datetime_in_interval_day_second.argtypes = [c_int]
    datetime_in_interval_day_second.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 68
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_is_absolute'):
        continue
    datetime_is_absolute = _lib.datetime_is_absolute
    datetime_is_absolute.argtypes = [POINTER(DateTime)]
    datetime_is_absolute.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 69
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_is_relative'):
        continue
    datetime_is_relative = _lib.datetime_is_relative
    datetime_is_relative.argtypes = [POINTER(DateTime)]
    datetime_is_relative.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 72
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_check_timezone'):
        continue
    datetime_check_timezone = _lib.datetime_check_timezone
    datetime_check_timezone.argtypes = [POINTER(DateTime), c_int]
    datetime_check_timezone.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 73
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_get_timezone'):
        continue
    datetime_get_timezone = _lib.datetime_get_timezone
    datetime_get_timezone.argtypes = [POINTER(DateTime), POINTER(c_int)]
    datetime_get_timezone.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 74
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_set_timezone'):
        continue
    datetime_set_timezone = _lib.datetime_set_timezone
    datetime_set_timezone.argtypes = [POINTER(DateTime), c_int]
    datetime_set_timezone.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 75
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_unset_timezone'):
        continue
    datetime_unset_timezone = _lib.datetime_unset_timezone
    datetime_unset_timezone.argtypes = [POINTER(DateTime)]
    datetime_unset_timezone.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 76
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_is_valid_timezone'):
        continue
    datetime_is_valid_timezone = _lib.datetime_is_valid_timezone
    datetime_is_valid_timezone.argtypes = [c_int]
    datetime_is_valid_timezone.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 79
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_change_timezone'):
        continue
    datetime_change_timezone = _lib.datetime_change_timezone
    datetime_change_timezone.argtypes = [POINTER(DateTime), c_int]
    datetime_change_timezone.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 80
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_change_to_utc'):
        continue
    datetime_change_to_utc = _lib.datetime_change_to_utc
    datetime_change_to_utc.argtypes = [POINTER(DateTime)]
    datetime_change_to_utc.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 81
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_decompose_timezone'):
        continue
    datetime_decompose_timezone = _lib.datetime_decompose_timezone
    datetime_decompose_timezone.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]
    datetime_decompose_timezone.restype = None
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 84
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_check_year'):
        continue
    datetime_check_year = _lib.datetime_check_year
    datetime_check_year.argtypes = [POINTER(DateTime), c_int]
    datetime_check_year.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 85
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_check_month'):
        continue
    datetime_check_month = _lib.datetime_check_month
    datetime_check_month.argtypes = [POINTER(DateTime), c_int]
    datetime_check_month.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 86
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_check_day'):
        continue
    datetime_check_day = _lib.datetime_check_day
    datetime_check_day.argtypes = [POINTER(DateTime), c_int]
    datetime_check_day.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 87
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_check_hour'):
        continue
    datetime_check_hour = _lib.datetime_check_hour
    datetime_check_hour.argtypes = [POINTER(DateTime), c_int]
    datetime_check_hour.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 88
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_check_minute'):
        continue
    datetime_check_minute = _lib.datetime_check_minute
    datetime_check_minute.argtypes = [POINTER(DateTime), c_int]
    datetime_check_minute.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 89
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_check_second'):
        continue
    datetime_check_second = _lib.datetime_check_second
    datetime_check_second.argtypes = [POINTER(DateTime), c_double]
    datetime_check_second.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 90
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_check_fracsec'):
        continue
    datetime_check_fracsec = _lib.datetime_check_fracsec
    datetime_check_fracsec.argtypes = [POINTER(DateTime), c_int]
    datetime_check_fracsec.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 91
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_get_year'):
        continue
    datetime_get_year = _lib.datetime_get_year
    datetime_get_year.argtypes = [POINTER(DateTime), POINTER(c_int)]
    datetime_get_year.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 92
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_set_year'):
        continue
    datetime_set_year = _lib.datetime_set_year
    datetime_set_year.argtypes = [POINTER(DateTime), c_int]
    datetime_set_year.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 93
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_get_month'):
        continue
    datetime_get_month = _lib.datetime_get_month
    datetime_get_month.argtypes = [POINTER(DateTime), POINTER(c_int)]
    datetime_get_month.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 94
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_set_month'):
        continue
    datetime_set_month = _lib.datetime_set_month
    datetime_set_month.argtypes = [POINTER(DateTime), c_int]
    datetime_set_month.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 95
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_get_day'):
        continue
    datetime_get_day = _lib.datetime_get_day
    datetime_get_day.argtypes = [POINTER(DateTime), POINTER(c_int)]
    datetime_get_day.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 96
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_set_day'):
        continue
    datetime_set_day = _lib.datetime_set_day
    datetime_set_day.argtypes = [POINTER(DateTime), c_int]
    datetime_set_day.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 97
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_get_hour'):
        continue
    datetime_get_hour = _lib.datetime_get_hour
    datetime_get_hour.argtypes = [POINTER(DateTime), POINTER(c_int)]
    datetime_get_hour.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 98
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_set_hour'):
        continue
    datetime_set_hour = _lib.datetime_set_hour
    datetime_set_hour.argtypes = [POINTER(DateTime), c_int]
    datetime_set_hour.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 99
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_get_minute'):
        continue
    datetime_get_minute = _lib.datetime_get_minute
    datetime_get_minute.argtypes = [POINTER(DateTime), POINTER(c_int)]
    datetime_get_minute.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 100
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_set_minute'):
        continue
    datetime_set_minute = _lib.datetime_set_minute
    datetime_set_minute.argtypes = [POINTER(DateTime), c_int]
    datetime_set_minute.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 101
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_get_second'):
        continue
    datetime_get_second = _lib.datetime_get_second
    datetime_get_second.argtypes = [POINTER(DateTime), POINTER(c_double)]
    datetime_get_second.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 102
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_set_second'):
        continue
    datetime_set_second = _lib.datetime_set_second
    datetime_set_second.argtypes = [POINTER(DateTime), c_double]
    datetime_set_second.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 103
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_get_fracsec'):
        continue
    datetime_get_fracsec = _lib.datetime_get_fracsec
    datetime_get_fracsec.argtypes = [POINTER(DateTime), POINTER(c_int)]
    datetime_get_fracsec.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/datetime.h: 104
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'datetime_set_fracsec'):
        continue
    datetime_set_fracsec = _lib.datetime_set_fracsec
    datetime_set_fracsec.argtypes = [POINTER(DateTime), c_int]
    datetime_set_fracsec.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/datetime.h: 4
try:
    DATETIME_ABSOLUTE = 1
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/datetime.h: 5
try:
    DATETIME_RELATIVE = 2
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/datetime.h: 10
try:
    DATETIME_YEAR = 101
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/datetime.h: 11
try:
    DATETIME_MONTH = 102
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/datetime.h: 12
try:
    DATETIME_DAY = 103
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/datetime.h: 13
try:
    DATETIME_HOUR = 104
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/datetime.h: 14
try:
    DATETIME_MINUTE = 105
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/datetime.h: 15
try:
    DATETIME_SECOND = 106
except:
    pass

DateTime = struct_DateTime # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/datetime.h: 27

# No inserted files

