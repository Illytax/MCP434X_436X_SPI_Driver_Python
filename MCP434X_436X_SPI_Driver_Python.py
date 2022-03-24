# Driver for the MCP434X/436X
# Author: Edward Jordan
# Version: 1.0
# Date: 24/03/2022

###################
# VOLATILE WIPERS #
###################

# MCP434X/436X Volatile Wiper 0 Command Bits In Hex
DIGIPOT_CMD_WRITE_0 = 0x00
DIGIPOT_CMD_READ_0 = 0x0C
DIGIPOT_CMD_INC_WIPER_0 = 0x04
DIGIPOT_CMD_DEC_WIPER_0 = 0x08

# MCP434X/436X Volatile Wiper 1 Command Bits In Hex
DIGIPOT_CMD_WRITE_1 = 0x10
DIGIPOT_CMD_READ_1 = 0x1C
DIGIPOT_CMD_INC_WIPER_1 = 0x14
DIGIPOT_CMD_DEC_WIPER_1 = 0x18

# MCP434X/436X Volatile Wiper 2 Command Bits In Hex
DIGIPOT_CMD_WRITE_2 = 0x60
DIGIPOT_CMD_READ_2 = 0x6C
DIGIPOT_CMD_INC_WIPER_2 = 0x64
DIGIPOT_CMD_DEC_WIPER_2 = 0x68

# MCP434X/436X Volatile Wiper 3 Command Bits In Hex
DIGIPOT_CMD_WRITE_3 = 0x70
DIGIPOT_CMD_READ_3 = 0x7C
DIGIPOT_CMD_INC_WIPER_3 = 0x74
DIGIPOT_CMD_DEC_WIPER_3 = 0x78

#######################
# NON-VOLATILE WIPERS #
#######################

# MCP434X/436X Non-Volatile Wiper 0 Command Bits In Hex
DIGIPOT_NON_VOLATILE_CMD_WRITE_0 = 0x20
DIGIPOT_NON_VOLATILE_CMD_READ_0 = 0x2C
DIGIPOT_HIGH_VOLTAGE_CMD_INC_WIPER_0 = 0x24
DIGIPOT_HIGH_VOLTAGE_CMD_DEC_WIPER_0 = 0x28

# MCP434X/436X Non-Volatile Wiper 1 Command Bits In Hex
DIGIPOT_NON_VOLATILE_CMD_WRITE_1 = 0x30
DIGIPOT_NON_VOLATILE_CMD_READ_1 = 0x3C
DIGIPOT_HIGH_VOLTAGE_CMD_INC_WIPER_1 = 0x34
DIGIPOT_HIGH_VOLTAGE_CMD_DEC_WIPER_1 = 0x38

# MCP434X/436X Non-Volatile Wiper 2 Command Bits In Hex
DIGIPOT_NON_VOLATILE_CMD_WRITE_2 = 0x80
DIGIPOT_NON_VOLATILE_CMD_READ_2 = 0x8C
DIGIPOT_HIGH_VOLTAGE_CMD_INC_WIPER_2 = 0x84
DIGIPOT_HIGH_VOLTAGE_CMD_DEC_WIPER_2 = 0x88

# MCP434X/436X Non-Volatile Wiper 3 Command Bits In Hex
DIGIPOT_NON_VOLATILE_CMD_WRITE_3 = 0x90
DIGIPOT_NON_VOLATILE_CMD_READ_3 = 0x9C
DIGIPOT_HIGH_VOLTAGE_CMD_INC_WIPER_3 = 0x94
DIGIPOT_HIGH_VOLTAGE_CMD_DEC_WIPER_3 = 0x98

###############
# Data EEPROM #
###############

# MCP434X/436X Data EEPROM 0 Command Bits In Hex
DIGIPOT_DATA_EEPROM_CMD_WRITE_0 = 0xB0
DIGIPOT_DATA_EEPROM_CMD_READ_0 = 0xBC

# MCP434X/436X Data EEPROM 1 Command Bits In Hex
DIGIPOT_DATA_EEPROM_CMD_WRITE_1 = 0xC0
DIGIPOT_DATA_EEPROM_CMD_READ_1 = 0xCC

# MCP434X/436X Data EEPROM 2 Command Bits In Hex
DIGIPOT_DATA_EEPROM_CMD_WRITE_2 = 0xD0
DIGIPOT_DATA_EEPROM_CMD_READ_2 = 0xDC

# MCP434X/436X Data EEPROM 3 Command Bits In Hex
DIGIPOT_DATA_EEPROM_CMD_WRITE_3 = 0xE0
DIGIPOT_DATA_EEPROM_CMD_READ_3 = 0xEC

# MCP434X/436X Data EEPROM 4 Command Bits In Hex
DIGIPOT_DATA_EEPROM_CMD_WRITE_4 = 0xF0
DIGIPOT_DATA_EEPROM_CMD_READ_4 = 0x7CD
IGIPOT_DATA_EEPROM_HIGH_VOLTAGE_CMD_INC_WIPER_4 = 0xF4
DIGIPOT_DATA_EEPROM_HIGH_VOLTAGE_CMD_DEC_WIPER_4 = 0xF8


#########
# Other #
#########

# MCP434X/436X Volatile TCON 0 Register Command Bits In Hex
DIGIPOT_DATA_EEPROM_CMD_WRITE_3 = 0x40
DIGIPOT_DATA_EEPROM_CMD_READ_3 = 0x4C

# MCP434X/436X Volatile TCON 1 Register Command Bits In Hex
DIGIPOT_DATA_EEPROM_CMD_WRITE_3 = 0xA0
DIGIPOT_DATA_EEPROM_CMD_READ_3 = 0xAC

# MCP434X/436X Volatile Status Register Command Bits In Hex
DIGIPOT_DATA_EEPROM_CMD_READ_3 = 0x5C

#####################
# RESISTANCE VALUES #
#####################

# MCP434X/436X Resistance Values
DIGIPOT_RES_0KOHM = 0x00
DIGIPOT_RES_1KOHM = 0x1A
DIGIPOT_RES_2KOHM = 0x34
DIGIPOT_RES_3KOHM = 0x4E
DIGIPOT_RES_5KOHM = 0x80
DIGIPOT_RES_7KOHM = 0xB6
DIGIPOT_RES_10KOHM = 0xFF

##################
# DECALATION END #
##################

import time
import spidev

# Open An Instance Of SPIDEV
spi = spidev.SpiDev()

# Set The Control Pin
# Param 1 Bus
# Param 2 SPI Channel
spi.open(0, 1)

# Sets The Max Speed In Hz For The SPI Device
spi.max_speed_hz = 1000000


# spi.xfer Performs An SPI Transaction,
# Sets The Channel Select Pin Low,
# Writes to the SPI Device,
# Then Sets Channel Select Pin High

# Example Code
while True:
    # Write Volatile Wiper 1 to 1KOHM
    spi.xfer([DIGIPOT_CMD_WRITE_1, DIGIPOT_RES_1KOHM])
    # Sleep For 1 Second
    time.sleep(1)
    # Write Volatile Wiper 1 to 10KOHM
    spi.xfer([DIGIPOT_CMD_WRITE_1, DIGIPOT_RES_10KOHM])
    # Sleep For 1 Second
    time.sleep(1)
