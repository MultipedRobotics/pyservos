EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:serial-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L 74LS126 U3
U 2 1 5A7F13E9
P 5250 2150
F 0 "U3" H 5350 2350 50  0000 C CNN
F 1 "74LS126" H 5500 2000 50  0000 C CNN
F 2 "Housings_SOIC:SOIC-14_3.9x8.7mm_Pitch1.27mm" H 5250 2150 50  0001 C CNN
F 3 "" H 5250 2150 50  0001 C CNN
	2    5250 2150
	1    0    0    -1  
$EndComp
$Comp
L 74LS126 U3
U 1 1 5A7F1432
P 4800 3150
F 0 "U3" H 4900 3350 50  0000 C CNN
F 1 "74LS126" H 5050 3000 50  0000 C CNN
F 2 "Housings_SOIC:SOIC-14_3.9x8.7mm_Pitch1.27mm" H 4800 3150 50  0001 C CNN
F 3 "" H 4800 3150 50  0001 C CNN
	1    4800 3150
	1    0    0    -1  
$EndComp
$Comp
L 74LS126 U3
U 4 1 5A7F1484
P 7100 2250
F 0 "U3" H 7200 2450 50  0000 C CNN
F 1 "74LS126" H 7350 2100 50  0000 C CNN
F 2 "Housings_SOIC:SOIC-14_3.9x8.7mm_Pitch1.27mm" H 7100 2250 50  0001 C CNN
F 3 "" H 7100 2250 50  0001 C CNN
	4    7100 2250
	1    0    0    -1  
$EndComp
$Comp
L 74LS126 U3
U 3 1 5A7F14E1
P 7050 3100
F 0 "U3" H 7150 3300 50  0000 C CNN
F 1 "74LS126" H 7300 2950 50  0000 C CNN
F 2 "Housings_SOIC:SOIC-14_3.9x8.7mm_Pitch1.27mm" H 7050 3100 50  0001 C CNN
F 3 "" H 7050 3100 50  0001 C CNN
	3    7050 3100
	1    0    0    -1  
$EndComp
$Comp
L Conn_01x05 J2
U 1 1 5A7F1515
P 4950 1150
F 0 "J2" H 4950 1350 50  0000 C CNN
F 1 "Serial" H 4950 850 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x05_Pitch2.54mm" H 4950 1150 50  0001 C CNN
F 3 "" H 4950 1150 50  0001 C CNN
	1    4950 1150
	-1   0    0    1   
$EndComp
$Comp
L R R7
U 1 1 5A7F169D
P 8000 2850
F 0 "R7" V 8080 2850 50  0000 C CNN
F 1 "10k" V 8000 2850 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 7930 2850 50  0001 C CNN
F 3 "" H 8000 2850 50  0001 C CNN
	1    8000 2850
	1    0    0    -1  
$EndComp
$Comp
L LM317_3PinPackage U2
U 1 1 5A7F16FB
P 3400 1550
F 0 "U2" H 3250 1675 50  0000 C CNN
F 1 "LM317" H 3400 1675 50  0000 L CNN
F 2 "TO_SOT_Packages_THT:TO-220-3_Horizontal" H 3400 1800 50  0001 C CIN
F 3 "" H 3400 1550 50  0001 C CNN
	1    3400 1550
	1    0    0    -1  
$EndComp
$Comp
L R R2
U 1 1 5A7F1770
P 3800 1750
F 0 "R2" V 3880 1750 50  0000 C CNN
F 1 "330" V 3800 1750 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 3730 1750 50  0001 C CNN
F 3 "" H 3800 1750 50  0001 C CNN
	1    3800 1750
	1    0    0    -1  
$EndComp
$Comp
L R R3
U 1 1 5A7F17CA
P 3800 2150
F 0 "R3" V 3880 2150 50  0000 C CNN
F 1 "1.8k" V 3800 2150 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 3730 2150 50  0001 C CNN
F 3 "" H 3800 2150 50  0001 C CNN
	1    3800 2150
	1    0    0    -1  
