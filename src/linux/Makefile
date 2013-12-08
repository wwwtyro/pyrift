
SYSARCH       = i386
ifeq ($(shell uname -m),x86_64)
SYSARCH       = x86_64
endif

CXX	= g++

all:
	$(CXX) pyrift.cpp -I LibOVR/Include \
	LibOVR/Lib/Linux/Release/$(SYSARCH)/libovr.a \
	-lpthread -ludev -lXinerama -lX11 --shared -fPIC -o ../../pyrift/_pyrift.so

exe:
	$(CXX) pyrift.cpp -I LibOVR/Include \
	LibOVR/Lib/Linux/Debug/$(SYSARCH)/libovr.a \
	-g -lpthread -ludev -lXinerama -lX11 -fPIC -o pyrift

clean:
	rm -f ../../pyrift/_pyrift.so ./pyrift
