'''Wrapper for vedit.h

Generated with:
./ctypesgen.py --cpp gcc -E -I/Applications/GRASS-7.8.app/Contents/Resources/include  -D_Nullable=     -I/Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include -I/Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include -D__GLIBC_HAVE_LONG_LONG -lgrass_vedit.7.8 -I/Applications/GRASS-7.8.app/Contents/Resources/include -I/Applications/GRASS-7.8.app/Contents/Resources/include /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h -o OBJ.x86_64-apple-darwin18.7.0/vedit.py

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

_libs["grass_vedit.7.8"] = load_library("grass_vedit.7.8")

# 1 libraries
# End libraries

# No modules

__int64_t = c_longlong # /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/i386/_types.h: 46

__darwin_off_t = __int64_t # /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types.h: 71

fpos_t = __darwin_off_t # /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_stdio.h: 81

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_stdio.h: 92
class struct___sbuf(Structure):
    pass

struct___sbuf.__slots__ = [
    '_base',
    '_size',
]
struct___sbuf._fields_ = [
    ('_base', POINTER(c_ubyte)),
    ('_size', c_int),
]

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_stdio.h: 98
class struct___sFILEX(Structure):
    pass

# /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_stdio.h: 157
class struct___sFILE(Structure):
    pass

struct___sFILE.__slots__ = [
    '_p',
    '_r',
    '_w',
    '_flags',
    '_file',
    '_bf',
    '_lbfsize',
    '_cookie',
    '_close',
    '_read',
    '_seek',
    '_write',
    '_ub',
    '_extra',
    '_ur',
    '_ubuf',
    '_nbuf',
    '_lb',
    '_blksize',
    '_offset',
]
struct___sFILE._fields_ = [
    ('_p', POINTER(c_ubyte)),
    ('_r', c_int),
    ('_w', c_int),
    ('_flags', c_short),
    ('_file', c_short),
    ('_bf', struct___sbuf),
    ('_lbfsize', c_int),
    ('_cookie', POINTER(None)),
    ('_close', CFUNCTYPE(UNCHECKED(c_int), POINTER(None))),
    ('_read', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), String, c_int)),
    ('_seek', CFUNCTYPE(UNCHECKED(fpos_t), POINTER(None), fpos_t, c_int)),
    ('_write', CFUNCTYPE(UNCHECKED(c_int), POINTER(None), String, c_int)),
    ('_ub', struct___sbuf),
    ('_extra', POINTER(struct___sFILEX)),
    ('_ur', c_int),
    ('_ubuf', c_ubyte * 3),
    ('_nbuf', c_ubyte * 1),
    ('_lb', struct___sbuf),
    ('_blksize', c_int),
    ('_offset', fpos_t),
]

FILE = struct___sFILE # /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/_stdio.h: 157

off_t = __darwin_off_t # /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/sys/_types/_off_t.h: 31

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/gis.h: 682
class struct_ilist(Structure):
    pass

struct_ilist.__slots__ = [
    'value',
    'n_values',
    'alloc_values',
]
struct_ilist._fields_ = [
    ('value', POINTER(c_int)),
    ('n_values', c_int),
    ('alloc_values', c_int),
]

enum_anon_7 = c_int # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_defines.h: 257

SF_FeatureType = enum_anon_7 # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_defines.h: 257

dglByte_t = c_ubyte # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/type.h: 36

dglInt32_t = c_long # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/type.h: 37

dglInt64_t = c_longlong # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/type.h: 38

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/heap.h: 33
class union__dglHeapData(Union):
    pass

union__dglHeapData.__slots__ = [
    'pv',
    'n',
    'un',
    'l',
    'ul',
]
union__dglHeapData._fields_ = [
    ('pv', POINTER(None)),
    ('n', c_int),
    ('un', c_uint),
    ('l', c_long),
    ('ul', c_ulong),
]

dglHeapData_u = union__dglHeapData # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/heap.h: 33

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/heap.h: 42
class struct__dglHeapNode(Structure):
    pass

struct__dglHeapNode.__slots__ = [
    'key',
    'value',
    'flags',
]
struct__dglHeapNode._fields_ = [
    ('key', c_long),
    ('value', dglHeapData_u),
    ('flags', c_ubyte),
]

dglHeapNode_s = struct__dglHeapNode # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/heap.h: 42

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/heap.h: 52
class struct__dglHeap(Structure):
    pass

struct__dglHeap.__slots__ = [
    'index',
    'count',
    'block',
    'pnode',
]
struct__dglHeap._fields_ = [
    ('index', c_long),
    ('count', c_long),
    ('block', c_long),
    ('pnode', POINTER(dglHeapNode_s)),
]

dglHeap_s = struct__dglHeap # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/heap.h: 52

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/tree.h: 164
class struct__dglTreeEdgePri32(Structure):
    pass

struct__dglTreeEdgePri32.__slots__ = [
    'nKey',
    'cnData',
    'pnData',
]
struct__dglTreeEdgePri32._fields_ = [
    ('nKey', dglInt32_t),
    ('cnData', dglInt32_t),
    ('pnData', POINTER(dglInt32_t)),
]

dglTreeEdgePri32_s = struct__dglTreeEdgePri32 # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/tree.h: 164

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/graph.h: 135
class struct_anon_8(Structure):
    pass

struct_anon_8.__slots__ = [
    'pvAVL',
]
struct_anon_8._fields_ = [
    ('pvAVL', POINTER(None)),
]

dglNodePrioritizer_s = struct_anon_8 # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/graph.h: 135

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/graph.h: 146
class struct_anon_9(Structure):
    pass

struct_anon_9.__slots__ = [
    'cEdge',
    'iEdge',
    'pEdgePri32Item',
    'pvAVL',
]
struct_anon_9._fields_ = [
    ('cEdge', c_int),
    ('iEdge', c_int),
    ('pEdgePri32Item', POINTER(dglTreeEdgePri32_s)),
    ('pvAVL', POINTER(None)),
]

dglEdgePrioritizer_s = struct_anon_9 # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/graph.h: 146

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/graph.h: 193
class struct__dglGraph(Structure):
    pass

struct__dglGraph.__slots__ = [
    'iErrno',
    'Version',
    'Endian',
    'NodeAttrSize',
    'EdgeAttrSize',
    'aOpaqueSet',
    'cNode',
    'cHead',
    'cTail',
    'cAlone',
    'cEdge',
    'nnCost',
    'Flags',
    'nFamily',
    'nOptions',
    'pNodeTree',
    'pEdgeTree',
    'pNodeBuffer',
    'iNodeBuffer',
    'pEdgeBuffer',
    'iEdgeBuffer',
    'edgePrioritizer',
    'nodePrioritizer',
]
struct__dglGraph._fields_ = [
    ('iErrno', c_int),
    ('Version', dglByte_t),
    ('Endian', dglByte_t),
    ('NodeAttrSize', dglInt32_t),
    ('EdgeAttrSize', dglInt32_t),
    ('aOpaqueSet', dglInt32_t * 16),
    ('cNode', dglInt32_t),
    ('cHead', dglInt32_t),
    ('cTail', dglInt32_t),
    ('cAlone', dglInt32_t),
    ('cEdge', dglInt32_t),
    ('nnCost', dglInt64_t),
    ('Flags', dglInt32_t),
    ('nFamily', dglInt32_t),
    ('nOptions', dglInt32_t),
    ('pNodeTree', POINTER(None)),
    ('pEdgeTree', POINTER(None)),
    ('pNodeBuffer', POINTER(dglByte_t)),
    ('iNodeBuffer', dglInt32_t),
    ('pEdgeBuffer', POINTER(dglByte_t)),
    ('iEdgeBuffer', dglInt32_t),
    ('edgePrioritizer', dglEdgePrioritizer_s),
    ('nodePrioritizer', dglNodePrioritizer_s),
]

dglGraph_s = struct__dglGraph # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/graph.h: 193

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/graph.h: 243
class struct_anon_10(Structure):
    pass

struct_anon_10.__slots__ = [
    'nStartNode',
    'NodeHeap',
    'pvVisited',
    'pvPredist',
]
struct_anon_10._fields_ = [
    ('nStartNode', dglInt32_t),
    ('NodeHeap', dglHeap_s),
    ('pvVisited', POINTER(None)),
    ('pvPredist', POINTER(None)),
]

dglSPCache_s = struct_anon_10 # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dgl/graph.h: 243

RectReal = c_double # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/rtree.h: 28

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/rtree.h: 57
class struct_RTree_Rect(Structure):
    pass

struct_RTree_Rect.__slots__ = [
    'boundary',
]
struct_RTree_Rect._fields_ = [
    ('boundary', POINTER(RectReal)),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/rtree.h: 77
class struct_RTree_Node(Structure):
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/rtree.h: 64
class union_RTree_Child(Union):
    pass

union_RTree_Child.__slots__ = [
    'id',
    'ptr',
    'pos',
]
union_RTree_Child._fields_ = [
    ('id', c_int),
    ('ptr', POINTER(struct_RTree_Node)),
    ('pos', off_t),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/rtree.h: 71
class struct_RTree_Branch(Structure):
    pass

struct_RTree_Branch.__slots__ = [
    'rect',
    'child',
]
struct_RTree_Branch._fields_ = [
    ('rect', struct_RTree_Rect),
    ('child', union_RTree_Child),
]

struct_RTree_Node.__slots__ = [
    'count',
    'level',
    'branch',
]
struct_RTree_Node._fields_ = [
    ('count', c_int),
    ('level', c_int),
    ('branch', POINTER(struct_RTree_Branch)),
]

SearchHitCallback = CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(struct_RTree_Rect), POINTER(None)) # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/rtree.h: 91

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/rtree.h: 128
class struct_RTree(Structure):
    pass

rt_search_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_RTree), POINTER(struct_RTree_Rect), POINTER(SearchHitCallback), POINTER(None)) # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/rtree.h: 95

rt_insert_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_RTree_Rect), union_RTree_Child, c_int, POINTER(struct_RTree)) # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/rtree.h: 97

rt_delete_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_RTree_Rect), union_RTree_Child, POINTER(struct_RTree)) # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/rtree.h: 98

rt_valid_child_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(union_RTree_Child)) # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/rtree.h: 99

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/rtree.h: 103
class struct_nstack(Structure):
    pass

struct_nstack.__slots__ = [
    'sn',
    'branch_id',
    'pos',
]
struct_nstack._fields_ = [
    ('sn', POINTER(struct_RTree_Node)),
    ('branch_id', c_int),
    ('pos', off_t),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/rtree.h: 111
class struct_NodeBuffer(Structure):
    pass

struct_NodeBuffer.__slots__ = [
    'n',
    'pos',
    'dirty',
]
struct_NodeBuffer._fields_ = [
    ('n', struct_RTree_Node),
    ('pos', off_t),
    ('dirty', c_char),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/rtree.h: 119
class struct_RTree_PartitionVars(Structure):
    pass

struct_RTree_PartitionVars.__slots__ = [
    'partition',
    'total',
    'minfill',
    'taken',
    'count',
    'cover',
    'area',
]
struct_RTree_PartitionVars._fields_ = [
    ('partition', c_int * (9 + 1)),
    ('total', c_int),
    ('minfill', c_int),
    ('taken', c_int * (9 + 1)),
    ('count', c_int * 2),
    ('cover', struct_RTree_Rect * 2),
    ('area', RectReal * 2),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/rtree.h: 155
class struct__recycle(Structure):
    pass

struct__recycle.__slots__ = [
    'avail',
    'alloc',
    'pos',
]
struct__recycle._fields_ = [
    ('avail', c_int),
    ('alloc', c_int),
    ('pos', POINTER(off_t)),
]

struct_RTree.__slots__ = [
    'fd',
    'ndims',
    'nsides',
    'ndims_alloc',
    'nsides_alloc',
    'nodesize',
    'branchsize',
    'rectsize',
    'n_nodes',
    'n_leafs',
    'rootlevel',
    'nodecard',
    'leafcard',
    'min_node_fill',
    'min_leaf_fill',
    'minfill_node_split',
    'minfill_leaf_split',
    'overflow',
    'free_nodes',
    'nb',
    'used',
    'insert_rect',
    'delete_rect',
    'search_rect',
    'valid_child',
    'root',
    'ns',
    'p',
    'BranchBuf',
    'tmpb1',
    'tmpb2',
    'c',
    'BranchCount',
    'rect_0',
    'rect_1',
    'upperrect',
    'orect',
    'center_n',
    'rootpos',
]
struct_RTree._fields_ = [
    ('fd', c_int),
    ('ndims', c_ubyte),
    ('nsides', c_ubyte),
    ('ndims_alloc', c_ubyte),
    ('nsides_alloc', c_ubyte),
    ('nodesize', c_int),
    ('branchsize', c_int),
    ('rectsize', c_int),
    ('n_nodes', c_int),
    ('n_leafs', c_int),
    ('rootlevel', c_int),
    ('nodecard', c_int),
    ('leafcard', c_int),
    ('min_node_fill', c_int),
    ('min_leaf_fill', c_int),
    ('minfill_node_split', c_int),
    ('minfill_leaf_split', c_int),
    ('overflow', c_char),
    ('free_nodes', struct__recycle),
    ('nb', POINTER(POINTER(struct_NodeBuffer))),
    ('used', POINTER(POINTER(c_int))),
    ('insert_rect', POINTER(rt_insert_fn)),
    ('delete_rect', POINTER(rt_delete_fn)),
    ('search_rect', POINTER(rt_search_fn)),
    ('valid_child', POINTER(rt_valid_child_fn)),
    ('root', POINTER(struct_RTree_Node)),
    ('ns', POINTER(struct_nstack)),
    ('p', struct_RTree_PartitionVars),
    ('BranchBuf', POINTER(struct_RTree_Branch)),
    ('tmpb1', struct_RTree_Branch),
    ('tmpb2', struct_RTree_Branch),
    ('c', struct_RTree_Branch),
    ('BranchCount', c_int),
    ('rect_0', struct_RTree_Rect),
    ('rect_1', struct_RTree_Rect),
    ('upperrect', struct_RTree_Rect),
    ('orect', struct_RTree_Rect),
    ('center_n', POINTER(RectReal)),
    ('rootpos', off_t),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dbmi.h: 153
class struct__dbmscap(Structure):
    pass

struct__dbmscap.__slots__ = [
    'driverName',
    'startup',
    'comment',
    'next',
]
struct__dbmscap._fields_ = [
    ('driverName', c_char * 256),
    ('startup', c_char * 256),
    ('comment', c_char * 256),
    ('next', POINTER(struct__dbmscap)),
]

dbDbmscap = struct__dbmscap # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dbmi.h: 159

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dbmi.h: 173
class struct__db_driver(Structure):
    pass

struct__db_driver.__slots__ = [
    'dbmscap',
    'send',
    'recv',
    'pid',
]
struct__db_driver._fields_ = [
    ('dbmscap', dbDbmscap),
    ('send', POINTER(FILE)),
    ('recv', POINTER(FILE)),
    ('pid', c_int),
]

dbDriver = struct__db_driver # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/dbmi.h: 173

OGRFeatureH = POINTER(None) # /Applications/GRASS-7.8.app/Contents/Resources/include/ogr_api.h: 302

OGRLayerH = POINTER(None) # /Applications/GRASS-7.8.app/Contents/Resources/include/ogr_api.h: 509

OGRDataSourceH = POINTER(None) # /Applications/GRASS-7.8.app/Contents/Resources/include/ogr_api.h: 511

OGRSFDriverH = POINTER(None) # /Applications/GRASS-7.8.app/Contents/Resources/include/ogr_api.h: 513

plus_t = c_int # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 41

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 46
class struct_site_att(Structure):
    pass

struct_site_att.__slots__ = [
    'cat',
    'dbl',
    'str',
]
struct_site_att._fields_ = [
    ('cat', c_int),
    ('dbl', POINTER(c_double)),
    ('str', POINTER(POINTER(c_char))),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 65
class struct_bound_box(Structure):
    pass

struct_bound_box.__slots__ = [
    'N',
    'S',
    'E',
    'W',
    'T',
    'B',
]
struct_bound_box._fields_ = [
    ('N', c_double),
    ('S', c_double),
    ('E', c_double),
    ('W', c_double),
    ('T', c_double),
    ('B', c_double),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 96
class struct_gvfile(Structure):
    pass

struct_gvfile.__slots__ = [
    'file',
    'start',
    'current',
    'end',
    'size',
    'alloc',
    'loaded',
]
struct_gvfile._fields_ = [
    ('file', POINTER(FILE)),
    ('start', String),
    ('current', String),
    ('end', String),
    ('size', off_t),
    ('alloc', off_t),
    ('loaded', c_int),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 134
class struct_field_info(Structure):
    pass

struct_field_info.__slots__ = [
    'number',
    'name',
    'driver',
    'database',
    'table',
    'key',
]
struct_field_info._fields_ = [
    ('number', c_int),
    ('name', String),
    ('driver', String),
    ('database', String),
    ('table', String),
    ('key', String),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 165
class struct_dblinks(Structure):
    pass

struct_dblinks.__slots__ = [
    'field',
    'alloc_fields',
    'n_fields',
]
struct_dblinks._fields_ = [
    ('field', POINTER(struct_field_info)),
    ('alloc_fields', c_int),
    ('n_fields', c_int),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 186
class struct_Port_info(Structure):
    pass

struct_Port_info.__slots__ = [
    'byte_order',
    'off_t_size',
    'dbl_cnvrt',
    'flt_cnvrt',
    'lng_cnvrt',
    'int_cnvrt',
    'shrt_cnvrt',
    'off_t_cnvrt',
    'dbl_quick',
    'flt_quick',
    'lng_quick',
    'int_quick',
    'shrt_quick',
    'off_t_quick',
]
struct_Port_info._fields_ = [
    ('byte_order', c_int),
    ('off_t_size', c_int),
    ('dbl_cnvrt', c_ubyte * 8),
    ('flt_cnvrt', c_ubyte * 4),
    ('lng_cnvrt', c_ubyte * 4),
    ('int_cnvrt', c_ubyte * 4),
    ('shrt_cnvrt', c_ubyte * 2),
    ('off_t_cnvrt', c_ubyte * 8),
    ('dbl_quick', c_int),
    ('flt_quick', c_int),
    ('lng_quick', c_int),
    ('int_quick', c_int),
    ('shrt_quick', c_int),
    ('off_t_quick', c_int),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 272
class struct_recycle(Structure):
    pass

struct_recycle.__slots__ = [
    'dummy',
]
struct_recycle._fields_ = [
    ('dummy', c_char),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 278
class struct_Version_info(Structure):
    pass

struct_Version_info.__slots__ = [
    'major',
    'minor',
    'back_major',
    'back_minor',
]
struct_Version_info._fields_ = [
    ('major', c_int),
    ('minor', c_int),
    ('back_major', c_int),
    ('back_minor', c_int),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 294
class struct_dig_head(Structure):
    pass

struct_dig_head.__slots__ = [
    'organization',
    'date',
    'user_name',
    'map_name',
    'source_date',
    'orig_scale',
    'comment',
    'proj',
    'plani_zone',
    'digit_thresh',
    'coor_version',
    'with_z',
    'size',
    'head_size',
    'port',
    'last_offset',
    'recycle',
]
struct_dig_head._fields_ = [
    ('organization', String),
    ('date', String),
    ('user_name', String),
    ('map_name', String),
    ('source_date', String),
    ('orig_scale', c_long),
    ('comment', String),
    ('proj', c_int),
    ('plani_zone', c_int),
    ('digit_thresh', c_double),
    ('coor_version', struct_Version_info),
    ('with_z', c_int),
    ('size', off_t),
    ('head_size', c_long),
    ('port', struct_Port_info),
    ('last_offset', off_t),
    ('recycle', POINTER(struct_recycle)),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 397
class struct_Format_info_offset(Structure):
    pass

struct_Format_info_offset.__slots__ = [
    'array',
    'array_num',
    'array_alloc',
]
struct_Format_info_offset._fields_ = [
    ('array', POINTER(c_int)),
    ('array_num', c_int),
    ('array_alloc', c_int),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 1675
class struct_line_pnts(Structure):
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 461
class struct_Format_info_cache(Structure):
    pass

struct_Format_info_cache.__slots__ = [
    'lines',
    'lines_types',
    'lines_cats',
    'lines_alloc',
    'lines_num',
    'lines_next',
    'fid',
    'sf_type',
    'ctype',
]
struct_Format_info_cache._fields_ = [
    ('lines', POINTER(POINTER(struct_line_pnts))),
    ('lines_types', POINTER(c_int)),
    ('lines_cats', POINTER(c_int)),
    ('lines_alloc', c_int),
    ('lines_num', c_int),
    ('lines_next', c_int),
    ('fid', c_long),
    ('sf_type', SF_FeatureType),
    ('ctype', c_int),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 516
class struct_Format_info_ogr(Structure):
    pass

struct_Format_info_ogr.__slots__ = [
    'driver_name',
    'dsn',
    'layer_name',
    'where',
    'driver',
    'ds',
    'layer',
    'dbdriver',
    'dsn_options',
    'layer_options',
    'cache',
    'feature_cache',
    'offset',
    'next_line',
]
struct_Format_info_ogr._fields_ = [
    ('driver_name', String),
    ('dsn', String),
    ('layer_name', String),
    ('where', String),
    ('driver', OGRSFDriverH),
    ('ds', OGRDataSourceH),
    ('layer', OGRLayerH),
    ('dbdriver', POINTER(dbDriver)),
    ('dsn_options', POINTER(POINTER(c_char))),
    ('layer_options', POINTER(POINTER(c_char))),
    ('cache', struct_Format_info_cache),
    ('feature_cache', OGRFeatureH),
    ('offset', struct_Format_info_offset),
    ('next_line', c_int),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 602
class struct_Format_info_pg(Structure):
    pass

struct_Format_info_pg.__slots__ = [
    'conninfo',
    'db_name',
    'schema_name',
    'table_name',
    'where',
    'fid_column',
    'geom_column',
    'feature_type',
    'coor_dim',
    'srid',
    'dbdriver',
    'fi',
    'inTransaction',
    'conn',
    'res',
    'cursor_name',
    'cursor_fid',
    'next_line',
    'cache',
    'offset',
    'topogeom_column',
    'toposchema_name',
    'toposchema_id',
    'topo_geo_only',
]
struct_Format_info_pg._fields_ = [
    ('conninfo', String),
    ('db_name', String),
    ('schema_name', String),
    ('table_name', String),
    ('where', String),
    ('fid_column', String),
    ('geom_column', String),
    ('feature_type', SF_FeatureType),
    ('coor_dim', c_int),
    ('srid', c_int),
    ('dbdriver', POINTER(dbDriver)),
    ('fi', POINTER(struct_field_info)),
    ('inTransaction', c_int),
    ('conn', POINTER(None)),
    ('res', POINTER(None)),
    ('cursor_name', String),
    ('cursor_fid', c_int),
    ('next_line', c_int),
    ('cache', struct_Format_info_cache),
    ('offset', struct_Format_info_offset),
    ('topogeom_column', String),
    ('toposchema_name', String),
    ('toposchema_id', c_int),
    ('topo_geo_only', c_int),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 713
class struct_Format_info(Structure):
    pass

struct_Format_info.__slots__ = [
    'i',
    'ogr',
    'pg',
]
struct_Format_info._fields_ = [
    ('i', c_int),
    ('ogr', struct_Format_info_ogr),
    ('pg', struct_Format_info_pg),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 732
class struct_Cat_index(Structure):
    pass

struct_Cat_index.__slots__ = [
    'field',
    'n_cats',
    'a_cats',
    'cat',
    'n_ucats',
    'n_types',
    'type',
    'offset',
]
struct_Cat_index._fields_ = [
    ('field', c_int),
    ('n_cats', c_int),
    ('a_cats', c_int),
    ('cat', POINTER(c_int * 3)),
    ('n_ucats', c_int),
    ('n_types', c_int),
    ('type', (c_int * 2) * 7),
    ('offset', off_t),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 787
class struct_anon_58(Structure):
    pass

struct_anon_58.__slots__ = [
    'topo',
    'spidx',
    'cidx',
]
struct_anon_58._fields_ = [
    ('topo', struct_Version_info),
    ('spidx', struct_Version_info),
    ('cidx', struct_Version_info),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 1448
class struct_P_node(Structure):
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 1574
class struct_P_line(Structure):
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 1605
class struct_P_area(Structure):
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 1646
class struct_P_isle(Structure):
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 1173
class struct_anon_59(Structure):
    pass

struct_anon_59.__slots__ = [
    'do_uplist',
    'uplines',
    'uplines_offset',
    'alloc_uplines',
    'n_uplines',
    'upnodes',
    'alloc_upnodes',
    'n_upnodes',
]
struct_anon_59._fields_ = [
    ('do_uplist', c_int),
    ('uplines', POINTER(c_int)),
    ('uplines_offset', POINTER(off_t)),
    ('alloc_uplines', c_int),
    ('n_uplines', c_int),
    ('upnodes', POINTER(c_int)),
    ('alloc_upnodes', c_int),
    ('n_upnodes', c_int),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 784
class struct_Plus_head(Structure):
    pass

struct_Plus_head.__slots__ = [
    'version',
    'with_z',
    'spidx_with_z',
    'off_t_size',
    'head_size',
    'spidx_head_size',
    'cidx_head_size',
    'release_support',
    'port',
    'spidx_port',
    'cidx_port',
    'mode',
    'built',
    'box',
    'Node',
    'Line',
    'Area',
    'Isle',
    'n_plines',
    'n_llines',
    'n_blines',
    'n_clines',
    'n_flines',
    'n_klines',
    'n_vfaces',
    'n_hfaces',
    'n_nodes',
    'n_edges',
    'n_lines',
    'n_areas',
    'n_isles',
    'n_faces',
    'n_volumes',
    'n_holes',
    'alloc_nodes',
    'alloc_edges',
    'alloc_lines',
    'alloc_areas',
    'alloc_isles',
    'alloc_faces',
    'alloc_volumes',
    'alloc_holes',
    'Node_offset',
    'Edge_offset',
    'Line_offset',
    'Area_offset',
    'Isle_offset',
    'Volume_offset',
    'Hole_offset',
    'Spidx_built',
    'Spidx_new',
    'Spidx_file',
    'spidx_fp',
    'Node_spidx_offset',
    'Line_spidx_offset',
    'Area_spidx_offset',
    'Isle_spidx_offset',
    'Face_spidx_offset',
    'Volume_spidx_offset',
    'Hole_spidx_offset',
    'Node_spidx',
    'Line_spidx',
    'Area_spidx',
    'Isle_spidx',
    'Face_spidx',
    'Volume_spidx',
    'Hole_spidx',
    'update_cidx',
    'n_cidx',
    'a_cidx',
    'cidx',
    'cidx_up_to_date',
    'coor_size',
    'coor_mtime',
    'uplist',
]
struct_Plus_head._fields_ = [
    ('version', struct_anon_58),
    ('with_z', c_int),
    ('spidx_with_z', c_int),
    ('off_t_size', c_int),
    ('head_size', c_long),
    ('spidx_head_size', c_long),
    ('cidx_head_size', c_long),
    ('release_support', c_int),
    ('port', struct_Port_info),
    ('spidx_port', struct_Port_info),
    ('cidx_port', struct_Port_info),
    ('mode', c_int),
    ('built', c_int),
    ('box', struct_bound_box),
    ('Node', POINTER(POINTER(struct_P_node))),
    ('Line', POINTER(POINTER(struct_P_line))),
    ('Area', POINTER(POINTER(struct_P_area))),
    ('Isle', POINTER(POINTER(struct_P_isle))),
    ('n_plines', plus_t),
    ('n_llines', plus_t),
    ('n_blines', plus_t),
    ('n_clines', plus_t),
    ('n_flines', plus_t),
    ('n_klines', plus_t),
    ('n_vfaces', plus_t),
    ('n_hfaces', plus_t),
    ('n_nodes', plus_t),
    ('n_edges', plus_t),
    ('n_lines', plus_t),
    ('n_areas', plus_t),
    ('n_isles', plus_t),
    ('n_faces', plus_t),
    ('n_volumes', plus_t),
    ('n_holes', plus_t),
    ('alloc_nodes', plus_t),
    ('alloc_edges', plus_t),
    ('alloc_lines', plus_t),
    ('alloc_areas', plus_t),
    ('alloc_isles', plus_t),
    ('alloc_faces', plus_t),
    ('alloc_volumes', plus_t),
    ('alloc_holes', plus_t),
    ('Node_offset', off_t),
    ('Edge_offset', off_t),
    ('Line_offset', off_t),
    ('Area_offset', off_t),
    ('Isle_offset', off_t),
    ('Volume_offset', off_t),
    ('Hole_offset', off_t),
    ('Spidx_built', c_int),
    ('Spidx_new', c_int),
    ('Spidx_file', c_int),
    ('spidx_fp', struct_gvfile),
    ('Node_spidx_offset', off_t),
    ('Line_spidx_offset', off_t),
    ('Area_spidx_offset', off_t),
    ('Isle_spidx_offset', off_t),
    ('Face_spidx_offset', off_t),
    ('Volume_spidx_offset', off_t),
    ('Hole_spidx_offset', off_t),
    ('Node_spidx', POINTER(struct_RTree)),
    ('Line_spidx', POINTER(struct_RTree)),
    ('Area_spidx', POINTER(struct_RTree)),
    ('Isle_spidx', POINTER(struct_RTree)),
    ('Face_spidx', POINTER(struct_RTree)),
    ('Volume_spidx', POINTER(struct_RTree)),
    ('Hole_spidx', POINTER(struct_RTree)),
    ('update_cidx', c_int),
    ('n_cidx', c_int),
    ('a_cidx', c_int),
    ('cidx', POINTER(struct_Cat_index)),
    ('cidx_up_to_date', c_int),
    ('coor_size', off_t),
    ('coor_mtime', c_long),
    ('uplist', struct_anon_59),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 1220
class struct_Graph_info(Structure):
    pass

struct_Graph_info.__slots__ = [
    'line_type',
    'graph_s',
    'spCache',
    'edge_fcosts',
    'edge_bcosts',
    'node_costs',
    'cost_multip',
]
struct_Graph_info._fields_ = [
    ('line_type', c_int),
    ('graph_s', dglGraph_s),
    ('spCache', dglSPCache_s),
    ('edge_fcosts', POINTER(c_double)),
    ('edge_bcosts', POINTER(c_double)),
    ('node_costs', POINTER(c_double)),
    ('cost_multip', c_int),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 1358
class struct_anon_60(Structure):
    pass

struct_anon_60.__slots__ = [
    'region_flag',
    'box',
    'type_flag',
    'type',
    'field_flag',
    'field',
]
struct_anon_60._fields_ = [
    ('region_flag', c_int),
    ('box', struct_bound_box),
    ('type_flag', c_int),
    ('type', c_int),
    ('field_flag', c_int),
    ('field', c_int),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 1259
class struct_Map_info(Structure):
    pass

struct_Map_info.__slots__ = [
    'format',
    'temporary',
    'dblnk',
    'plus',
    'open',
    'mode',
    'level',
    'head_only',
    'support_updated',
    'name',
    'mapset',
    'location',
    'gisdbase',
    'next_line',
    'constraint',
    'proj',
    'hist_fp',
    'dgraph',
    'head',
    'dig_fp',
    'fInfo',
    'site_att',
    'n_site_att',
    'n_site_dbl',
    'n_site_str',
]
struct_Map_info._fields_ = [
    ('format', c_int),
    ('temporary', c_int),
    ('dblnk', POINTER(struct_dblinks)),
    ('plus', struct_Plus_head),
    ('open', c_int),
    ('mode', c_int),
    ('level', c_int),
    ('head_only', c_int),
    ('support_updated', c_int),
    ('name', String),
    ('mapset', String),
    ('location', String),
    ('gisdbase', String),
    ('next_line', plus_t),
    ('constraint', struct_anon_60),
    ('proj', c_int),
    ('hist_fp', POINTER(FILE)),
    ('dgraph', struct_Graph_info),
    ('head', struct_dig_head),
    ('dig_fp', struct_gvfile),
    ('fInfo', struct_Format_info),
    ('site_att', POINTER(struct_site_att)),
    ('n_site_att', c_int),
    ('n_site_dbl', c_int),
    ('n_site_str', c_int),
]

struct_P_node.__slots__ = [
    'x',
    'y',
    'z',
    'alloc_lines',
    'n_lines',
    'lines',
    'angles',
]
struct_P_node._fields_ = [
    ('x', c_double),
    ('y', c_double),
    ('z', c_double),
    ('alloc_lines', plus_t),
    ('n_lines', plus_t),
    ('lines', POINTER(plus_t)),
    ('angles', POINTER(c_float)),
]

struct_P_line.__slots__ = [
    'type',
    'offset',
    'topo',
]
struct_P_line._fields_ = [
    ('type', c_char),
    ('offset', off_t),
    ('topo', POINTER(None)),
]

struct_P_area.__slots__ = [
    'n_lines',
    'alloc_lines',
    'lines',
    'centroid',
    'n_isles',
    'alloc_isles',
    'isles',
]
struct_P_area._fields_ = [
    ('n_lines', plus_t),
    ('alloc_lines', plus_t),
    ('lines', POINTER(plus_t)),
    ('centroid', plus_t),
    ('n_isles', plus_t),
    ('alloc_isles', plus_t),
    ('isles', POINTER(plus_t)),
]

struct_P_isle.__slots__ = [
    'n_lines',
    'alloc_lines',
    'lines',
    'area',
]
struct_P_isle._fields_ = [
    ('n_lines', plus_t),
    ('alloc_lines', plus_t),
    ('lines', POINTER(plus_t)),
    ('area', plus_t),
]

struct_line_pnts.__slots__ = [
    'x',
    'y',
    'z',
    'n_points',
    'alloc_points',
]
struct_line_pnts._fields_ = [
    ('x', POINTER(c_double)),
    ('y', POINTER(c_double)),
    ('z', POINTER(c_double)),
    ('n_points', c_int),
    ('alloc_points', c_int),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vect/dig_structs.h: 1723
class struct_cat_list(Structure):
    pass

struct_cat_list.__slots__ = [
    'field',
    'min',
    'max',
    'n_ranges',
    'alloc_ranges',
]
struct_cat_list._fields_ = [
    ('field', c_int),
    ('min', POINTER(c_int)),
    ('max', POINTER(c_int)),
    ('n_ranges', c_int),
    ('alloc_ranges', c_int),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 45
class struct_rpoint(Structure):
    pass

struct_rpoint.__slots__ = [
    'x',
    'y',
]
struct_rpoint._fields_ = [
    ('x', c_int),
    ('y', c_int),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 50
class struct_robject(Structure):
    pass

struct_robject.__slots__ = [
    'fid',
    'type',
    'npoints',
    'point',
]
struct_robject._fields_ = [
    ('fid', c_int),
    ('type', c_int),
    ('npoints', c_int),
    ('point', POINTER(struct_rpoint)),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 58
class struct_robject_list(Structure):
    pass

struct_robject_list.__slots__ = [
    'nitems',
    'item',
]
struct_robject_list._fields_ = [
    ('nitems', c_int),
    ('item', POINTER(POINTER(struct_robject))),
]

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 5
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_split_lines'):
        continue
    Vedit_split_lines = _lib.Vedit_split_lines
    Vedit_split_lines.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), POINTER(struct_line_pnts), c_double, POINTER(struct_ilist)]
    Vedit_split_lines.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 7
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_connect_lines'):
        continue
    Vedit_connect_lines = _lib.Vedit_connect_lines
    Vedit_connect_lines.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), c_double]
    Vedit_connect_lines.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 10
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_extend_lines'):
        continue
    Vedit_extend_lines = _lib.Vedit_extend_lines
    Vedit_extend_lines.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), c_int, c_int, c_double]
    Vedit_extend_lines.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 13
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_modify_cats'):
        continue
    Vedit_modify_cats = _lib.Vedit_modify_cats
    Vedit_modify_cats.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), c_int, c_int, POINTER(struct_cat_list)]
    Vedit_modify_cats.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 17
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_copy_lines'):
        continue
    Vedit_copy_lines = _lib.Vedit_copy_lines
    Vedit_copy_lines.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info), POINTER(struct_ilist)]
    Vedit_copy_lines.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 20
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_chtype_lines'):
        continue
    Vedit_chtype_lines = _lib.Vedit_chtype_lines
    Vedit_chtype_lines.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist)]
    Vedit_chtype_lines.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 23
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_delete_lines'):
        continue
    Vedit_delete_lines = _lib.Vedit_delete_lines
    Vedit_delete_lines.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist)]
    Vedit_delete_lines.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 24
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_delete_area_centroid'):
        continue
    Vedit_delete_area_centroid = _lib.Vedit_delete_area_centroid
    Vedit_delete_area_centroid.argtypes = [POINTER(struct_Map_info), c_int]
    Vedit_delete_area_centroid.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 25
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_delete_area'):
        continue
    Vedit_delete_area = _lib.Vedit_delete_area
    Vedit_delete_area.argtypes = [POINTER(struct_Map_info), c_int]
    Vedit_delete_area.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 26
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_delete_areas_cat'):
        continue
    Vedit_delete_areas_cat = _lib.Vedit_delete_areas_cat
    Vedit_delete_areas_cat.argtypes = [POINTER(struct_Map_info), c_int, c_int]
    Vedit_delete_areas_cat.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 29
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_get_min_distance'):
        continue
    Vedit_get_min_distance = _lib.Vedit_get_min_distance
    Vedit_get_min_distance.argtypes = [POINTER(struct_line_pnts), POINTER(struct_line_pnts), c_int, POINTER(c_int)]
    Vedit_get_min_distance.restype = c_double
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 33
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_flip_lines'):
        continue
    Vedit_flip_lines = _lib.Vedit_flip_lines
    Vedit_flip_lines.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist)]
    Vedit_flip_lines.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 36
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_merge_lines'):
        continue
    Vedit_merge_lines = _lib.Vedit_merge_lines
    Vedit_merge_lines.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist)]
    Vedit_merge_lines.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 39
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_move_lines'):
        continue
    Vedit_move_lines = _lib.Vedit_move_lines
    Vedit_move_lines.argtypes = [POINTER(struct_Map_info), POINTER(POINTER(struct_Map_info)), c_int, POINTER(struct_ilist), c_double, c_double, c_double, c_int, c_double]
    Vedit_move_lines.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 43
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_render_map'):
        continue
    Vedit_render_map = _lib.Vedit_render_map
    Vedit_render_map.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box), c_int, c_double, c_double, c_int, c_int, c_double]
    Vedit_render_map.restype = POINTER(struct_robject_list)
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 47
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_select_by_query'):
        continue
    Vedit_select_by_query = _lib.Vedit_select_by_query
    Vedit_select_by_query.argtypes = [POINTER(struct_Map_info), c_int, c_int, c_double, c_int, POINTER(struct_ilist)]
    Vedit_select_by_query.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 51
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_snap_point'):
        continue
    Vedit_snap_point = _lib.Vedit_snap_point
    Vedit_snap_point.argtypes = [POINTER(struct_Map_info), c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), c_double, c_int]
    Vedit_snap_point.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 53
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_snap_line'):
        continue
    Vedit_snap_line = _lib.Vedit_snap_line
    Vedit_snap_line.argtypes = [POINTER(struct_Map_info), POINTER(POINTER(struct_Map_info)), c_int, c_int, POINTER(struct_line_pnts), c_double, c_int]
    Vedit_snap_line.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 55
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_snap_lines'):
        continue
    Vedit_snap_lines = _lib.Vedit_snap_lines
    Vedit_snap_lines.argtypes = [POINTER(struct_Map_info), POINTER(POINTER(struct_Map_info)), c_int, POINTER(struct_ilist), c_double, c_int]
    Vedit_snap_lines.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 59
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_move_vertex'):
        continue
    Vedit_move_vertex = _lib.Vedit_move_vertex
    Vedit_move_vertex.argtypes = [POINTER(struct_Map_info), POINTER(POINTER(struct_Map_info)), c_int, POINTER(struct_ilist), POINTER(struct_line_pnts), c_double, c_double, c_double, c_double, c_double, c_int, c_int]
    Vedit_move_vertex.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 63
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_add_vertex'):
        continue
    Vedit_add_vertex = _lib.Vedit_add_vertex
    Vedit_add_vertex.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), POINTER(struct_line_pnts), c_double]
    Vedit_add_vertex.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 65
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_remove_vertex'):
        continue
    Vedit_remove_vertex = _lib.Vedit_remove_vertex
    Vedit_remove_vertex.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), POINTER(struct_line_pnts), c_double]
    Vedit_remove_vertex.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/defs/vedit.h: 69
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vedit_bulk_labeling'):
        continue
    Vedit_bulk_labeling = _lib.Vedit_bulk_labeling
    Vedit_bulk_labeling.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), c_double, c_double, c_double, c_double, c_double, c_double]
    Vedit_bulk_labeling.restype = c_int
    break

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 7
try:
    NO_SNAP = 0
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 8
try:
    SNAP = 1
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 9
try:
    SNAPVERTEX = 2
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 11
try:
    QUERY_UNKNOWN = (-1)
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 12
try:
    QUERY_LENGTH = 0
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 13
try:
    QUERY_DANGLE = 1
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 16
try:
    TYPE_POINT = 1
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 17
try:
    TYPE_LINE = 2
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 18
try:
    TYPE_BOUNDARYNO = 4
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 19
try:
    TYPE_BOUNDARYTWO = 8
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 20
try:
    TYPE_BOUNDARYONE = 16
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 21
try:
    TYPE_CENTROIDIN = 32
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 22
try:
    TYPE_CENTROIDOUT = 64
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 23
try:
    TYPE_CENTROIDDUP = 128
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 24
try:
    TYPE_NODEONE = 256
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 25
try:
    TYPE_NODETWO = 512
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 26
try:
    TYPE_VERTEX = 1024
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 27
try:
    TYPE_AREA = 2048
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 28
try:
    TYPE_ISLE = 4096
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 29
try:
    TYPE_DIRECTION = 8192
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 31
try:
    DRAW_POINT = 1
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 32
try:
    DRAW_LINE = 2
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 33
try:
    DRAW_BOUNDARYNO = 4
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 34
try:
    DRAW_BOUNDARYTWO = 8
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 35
try:
    DRAW_BOUNDARYONE = 16
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 36
try:
    DRAW_CENTROIDIN = 32
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 37
try:
    DRAW_CENTROIDOUT = 64
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 38
try:
    DRAW_CENTROIDDUP = 128
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 39
try:
    DRAW_NODEONE = 256
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 40
try:
    DRAW_NODETWO = 512
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 41
try:
    DRAW_VERTEX = 1024
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 42
try:
    DRAW_AREA = 2048
except:
    pass

# /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 43
try:
    DRAW_DIRECTION = 4096
except:
    pass

rpoint = struct_rpoint # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 45

robject = struct_robject # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 50

robject_list = struct_robject_list # /Users/cmbarton/grass_source/grass-7.8.3/dist.x86_64-apple-darwin18.7.0/include/grass/vedit.h: 58

# No inserted files

