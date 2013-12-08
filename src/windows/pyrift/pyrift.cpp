#include "../../LibOVR/Include/OVR.h"

using namespace OVR;

Ptr<DeviceManager> pManager;
Ptr<HMDDevice> pHMD;
Ptr<SensorDevice> pSensor;
SensorFusion SFusion;
Util::MagCalibration MagCal;

extern "C" {

    __declspec(dllexport) void initialize(void) {
        System::Init(Log::ConfigureDefaultLog(LogMask_None));    
        pManager = *DeviceManager::Create();
        pHMD = *pManager->EnumerateDevices<HMDDevice>().CreateDevice(); 
        pSensor = *pHMD->GetSensor();
        SFusion.AttachToSensor(pSensor);
        MagCal.BeginAutoCalibration(SFusion);
    }

    __declspec(dllexport) void get_orientation(float *yaw, float *pitch, float *roll) {
        Quatf hmdOrient = SFusion.GetPredictedOrientation();
        hmdOrient.GetEulerAngles<Axis_Y, Axis_X, Axis_Z>(yaw, pitch, roll);
    }

    __declspec(dllexport) bool is_calibrated(void) {
        return MagCal.IsCalibrated();
    }

    __declspec(dllexport) void update_calibration(void) {
        if (MagCal.IsAutoCalibrating()) 
        {
            MagCal.UpdateAutoCalibration(SFusion);
            if (MagCal.IsCalibrated())
            {
                SFusion.SetYawCorrectionEnabled(true);
            }
        }
    }

}