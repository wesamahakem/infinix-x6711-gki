# GKI 5.10.198 Kernel for Infinix Note 30 5G (X6711)

A custom GKI kernel build preserving 100% MediaTek OEM hardware sensor compatibility while enabling:
* **Droidspaces full container support** (PID, IPC, USER namespaces, devtmpfs, Macvlan, IPv6 NAT, UFW, Fail2ban)
* **SUSFS root hiding support** (KernelSU-Next compatible)
* **Zero ABI breakage**: Built from exact Transsion/Google commit `85b72e945a8d` with kABI slot reservations (Droidspaces on slots 1-3, SUSFS on slot 7)
* **MediaTek compressed format**: `Image.gz` bundled into an `AnyKernel3.zip` flashable via PBRP Recovery

## Flashing Instructions
1. Download `AnyKernel3-X6711-GKI-5.10.198-Droidspaces-SUSFS.zip` from GitHub Actions Artifacts.
2. Boot into PBRP Recovery.
3. Tap **Install** (or **Install Kernel**) -> Select the `.zip` file -> Swipe to Flash.
4. Reboot to System.