$EndComp
$Comp
L Barrel_Jack J1
U 1 1 5A7F181C
P 1350 1650
F 0 "J1" H 1350 1860 50  0000 C CNN
F 1 "12V Pwr" H 1350 1475 50  0000 C CNN
F 2 "Connectors:BARREL_JACK" H 1400 1610 50  0001 C CNN
F 3 "" H 1400 1610 50  0001 C CNN
	1    1350 1650
	1    0    0    -1  
$EndComp
$Comp
L CP C2
U 1 1 5A7F1A59
P 3000 1800
F 0 "C2" H 3025 1900 50  0000 L CNN
F 1 "10" H 3025 1700 50  0000 L CNN
F 2 "Capacitors_THT:CP_Radial_D6.3mm_P2.50mm" H 3038 1650 50  0001 C CNN
F 3 "" H 3000 1800 50  0001 C CNN
	1    3000 1800
	1    0    0    -1  
$EndComp
$Comp
L C C4
U 1 1 5A7F1ABA
P 4100 1800
F 0 "C4" H 4125 1900 50  0000 L CNN
F 1 ".1" H 4125 1700 50  0000 L CNN
F 2 "Capacitors_SMD:C_1206_HandSoldering" H 4138 1650 50  0001 C CNN
F 3 "" H 4100 1800 50  0001 C CNN
	1    4100 1800
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR01
U 1 1 5A7F1C04
P 1800 1850
F 0 "#PWR01" H 1800 1600 50  0001 C CNN
F 1 "GND" H 1800 1700 50  0000 C CNN
F 2 "" H 1800 1850 50  0001 C CNN
F 3 "" H 1800 1850 50  0001 C CNN
	1    1800 1850
	1    0    0    -1  
$EndComp
$Comp
L PWR_FLAG #FLG02
U 1 1 5A7F1CAE
P 4100 4300
F 0 "#FLG02" H 4100 4375 50  0001 C CNN
F 1 "PWR_FLAG" H 4100 4450 50  0000 C CNN
F 2 "" H 4100 4300 50  0001 C CNN
F 3 "" H 4100 4300 50  0001 C CNN
	1    4100 4300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR03
U 1 1 5A7F1D53
P 4100 4450
F 0 "#PWR03" H 4100 4200 50  0001 C CNN
F 1 "GND" H 4100 4300 50  0000 C CNN
F 2 "" H 4100 4450 50  0001 C CNN
F 3 "" H 4100 4450 50  0001 C CNN
	1    4100 4450
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR04
U 1 1 5A7F1DCD
P 2950 4300
F 0 "#PWR04" H 2950 4150 50  0001 C CNN
F 1 "VCC" H 2950 4450 50  0000 C CNN
F 2 "" H 2950 4300 50  0001 C CNN
F 3 "" H 2950 4300 50  0001 C CNN
	1    2950 4300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR05
U 1 1 5A7F209B
P 3800 2450
F 0 "#PWR05" H 3800 2200 50  0001 C CNN
F 1 "GND" H 3800 2300 50  0000 C CNN
F 2 "" H 3800 2450 50  0001 C CNN
F 3 "" H 3800 2450 50  0001 C CNN
	1    3800 2450
	1    0    0    -1  
$EndComp
$Comp
L +8V #PWR06
U 1 1 5A7F21C8
P 4300 1350
F 0 "#PWR06" H 4300 1200 50  0001 C CNN
F 1 "+8V" H 4300 1490 50  0000 C CNN
F 2 "" H 4300 1350 50  0001 C CNN
F 3 "" H 4300 1350 50  0001 C CNN
	1    4300 1350
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR07
U 1 1 5A7F28F9
P 3250 3400
F 0 "#PWR07" H 3250 3150 50  0001 C CNN
F 1 "GND" H 3250 3250 50  0000 C CNN
F 2 "" H 3250 3400 50  0001 C CNN
F 3 "" H 3250 3400 50  0001 C CNN
	1    3250 3400
	1    0    0    -1  
