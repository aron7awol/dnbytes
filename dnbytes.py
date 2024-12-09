#dialnorm
dn2 = 37
dn6 = 31
dn8 = 21
dn16 = 31

#mix level
ml2 = 99
ml6 = 105
ml8 = 105
ml16 = 105

drc = "0" #DRC default on/off (2ch)

#DRC startup gain
drcsg = "1000000" #0.06
#drcsg = "0000000" #1.0
#drcsg = "1111100" #0.84
#drcsg = "0000100" #1.19

bdn2 = format(dn2, '06b')
bdn6 = format(dn6, '05b')
bdn8 = format(dn8, '05b')
bdn16 = format(dn16, '05b')
bml2 = format(ml2-70, '06b')
bml6 = format(ml6-70, '06b')
bml8 = format(ml8-70, '06b')
bml16 = format(ml16-70, '06b')

b22 = "000000" + drc + "0"  #reserved 000000, 6ch_control_enabled 0
b23 = "00" + drcsg[:6]      #8ch_control_enabled 0, reserved 0
b24 = drcsg[6:] + bdn2 + bml2[:1]
b25 = bml2[1:] + bdn6[:3]
b26 = bdn6[3:] + bml6
b27 = "00000" + bdn8[:3]    #6ch_source_format 00000
b28 = bdn8[3:] + bml8
b29 = "00000001"            #8ch_source_format 000000, reserved 0, extra_channel_meaning_present 1
b30 = "0001" + bdn16[:4]    #extra_channel_meaning_length 0001
b31 = bdn16[4:] + bml16 +"0"

h22 = "{0:0>2X}".format(int(b22, 2))
h23 = "{0:0>2X}".format(int(b23, 2))
h24 = "{0:0>2X}".format(int(b24, 2))
h25 = "{0:0>2X}".format(int(b25, 2))
h26 = "{0:0>2X}".format(int(b26, 2))
h27 = "{0:0>2X}".format(int(b27, 2))
h28 = "{0:0>2X}".format(int(b28, 2))
h29 = "{0:0>2X}".format(int(b29, 2))
h30 = "{0:0>2X}".format(int(b30, 2))
h31 = "{0:0>2X}".format(int(b31, 2))

print("22:", b22, h22)
print("23:", b23, h23)
print("24:", b24, h24)
print("25:", b25, h25)
print("26:", b26, h26)
print("27:", b27, h27)
print("28:", b28, h28)
print("29:", b29, h29)
print("30:", b30, h30)
print("31:", b31, h31)