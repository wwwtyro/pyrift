#include "OVR.h"

extern "C" void initialize(void);
extern "C" void get_orientation(float *, float *, float *);

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

int main(void) {
    initialize();
    float yaw, pitch, roll;
    while (true) {
        get_orientation(&yaw, &pitch, &roll);
        printf("%f, %f, %f\n", yaw, pitch, roll);
    }
}