$EndComp
$Comp
L C C3
U 1 1 5A7F2931
P 3650 3250
F 0 "C3" H 3675 3350 50  0000 L CNN
F 1 ".1" H 3675 3150 50  0000 L CNN
F 2 "Capacitors_SMD:C_1206_HandSoldering" H 3688 3100 50  0001 C CNN
F 3 "" H 3650 3250 50  0001 C CNN
	1    3650 3250
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR08
U 1 1 5A7F29A5
P 3750 2950
F 0 "#PWR08" H 3750 2800 50  0001 C CNN
F 1 "+5V" H 3750 3090 50  0000 C CNN
F 2 "" H 3750 2950 50  0001 C CNN
F 3 "" H 3750 2950 50  0001 C CNN
	1    3750 2950
	1    0    0    -1  
$EndComp
$Comp
L C C1
U 1 1 5A7F2B39
P 2850 3250
F 0 "C1" H 2875 3350 50  0000 L CNN
F 1 ".1" H 2875 3150 50  0000 L CNN
F 2 "Capacitors_SMD:C_1206_HandSoldering" H 2888 3100 50  0001 C CNN
F 3 "" H 2850 3250 50  0001 C CNN
	1    2850 3250
	1    0    0    -1  
$EndComp
$Comp
L Conn_01x03 J4
U 1 1 5A7F2FF1
P 7100 1450
F 0 "J4" H 7100 1650 50  0000 C CNN
F 1 "AX-12A" H 7100 1250 50  0000 C CNN
F 2 "Connectors_Molex:Molex_SPOX-5267_22-03-5035_03x2.54mm_Straight" H 7100 1450 50  0001 C CNN
F 3 "" H 7100 1450 50  0001 C CNN
	1    7100 1450
	1    0    0    -1  
$EndComp
NoConn ~ 4350 3150
NoConn ~ 4800 3450
NoConn ~ 5250 3150
Text GLabel 5350 850  2    60   Output ~ 0
DTR
$Comp
L GND #PWR09
U 1 1 5A7F3586
P 5350 1400
F 0 "#PWR09" H 5350 1150 50  0001 C CNN
F 1 "GND" H 5350 1250 50  0000 C CNN
F 2 "" H 5350 1400 50  0001 C CNN
F 3 "" H 5350 1400 50  0001 C CNN
	1    5350 1400
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR010
U 1 1 5A7F37B7
P 6750 1600
F 0 "#PWR010" H 6750 1350 50  0001 C CNN
F 1 "GND" H 6750 1450 50  0000 C CNN
F 2 "" H 6750 1600 50  0001 C CNN
F 3 "" H 6750 1600 50  0001 C CNN
	1    6750 1600
	1    0    0    -1  
$EndComp
Text GLabel 6700 1350 0    60   BiDi ~ 0
DATA
$Comp
L +8V #PWR011
U 1 1 5A7F3824
P 6500 850
F 0 "#PWR011" H 6500 700 50  0001 C CNN
F 1 "+8V" H 6500 990 50  0000 C CNN
F 2 "" H 6500 850 50  0001 C CNN
F 3 "" H 6500 850 50  0001 C CNN
	1    6500 850 
	1    0    0    -1  
$EndComp
Text GLabel 5100 2550 0    60   Input ~ 0
DTR
Text GLabel 6550 2250 0    60   Input ~ 0
TXO
Text GLabel 5800 2150 2    60   Output ~ 0
RXI
Text GLabel 4700 2150 0    60   BiDi ~ 0
DATA
Text GLabel 7650 2250 2    60   BiDi ~ 0
DATA
$Comp
L +5V #PWR012
U 1 1 5A7F3FF2
P 8000 2600
F 0 "#PWR012" H 8000 2450 50  0001 C CNN
F 1 "+5V" H 8000 2740 50  0000 C CNN
F 2 "" H 8000 2600 50  0001 C CNN
F 3 "" H 8000 2600 50  0001 C CNN
	1    8000 2600
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR013
U 1 1 5A7F402D
P 6500 3300
F 0 "#PWR013" H 6500 3050 50  0001 C CNN
F 1 "GND" H 6500 3150 50  0000 C CNN
F 2 "" H 6500 3300 50  0001 C CNN
F 3 "" H 6500 3300 50  0001 C CNN
	1    6500 3300
	1    0    0    -1  
