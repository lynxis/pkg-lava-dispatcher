"""
This is an ugly hack, the uboot commands for a given board type and the board
type of a test machine need to come from the device registry.  This is an
easy way to look it up for now though, just to show the rest of the code
around it
"""

class Board:
    pass

class BeagleBoard(Board):
    uboot_cmds = ["mmc init",
        "setenv bootcmd 'fatload mmc 0:3 0x80000000 uImage; fatload mmc "
        "0:3 0x81600000 uInitrd; bootm 0x80000000 0x81600000'",
        "setenv bootargs ' console=tty0 console=ttyO2,115200n8 "
        "root=LABEL=testrootfs rootwait ro earlyprintk fixrtc nocompcache "
        "vram=12M omapfb.debug=y omapfb.mode=dvi:1280x720MR-16@60'",
        "boot"]
    type = "beagle"

class PandaBoard(Board):
    uboot_cmds = ["mmc init",
        "setenv bootcmd 'fatload mmc 0:5 0x80200000 uImage; fatload mmc "
        "0:5 0x81600000 uInitrd; bootm 0x80200000 0x81600000'",
        "setenv bootargs ' console=tty0 console=ttyO2,115200n8 "
        "root=LABEL=testrootfs rootwait ro earlyprintk fixrtc nocompcache "
        "vram=32M omapfb.vram=0:8M mem=463M ip=none'",
        "boot"]
    type = "panda"

class Mx51evkBoard(Board):
    uboot_cmds = ["mmc init",
        "setenv bootcmd 'fatload mmc 0:5 0x90800000 uImage; fatload mmc "
        "0:5 0x90800000 uInitrd; bootm 0x90000000 0x90800000'",
        "setenv bootargs ' console=tty0 console=ttymxc0,115200n8 "
        "root=LABEL=testrootfs rootwait ro'",
        "boot"]
    type = "mx51evk"

#Here, it still needs to maintain a map from boardid to board, for there is only
#boardid in jobfile.json
BOARDS = {
        "panda01": PandaBoard,
        "panda02": PandaBoard,
        "beagle01": BeagleBoard,
        "bbg01": Mx51evkBoard,
        }

#Main LAVA server IP in the boards farm
LAVA_SERVER_IP = "192.168.1.10"
#Location for hosting rootfs/boot tarballs extracted from images
LAVA_IMAGE_TMPDIR = "/linaro/images/tmp"
#URL where LAVA_IMAGE_TMPDIR can be accessed remotely
LAVA_IMAGE_URL = "http://%s/images/tmp" % LAVA_SERVER_IP

#Master image recognization string
MASTER_STR = "root@master:"
#Test image recognization string
TESTER_STR = "root@linaro:"