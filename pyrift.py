from ctypes import *

sdk = CDLL("libovr.dll")

ovrHmdCap_Present           = 0x0001
ovrHmdCap_Available         = 0x0002
ovrHmdCap_Orientation       = 0x0010
ovrHmdCap_YawCorrection     = 0x0020
ovrHmdCap_Position          = 0x0040
ovrHmdCap_LowPersistence    = 0x0080
ovrHmdCap_LatencyTest       = 0x0100
ovrHmdCap_DynamicPrediction = 0x0200
ovrHmdCap_NoVSync           = 0x1000
ovrHmdCap_All = 0x0001 | 0x0002 | 0x0010 | 0x0020 | 0x0040 | 0x0080 | 0x0100 | 0x0200 | 0x1000

# typedef enum
# {
#     ovrHmd_None             = 0,    
#     ovrHmd_DK1              = 3,
#     ovrHmd_DKHD             = 4,
#     ovrHmd_CrystalCoveProto = 5,
#     ovrHmd_DK2              = 6,
#     ovrHmd_Other            
# } ovrHmdType;
ovrHmdType              = c_int
ovrHmd_None             = 0    
ovrHmd_DK1              = 3
ovrHmd_DKHD             = 4
ovrHmd_CrystalCoveProto = 5
ovrHmd_DK2              = 6
ovrHmd_Other            = 7

# typedef struct ovrSizei_
# {
#     int w, h;
# } ovrSizei;
class ovrSizei(Structure):
    pass
ovrSizei._fields_ = [
    ("w", c_int),
    ("h", c_int)
]

# typedef struct ovrVector2i_
# {
#     int x, y;
# } ovrVector2i;
class ovrVector2i(Structure):
    pass
ovrVector2i._fields_ = [
    ("x", c_int),
    ("y", c_int)
]

# typedef struct ovrFovPort_
# {
#     float UpTan;
#     float DownTan;
#     float LeftTan;
#     float RightTan;
# } ovrFovPort;
class ovrFovPort(Structure):
    pass
ovrFovPort._fields_ = [
    ("UpTan", c_float),
    ("DownTan", c_float),
    ("LeftTan", c_float),
    ("RightTan", c_float)
]

# typedef enum
# {
#     ovrEye_Left  = 0,
#     ovrEye_Right = 1,
#     ovrEye_Count = 2
# } ovrEyeType;
ovrEyeType   = c_int
ovrEye_Left  = 0
ovrEye_Right = 1
ovrEye_Count = 2

# struct ovrHmdStruct { };
class ovrHmdStruct(Structure):
    pass

# typedef struct ovrHmdStruct* ovrHmd;
ovrHmd = POINTER(ovrHmdStruct)

# typedef struct ovrHmdDesc_
# {
#     ovrHmd         Handle;
#     ovrHmdType     Type;
#     const char*    ProductName;    
#     const char*    Manufacturer;
#     unsigned int   Caps;
#     unsigned int   DistortionCaps;
#     ovrSizei       Resolution;
#     ovrVector2i    WindowsPos;     
#     ovrFovPort     DefaultEyeFov[ovrEye_Count];
#     ovrFovPort     MaxEyeFov[ovrEye_Count];
#     ovrEyeType     EyeRenderOrder[ovrEye_Count];
#     const char*    DisplayDeviceName;
#     long           DisplayId;
# } ovrHmdDesc;
class ovrHmdDesc(Structure):
    pass
ovrHmdDesc._fields_ = [
    ("Handle", ovrHmd),
    ("Type", ovrHmdType),
    ("ProductName", c_char_p),
    ("Manufacturer", c_char_p),
    ("Caps", c_uint),
    ("DistortionCaps", c_uint),
    ("Resolution", ovrSizei),
    ("WindowsPos", ovrVector2i),
    ("DefaultEyeFov", ovrFovPort * ovrEye_Count),
    ("MaxEyeFov", ovrFovPort * ovrEye_Count),
    ("EyeRenderOrder", ovrEyeType * ovrEye_Count),
    ("DisplayDeviceName", c_char_p),
    ("DisplayId", c_long)
]


# typedef char ovrBool;
ovrBool = c_char

# typedef struct ovrQuatf_
# {
#     float x, y, z, w;  
# } ovrQuatf;
class ovrQuatf(Structure):
    pass
ovrQuatf._fields_ = [
    ("x", c_float), 
    ("y", c_float), 
    ("z", c_float), 
    ("w", c_float)
]

# typedef struct ovrVector3f_
# {
#     float x, y, z;
# } ovrVector3f;
class ovrVector3f(Structure):
    pass
ovrVector3f._fields_ = [
    ("x", c_float),
    ("y", c_float),
    ("z", c_float),
]

# typedef struct ovrPosef_
# {
#     ovrQuatf     Orientation;
#     ovrVector3f  Position;    
# } ovrPosef;
class ovrPosef(Structure):
    pass
ovrPosef._fields_ = [
    ("Orientation", ovrQuatf),
    ("Position", ovrVector3f)
]

# typedef struct ovrPoseStatef_
# {
#     ovrPosef     Pose;
#     ovrVector3f  AngularVelocity;
#     ovrVector3f  LinearVelocity;
#     ovrVector3f  AngularAcceleration;
#     ovrVector3f  LinearAcceleration;
#     double       TimeInSeconds;
# } ovrPoseStatef;
class ovrPoseStatef(Structure):
    pass