$EndComp
Text GLabel 6950 3550 0    60   Input ~ 0
DTR
$Comp
L PWR_FLAG #FLG014
U 1 1 5A7F46C3
P 3700 4450
F 0 "#FLG014" H 3700 4525 50  0001 C CNN
F 1 "PWR_FLAG" H 3700 4600 50  0000 C CNN
F 2 "" H 3700 4450 50  0001 C CNN
F 3 "" H 3700 4450 50  0001 C CNN
	1    3700 4450
	-1   0    0    1   
$EndComp
$Comp
L LED D2
U 1 1 5A862706
P 5750 2450
F 0 "D2" H 5750 2550 50  0000 C CNN
F 1 "RX" H 5750 2350 50  0000 C CNN
F 2 "LEDs:LED_1206_HandSoldering" H 5750 2450 50  0001 C CNN
F 3 "" H 5750 2450 50  0001 C CNN
	1    5750 2450
	0    -1   -1   0   
$EndComp
$Comp
L LED D3
U 1 1 5A862765
P 6300 2600
F 0 "D3" H 6300 2700 50  0000 C CNN
F 1 "TX" H 6300 2500 50  0000 C CNN
F 2 "LEDs:LED_1206_HandSoldering" H 6300 2600 50  0001 C CNN
F 3 "" H 6300 2600 50  0001 C CNN
	1    6300 2600
	0    -1   -1   0   
$EndComp
$Comp
L R R4
U 1 1 5A8627B6
P 5750 2850
F 0 "R4" V 5830 2850 50  0000 C CNN
F 1 "330" V 5750 2850 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 5680 2850 50  0001 C CNN
F 3 "" H 5750 2850 50  0001 C CNN
	1    5750 2850
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR015
U 1 1 5A8628F6
P 5750 3100
F 0 "#PWR015" H 5750 2850 50  0001 C CNN
F 1 "GND" H 5750 2950 50  0000 C CNN
F 2 "" H 5750 3100 50  0001 C CNN
F 3 "" H 5750 3100 50  0001 C CNN
	1    5750 3100
	1    0    0    -1  
$EndComp
$Comp
L R R5
U 1 1 5A862D7C
P 6300 3000
F 0 "R5" V 6380 3000 50  0000 C CNN
F 1 "330" V 6300 3000 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 6230 3000 50  0001 C CNN
F 3 "" H 6300 3000 50  0001 C CNN
	1    6300 3000
	1    0    0    -1  
$EndComp
$Comp
L Conn_01x03 J3
U 1 1 5A863A11
P 7100 850
F 0 "J3" H 7100 1050 50  0000 C CNN
F 1 "XL-320" H 7100 650 50  0000 C CNN
F 2 "Connectors_Molex:Molex_MicroLatch-53253-0370_03x2.00mm_Straight" H 7100 850 50  0001 C CNN
F 3 "" H 7100 850 50  0001 C CNN
	1    7100 850 
	1    0    0    -1  
$EndComp
$Comp
L AP1117-50 U1
U 1 1 5A864FB2
P 3250 3000
F 0 "U1" H 3100 3125 50  0000 C CNN
F 1 "AP1117-50" H 3250 3125 50  0000 L CNN
F 2 "TO_SOT_Packages_SMD:SOT-223-3Lead_TabPin2" H 3250 3200 50  0001 C CNN
F 3 "" H 3350 2750 50  0001 C CNN
	1    3250 3000
	1    0    0    -1  
$EndComp
$Comp
L PWR_FLAG #FLG016
U 1 1 5A864DA9
P 3200 4450
F 0 "#FLG016" H 3200 4525 50  0001 C CNN
F 1 "PWR_FLAG" H 3200 4600 50  0000 C CNN
F 2 "" H 3200 4450 50  0001 C CNN
F 3 "" H 3200 4450 50  0001 C CNN
	1    3200 4450
	-1   0    0    1   
