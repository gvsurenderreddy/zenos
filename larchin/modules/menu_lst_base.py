menu_lst_base = """# Config file for GRUB - The GNU GRand Unified Bootloader
# /boot/grub/menu.lst

# DEVICE NAME CONVERSIONS
#
#  Linux           Grub
# -------------------------
#  /dev/fd0        (fd0)
#  /dev/hda        (hd0)
#  /dev/hdb2       (hd1,1)
#  /dev/hda3       (hd0,2)
#

#  FRAMEBUFFER RESOLUTION SETTINGS
#     +-------------------------------------------------+
#          | 640x480    800x600    1024x768   1280x1024
#      ----+--------------------------------------------
#      256 | 0x301=769  0x303=771  0x305=773   0x307=775
#      32K | 0x310=784  0x313=787  0x316=790   0x319=793
#      64K | 0x311=785  0x314=788  0x317=791   0x31A=794
#      16M | 0x312=786  0x315=789  0x318=792   0x31B=795
#     +-------------------------------------------------+

# general configuration:
timeout   5
default   0
color light-blue/black light-cyan/blue

# boot sections follow
# each is implicitly numbered from 0 in the order of appearance below
#
#-*

#--- without separate boot partition
#title  Arch Linux  [/boot/vmlinuz26]
#root   (hd0,2)
#kernel /boot/vmlinuz26 root=/dev/hda3 ro
#initrd /boot/kernel26.img

#--- with separate boot partition
#title  Arch Linux  [/boot/vmlinuz26]
#root   (hd0,0)
#kernel /vmlinuz26 root=/dev/hda3 ro
#initrd /kernel26.img

#title Windows
#rootnoverify (hd0,0)
#makeactive
#chainloader +1

"""
