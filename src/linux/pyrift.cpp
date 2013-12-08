#include "OVR.h"

extern "C" void initialize(void);
extern "C" void get_orientation(float *, float *, float *);
extern "C" void get_orientation_quaternion(float *, float *, float *, float *);

using namespace OVR;

Ptr<DeviceManager> pManager;
Ptr<SensorDevice> pSensor;
SensorFusion* pSFusion;

void initialize(void) {
    System::Init(Log::ConfigureDefaultLog(LogMask_All));    
    pManager = *DeviceManager::Create();
    pSensor = *pManager->EnumerateDevices<SensorDevice>().CreateDevice();
    pSFusion = new SensorFusion();
    pSFusion->AttachToSensor(pSensor);
    pSFusion->Reset();
}

void get_orientation(float *yaw, float *pitch, float *roll) {
    Quatf hmdOrient = pSFusion->GetPredictedOrientation();
    hmdOrient.GetEulerAngles<Axis_Y, Axis_X, Axis_Z>(yaw, pitch, roll);
}

void get_orientation_quaternion(float *x, float *y, float *z, float *w) {
    Quatf hmdOrient = pSFusion->GetPredictedOrientation();
    *x = hmdOrient.x;
    *y = hmdOrient.y;
    *z = hmdOrient.z;
    *w = hmdOrient.w;
}

int main(void) {
    initialize();
    float yaw, pitch, roll;
    while (true) {
        get_orientation(&yaw, &pitch, &roll);
        printf("%f, %f, %f\n", yaw, pitch, roll);
    }
}