$EndComp
$Comp
L +5V #PWR017
U 1 1 5A864DF3
P 3200 4300
F 0 "#PWR017" H 3200 4150 50  0001 C CNN
F 1 "+5V" H 3200 4440 50  0000 C CNN
F 2 "" H 3200 4300 50  0001 C CNN
F 3 "" H 3200 4300 50  0001 C CNN
	1    3200 4300
	1    0    0    -1  
$EndComp
$Comp
L +12V #PWR018
U 1 1 5A8A6102
P 1800 1450
F 0 "#PWR018" H 1800 1300 50  0001 C CNN
F 1 "+12V" H 1800 1590 50  0000 C CNN
F 2 "" H 1800 1450 50  0001 C CNN
F 3 "" H 1800 1450 50  0001 C CNN
	1    1800 1450
	1    0    0    -1  
$EndComp
$Comp
L +12V #PWR019
U 1 1 5A8A616A
P 6200 1400
F 0 "#PWR019" H 6200 1250 50  0001 C CNN
F 1 "+12V" H 6200 1540 50  0000 C CNN
F 2 "" H 6200 1400 50  0001 C CNN
F 3 "" H 6200 1400 50  0001 C CNN
	1    6200 1400
	1    0    0    -1  
$EndComp
$Comp
L +12V #PWR020
U 1 1 5A8A6C74
P 2650 2950
F 0 "#PWR020" H 2650 2800 50  0001 C CNN
F 1 "+12V" H 2650 3090 50  0000 C CNN
F 2 "" H 2650 2950 50  0001 C CNN
F 3 "" H 2650 2950 50  0001 C CNN
	1    2650 2950
	1    0    0    -1  
$EndComp
$Comp
L +12V #PWR021
U 1 1 5A8A7107
P 2650 1450
F 0 "#PWR021" H 2650 1300 50  0001 C CNN
F 1 "+12V" H 2650 1590 50  0000 C CNN
F 2 "" H 2650 1450 50  0001 C CNN
F 3 "" H 2650 1450 50  0001 C CNN
	1    2650 1450
	1    0    0    -1  
$EndComp
$Comp
L +12V #PWR022
U 1 1 5A8A772A
P 3700 4300
F 0 "#PWR022" H 3700 4150 50  0001 C CNN
F 1 "+12V" H 3700 4440 50  0000 C CNN
F 2 "" H 3700 4300 50  0001 C CNN
F 3 "" H 3700 4300 50  0001 C CNN
	1    3700 4300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR023
U 1 1 5A8A8E66
P 1850 3250
F 0 "#PWR023" H 1850 3000 50  0001 C CNN
F 1 "GND" H 1850 3100 50  0000 C CNN
F 2 "" H 1850 3250 50  0001 C CNN
F 3 "" H 1850 3250 50  0001 C CNN
	1    1850 3250
	1    0    0    -1  
$EndComp
$Comp
L R R1
U 1 1 5A8A8EB0
P 1850 3000
F 0 "R1" V 1930 3000 50  0000 C CNN
F 1 "330" V 1850 3000 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 1780 3000 50  0001 C CNN
F 3 "" H 1850 3000 50  0001 C CNN
	1    1850 3000
	1    0    0    -1  
$EndComp
$Comp
L LED D1
U 1 1 5A8A8F0B
P 1850 2600
F 0 "D1" H 1850 2700 50  0000 C CNN
F 1 "PWR" H 1850 2500 50  0000 C CNN
F 2 "LEDs:LED_1206_HandSoldering" H 1850 2600 50  0001 C CNN
F 3 "" H 1850 2600 50  0001 C CNN
	1    1850 2600
	0    -1   -1   0   
$EndComp
$Comp
L +5V #PWR024
U 1 1 5A8A9380
P 1850 2350
F 0 "#PWR024" H 1850 2200 50  0001 C CNN
F 1 "+5V" H 1850 2490 50  0000 C CNN
F 2 "" H 1850 2350 50  0001 C CNN
F 3 "" H 1850 2350 50  0001 C CNN
	1    1850 2350
	1    0    0    -1  