ovrPoseStatef._fields_ = [
    ("Pose", ovrPosef),
    ("AngularVelocity", ovrVector3f),
    ("LinearVelocity", ovrVector3f),
    ("AngularAcceleration", ovrVector3f),
    ("LinearAcceleration", ovrVector3f),
    ("TimeInSeconds", c_double)
]

# typedef struct ovrSensorState_
# {
#     ovrPoseStatef  Predicted;
#     ovrPoseStatef  Recorded;
#     float          Temperature;    
#     unsigned int   StatusFlags;
# } ovrSensorState;
class ovrSensorState(Structure):
    pass
ovrSensorState._fields_ = [ 
    ("Predicted", ovrPoseStatef),
    ("Recorded", ovrPoseStatef),
    ("Temperature", c_float),
    ("StatusFlags", c_uint)
]



# ovrBool  ovr_Initialize();
sdk.ovr_Initialize.argtypes = []
sdk.ovr_Initialize.restype = ovrBool

# OVR_EXPORT void     ovr_Shutdown();

# OVR_EXPORT int      ovrHmd_Detect();

# OVR_EXPORT ovrHmd   ovrHmd_Create(int index);
sdk.ovrHmd_Create.argtypes = [c_int]
sdk.ovrHmd_Create.restype = ovrHmd

# OVR_EXPORT void     ovrHmd_Destroy(ovrHmd hmd);

# ovrBool  ovrHmd_StartSensor(ovrHmd hmd, unsigned int supportedCaps,
sdk.ovrHmd_StartSensor.argtypes = [c_void_p, c_uint, c_uint]
sdk.ovrHmd_StartSensor.restype = ovrBool

# ovrSensorState ovrHmd_GetSensorState(ovrHmd hmd, double absTime);
sdk.ovrHmd_GetSensorState.argtypes = [ovrHmd, c_double]
sdk.ovrHmd_GetSensorState.restype = ovrSensorState

# double   ovr_GetTimeInSeconds();
sdk.ovr_GetTimeInSeconds.argtypes = []
sdk.ovr_GetTimeInSeconds.restype = c_double



import time
hmd = None

sdk.ovr_Initialize()

def acquire():
    hmd = sdk.ovrHmd_Create(0)
    hmdDesc = ovrHmdDesc()
    sdk.ovrHmd_GetDesc(hmd, byref(hmdDesc))
    sdk.ovrHmd_StartSensor(hmd, ovrHmdCap_All, ovrHmdCap_Orientation)
    while True:
        ss = sdk.ovrHmd_GetSensorState(hmd, sdk.ovr_GetTimeInSeconds())
        pose = ss.Predicted.Pose
        print "%10f   %10f   %10f   %10f" % ( \
            pose.Orientation.w, 
            pose.Orientation.x, 
            pose.Orientation.y, 
            pose.Orientation.z
        )
        time.sleep(0.016)
# ovr_Initialize()
# hmd = ovrHmd_Create(0)
# hmdDesc = ovrHmdDesc()
# ovrHmd_GetDesc(hmd, byref(hmdDesc))
# print hmdDesc.ProductName
# ovrHmd_StartSensor( \
#     hmd, 
#     ovrHmdCap_Orientation | 
#     ovrHmdCap_YawCorrection, 
#     0
# )

# while True:
#     ss = ovrHmd_GetSensorState(hmd, ovr_GetTimeInSeconds())
#     pose = ss.Predicted.Pose
#     # import pdb; pdb.set_trace()
#     print "%10f   %10f   %10f   %10f" % ( \
#         pose.Orientation.w, 
#         pose.Orientation.x, 
#         pose.Orientation.y, 
#         pose.Orientation.z
#     )
#     time.sleep(0.016)

# ovrHmd_Destroy(hmd)
# ovr_Shutdown()



if __name__ == "__main__":
    acquire()
# ['ARRAY', 'ArgumentError', 'Array', 'BigEndianStructure', 'CDLL', 'CFUNCTYPE', 'DEFAULT_MODE', 'DllCanUnloadNow', 'DllGe
# tClassObject', 'FormatError', 'GetLastError', 'HRESULT', 'LibraryLoader', 'LittleEndianStructure', 'OleDLL', 'POINTER',
# 'PYFUNCTYPE', 'PyDLL', 'RTLD_GLOBAL', 'RTLD_LOCAL', 'SetPointerType', 'Structure', 'Union', 'WINFUNCTYPE', 'WinDLL', 'Wi
# nError', '__builtins__', '__doc__', '__name__', '__package__', 'addressof', 'alignment', 'byref', 'c_bool', 'c_buffer',
# 'c_byte', 'c_char', 'c_char_p', 'c_double', 'c_float', 'c_int', 'c_int16', 'c_int32', 'c_int64', 'c_int8', 'c_long', 'c_
# longdouble', 'c_longlong', 'c_short', 'c_size_t', 'c_ssize_t', 'c_ubyte', 'c_uint', 'c_uint16', 'c_uint32', 'c_uint64',
# 'c_uint8', 'c_ulong', 'c_ulonglong', 'c_ushort', 'c_void_p', 'c_voidp', 'c_wchar', 'c_wchar_p', 'cast', 'cdll', 'create_
# string_buffer', 'create_unicode_buffer', 'get_errno', 'get_last_error', 'memmove', 'memset', 'oledll', 'pointer', 'py_ob
# ject', 'pydll', 'pythonapi', 'resize', 'set_conversion_mode', 'set_errno', 'set_last_error', 'sizeof', 'string_at', 'win
# dll', 'wstring_at']