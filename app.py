import os, sys
from serial import SerialException
from flask import Flask, request, render_template, redirect, url_for
from NFC_Class import NFC


NFC_locate = "COM6"
STM32_locate = "COM7"
LORA_locate = "COM8"

# fake data 

# STM32 check mount
def STM32_boot(STM32_locate):
    return = "OK"
# STM32 check response
def STM32_response(STM32_locate):
    return = "OK"
# LORA check "mod get_ver"
def LORA_response(STM32_locate, check_item):
    return = "OK"

# system hardware boot up
def Client_hotware_boot():
    hardware_error = 0
    error_massage = ""
    # STM32_check_device
    if (STM32.STM32_response(STM32_locate, "STM32_OK") == "OK" & hardware_error = 0):
        if (NFC.wake(NFC.locate) == "OK"):
            STM32_write("STM32_OK")
        else:
            STM32_write("STM32_ERROR")
            hardware_error = 1
            error_massage = "STM32_ERROR"
    # RFID_check_device
    if (STM32.STM32_response(STM32_locate, "RFID_OK") != "OK" & hardware_error = 0):
        if (NFC.wake(NFC.locate) == "OK"):
            STM32_write("RFID_OK")
        else:
            STM32_write("RFID_ERROR")
            hardware_error = 1
            error_massage = "RFID_ERROR"
    # LORA_check_device
    if (STM32.STM32_response(STM32_locate, "LORA_OK") != "OK" & hardware_error = 0)
        if (LORA.LORA_response(LORA_locate(LORA_locate)) == "OK")
            STM32_write("LORA_OK")
        else:
            STM32_write("LORA_ERROR")
            hardware_error = 1
            error_massage = "LORA_ERROR"
    return hardware_error, error_massage

# system software boot up
def Client_software_boot():