$EndComp
Wire Wire Line
	1800 1650 1800 1850
Wire Wire Line
	2950 4300 2950 4400
Wire Wire Line
	4100 4300 4100 4450
Wire Wire Line
	3700 1550 4300 1550
Wire Wire Line
	4300 1550 4300 1350
Wire Wire Line
	3800 1600 3800 1550
Connection ~ 3800 1550
Wire Wire Line
	3800 1900 3800 2000
Wire Wire Line
	3400 1850 3400 1950
Wire Wire Line
	3400 1950 3800 1950
Connection ~ 3800 1950
Wire Wire Line
	3000 1650 3000 1550
Wire Wire Line
	3800 2300 3800 2450
Wire Wire Line
	3000 1950 3000 2350
Wire Wire Line
	3000 2350 4100 2350
Connection ~ 3800 2350
Wire Wire Line
	4100 1650 4100 1550
Connection ~ 4100 1550
Wire Wire Line
	4100 2350 4100 1950
Wire Wire Line
	3250 3300 3250 3400
Wire Wire Line
	3550 3000 3750 3000
Wire Wire Line
	3750 3000 3750 2950
Wire Wire Line
	3650 3100 3650 3000
Connection ~ 3650 3000
Wire Wire Line
	2850 3400 3650 3400
Wire Wire Line
	2650 3000 2950 3000
Wire Wire Line
	2850 3100 2850 3000
Connection ~ 2850 3000
Connection ~ 3250 3400
Wire Wire Line
	5150 1150 5350 1150
Wire Wire Line
	5150 1050 5250 1050
Wire Wire Line
	5250 1050 5250 1000
Wire Wire Line
	5250 1000 5350 1000
Wire Wire Line
	5150 950  5250 950 
Wire Wire Line
	5250 950  5250 850 
Wire Wire Line
	5250 850  5350 850 
Wire Wire Line
	6700 1350 6900 1350
Wire Wire Line
	6900 850  6500 850 
Wire Wire Line
	6750 1550 6900 1550
Wire Wire Line
	6750 1550 6750 1600
Wire Wire Line
	7550 2250 7650 2250
Wire Wire Line
	6550 2250 6650 2250
Wire Wire Line
	5700 2150 5800 2150
Wire Wire Line
	4700 2150 4800 2150
Wire Wire Line
	5100 2550 5250 2550
Wire Wire Line
	5250 2550 5250 2450
Wire Wire Line
	7100 2550 7100 2650
Wire Wire Line
	7100 2650 7600 2650
Wire Wire Line
	7600 2650 7600 3100
Wire Wire Line
	7500 3100 8000 3100
Wire Wire Line
	6500 3100 6500 3300
Wire Wire Line
	6500 3100 6600 3100
Wire Wire Line
	8000 3100 8000 3000
Connection ~ 7600 3100
Wire Wire Line
	8000 2700 8000 2600
Wire Wire Line
	6950 3550 7050 3550
Wire Wire Line
	7050 3550 7050 3400
Wire Wire Line
	5750 2300 5750 2150
Connection ~ 5750 2150
Wire Wire Line
	5750 2600 5750 2700
Wire Wire Line
	5750 3000 5750 3100
Wire Wire Line
	6300 2450 6300 2400
Wire Wire Line
	6300 2400 6600 2400
Wire Wire Line
	6600 2400 6600 2250
Connection ~ 6600 2250
Wire Wire Line
	6300 2750 6300 2850
Wire Wire Line
	6300 3150 6300 3200
Wire Wire Line
	6300 3200 6500 3200
Connection ~ 6500 3200
Connection ~ 6850 1550
Connection ~ 6750 1350
Wire Wire Line
	3200 4300 3200 4450
Wire Wire Line
	6900 1450 6200 1450
Wire Wire Line
	6200 1450 6200 1400
Wire Wire Line
	1650 1750 1800 1750
