import os
import re
import time
from lxml import etree


def system(cmd):
    os.system(f"{cmd} >/dev/null 2>&1")


def tap(x, y):
    system(f"adb shell input tap {x} {y}")


def get_screen():
    filename = "window_dump.xml"
    dump_path = f"/sdcard/{filename}"
    system(f"adb shell uiautomator dump {dump_path}")
    system(f"adb pull {dump_path} {filename}")

    root = etree.parse(filename)

    return root


def check_call_button(xml):
    call_button = xml.xpath(
        '//node[@resource-id="com.whatsapp:id/action_call"]')

    if len(call_button) == 0:
        call_button = xml.xpath(
            '//node[@resource-id="com.whatsapp:id/call_back_btn"]')
        if len(call_button) == 0:
            return False

    bounds = call_button[0].get('bounds')
    matches = re.compile('\[(\d+),(\d+)\]').findall(bounds)
    if len(matches) > 0:
        return matches[0]
    return False


def check_answered_call(xml):
    video_button = xml.xpath(
        '//node[@resource-id="com.whatsapp:id/toggle_video_btn"]')

    if len(video_button) == 0:
        return False

    return video_button[0].get('enabled') == "true"


def do_call():
    screen = get_screen()
    call_button = check_call_button(screen)
    if not call_button:
        print("no call button found")
    else:
        x, y = call_button
        print(f"call button found at {x} {y}. Calling...")
        tap(x, y)
    return check_answered_call(screen)


while not do_call():
    time.sleep(0.1)
