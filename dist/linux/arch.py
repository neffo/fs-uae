#!/usr/bin/env python3
import sys
import platform

X86_MACHINES = ["x86", "i386", "i486", "i586", "i686"]
X86_64_MACHINES = ["x86_64", "x86-64", "amd64"]
ARM_64_MACHINES = ["aarch64", "arm64"]
ARM_32_MACHINES = ["armhf", "armv8", "armv7l", "armv7", "armv6"]

X86_ANY_MACHINES = X86_MACHINES + X86_64_MACHINES
ARM_ANY_MACHINES = ARM_32_MACHINES + ARM_64_MACHINES

def get_arch():
    machine = platform.machine().lower()
    if machine in X86_ANY_MACHINES:
        if platform.architecture()[0] == "32bit":
            return "x86"
        if platform.architecture()[0] == "64bit":
            return "x86-64"
    if machine.startswith("power"):
        if platform.architecture()[0] == "32bit":
            return "PPC"
    if machine in ARM_ANY_MACHINES:
        if platform.architecture()[0] == "32bit":
            return "ARM32"
        if platform.architecture()[0] == "64bit":
            return "ARM64"
    raise Exception(f"Unknown platform for machine {machine}")
    # return 'Unknown'


if __name__ == '__main__':
    arch = get_arch()
    print(arch)
    sys.exit(0)