Wire Wire Line
	1650 1650 1800 1650
Connection ~ 1800 1750
Wire Wire Line
	1650 1550 1800 1550
Wire Wire Line
	1800 1550 1800 1450
Wire Wire Line
	2650 3000 2650 2950
Wire Wire Line
	2650 1550 3100 1550
Connection ~ 3000 1550
Wire Wire Line
	2650 1550 2650 1450
Wire Wire Line
	3700 4450 3700 4300
Wire Wire Line
	1850 2350 1850 2450
Wire Wire Line
	1850 2750 1850 2850
Wire Wire Line
	1850 3150 1850 3250
Wire Wire Line
	6900 750  6850 750 
Wire Wire Line
	6850 750  6850 1550
Wire Wire Line
	6900 950  6750 950 
Wire Wire Line
	6750 950  6750 1350
Wire Wire Line
	2950 4400 3200 4400
Connection ~ 3200 4400
Text GLabel 9350 4450 0    60   Input ~ 0
TXO3v3
Text GLabel 7700 4500 0    60   Output ~ 0
RXI3v3
$Comp
L +3.3V #PWR025
U 1 1 5A9B210E
P 5800 1200
F 0 "#PWR025" H 5800 1050 50  0001 C CNN
F 1 "+3.3V" H 5800 1340 50  0000 C CNN
F 2 "" H 5800 1200 50  0001 C CNN
F 3 "" H 5800 1200 50  0001 C CNN
	1    5800 1200
	1    0    0    -1  
$EndComp
$Comp
L +3.3V #PWR026
U 1 1 5A9B2174
P 7850 3700
F 0 "#PWR026" H 7850 3550 50  0001 C CNN
F 1 "+3.3V" H 7850 3840 50  0000 C CNN
F 2 "" H 7850 3700 50  0001 C CNN
F 3 "" H 7850 3700 50  0001 C CNN
	1    7850 3700
	1    0    0    -1  
$EndComp
$Comp
L R R6
U 1 1 5A9B21D3
P 7850 3950
F 0 "R6" V 7930 3950 50  0000 C CNN
F 1 "10k" V 7850 3950 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 7780 3950 50  0001 C CNN
F 3 "" H 7850 3950 50  0001 C CNN
	1    7850 3950
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR027
U 1 1 5A9B24DF
P 8400 4000
F 0 "#PWR027" H 8400 3850 50  0001 C CNN
F 1 "+5V" H 8400 4140 50  0000 C CNN
F 2 "" H 8400 4000 50  0001 C CNN
F 3 "" H 8400 4000 50  0001 C CNN
	1    8400 4000
	1    0    0    -1  
$EndComp
$Comp
L R R8
U 1 1 5A9B2541
P 8400 4250
F 0 "R8" V 8480 4250 50  0000 C CNN
F 1 "10k" V 8400 4250 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 8330 4250 50  0001 C CNN
F 3 "" H 8400 4250 50  0001 C CNN
	1    8400 4250
	1    0    0    -1  
$EndComp
Text GLabel 8500 4500 2    60   Output ~ 0
RXI
Text GLabel 10150 4450 2    60   Input ~ 0
TXO
Wire Wire Line
	7700 4500 7900 4500
Wire Wire Line
	7850 3700 7850 3800
Wire Wire Line
	7850 4100 7850 4500
Connection ~ 7850 4500
Wire Wire Line
	8100 4200 8100 4150
Wire Wire Line
	8100 4150 7850 4150
Connection ~ 7850 4150
Wire Wire Line
	8300 4500 8500 4500
Wire Wire Line
	8400 4400 8400 4500
Connection ~ 8400 4500
Wire Wire Line
	8400 4100 8400 4000
$Comp
L +3.3V #PWR028
U 1 1 5A9B3CAC
P 9500 3650
F 0 "#PWR028" H 9500 3500 50  0001 C CNN
F 1 "+3.3V" H 9500 3790 50  0000 C CNN
F 2 "" H 9500 3650 50  0001 C CNN
F 3 "" H 9500 3650 50  0001 C CNN
	1    9500 3650
	1    0    0    -1  
