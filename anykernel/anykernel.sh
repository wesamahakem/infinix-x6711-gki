### AnyKernel3 Ramdisk Mod Script
## Infinix Note 30 5G (X6711) - GKI 5.10.198 (Droidspaces + SUSFS)

### AnyKernel setup
# global properties
properties() { '
kernel.string=Infinix Note 30 5G (X6711) GKI 5.10.198 [Droidspaces + SUSFS]
do.devicecheck=0
do.modules=0
do.systemless=1
do.cleanup=1
do.cleanuponabort=0
device.name1=X6711
device.name2=Infinix-X6711
device.name3=Infinix_X6711
supported.versions=12,12L,13,14,15,16
supported.patchlevels=
supported.vendorpatchlevels=
'; } # end properties

### AnyKernel install
# boot shell variables
BLOCK=/dev/block/by-name/boot;
[ ! -e "$BLOCK" ] && BLOCK=/dev/block/bootdevice/by-name/boot;
IS_SLOT_DEVICE=auto;
RAMDISK_COMPRESSION=auto;
PATCH_VBMETA_FLAG=auto;

# import functions/variables and setup patching - see for reference (DO NOT REMOVE)
. tools/ak3-core.sh;

# boot install
split_boot;
flash_boot;