$EndComp
$Comp
L R R9
U 1 1 5A9B3CB2
P 9500 3900
F 0 "R9" V 9580 3900 50  0000 C CNN
F 1 "10k" V 9500 3900 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 9430 3900 50  0001 C CNN
F 3 "" H 9500 3900 50  0001 C CNN
	1    9500 3900
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR029
U 1 1 5A9B3CB8
P 10050 3950
F 0 "#PWR029" H 10050 3800 50  0001 C CNN
F 1 "+5V" H 10050 4090 50  0000 C CNN
F 2 "" H 10050 3950 50  0001 C CNN
F 3 "" H 10050 3950 50  0001 C CNN
	1    10050 3950
	1    0    0    -1  
$EndComp
$Comp
L R R10
U 1 1 5A9B3CBE
P 10050 4200
F 0 "R10" V 10130 4200 50  0000 C CNN
F 1 "10k" V 10050 4200 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 9980 4200 50  0001 C CNN
F 3 "" H 10050 4200 50  0001 C CNN
	1    10050 4200
	1    0    0    -1  
$EndComp
Wire Wire Line
	9350 4450 9550 4450
Wire Wire Line
	9500 3650 9500 3750
Wire Wire Line
	9500 4050 9500 4450
Connection ~ 9500 4450
Wire Wire Line
	9750 4150 9750 4100
Wire Wire Line
	9750 4100 9500 4100
Connection ~ 9500 4100
Wire Wire Line
	9950 4450 10150 4450
Wire Wire Line
	10050 4350 10050 4450
Connection ~ 10050 4450
Wire Wire Line
	10050 4050 10050 3950
Wire Wire Line
	5150 1250 5800 1250
Wire Wire Line
	5800 1250 5800 1200
Wire Wire Line
	5150 1350 5350 1350
Wire Wire Line
	5350 1350 5350 1400
$Comp
L +3.3V #PWR030
U 1 1 5A9B4AC8
P 4550 4300
F 0 "#PWR030" H 4550 4150 50  0001 C CNN
F 1 "+3.3V" H 4550 4440 50  0000 C CNN
F 2 "" H 4550 4300 50  0001 C CNN
F 3 "" H 4550 4300 50  0001 C CNN
	1    4550 4300
	1    0    0    -1  
$EndComp
$Comp
L PWR_FLAG #FLG031
U 1 1 5A9B4C86
P 4550 4450
F 0 "#FLG031" H 4550 4525 50  0001 C CNN
F 1 "PWR_FLAG" H 4550 4600 50  0000 C CNN
F 2 "" H 4550 4450 50  0001 C CNN
F 3 "" H 4550 4450 50  0001 C CNN
	1    4550 4450
	-1   0    0    1   
$EndComp
Wire Wire Line
	4550 4450 4550 4300
Text GLabel 5350 1000 2    60   Output ~ 0
RXI3v3
Text GLabel 5350 1150 2    60   Input ~ 0
TXO3v3
$Comp
L BS170 Q1
U 1 1 5A9CB1AE
P 8100 4400
F 0 "Q1" H 8300 4475 50  0000 L CNN
F 1 "BS170" H 8300 4400 50  0000 L CNN
F 2 "TO_SOT_Packages_THT:TO-92_Inline_Wide" H 8300 4325 50  0001 L CIN
F 3 "" H 8100 4400 50  0001 L CNN
	1    8100 4400
	0    1    1    0   
$EndComp
$Comp
L BS170 Q2
U 1 1 5A9CB504
P 9750 4350
F 0 "Q2" H 9950 4425 50  0000 L CNN
F 1 "BS170" H 9950 4350 50  0000 L CNN
F 2 "TO_SOT_Packages_THT:TO-92_Inline_Wide" H 9950 4275 50  0001 L CIN
F 3 "" H 9750 4350 50  0001 L CNN
	1    9750 4350
	0    1    1    0   
$EndComp
$EndSCHEMATC
