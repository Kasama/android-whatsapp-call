Android Whatsapp call
=====================

This project was developed with the goal to call São Paulo's Italian consulate on whatsapp to schedule for passport emission.

It can be used to continuously call and re-call any whatsapp contact when they are busy or the call disconnects.

Dependencies
============

- Android device with `uiautomator`
- `ADB` installed in the computer and android with developer options enabled
- `python 3+`
  * [lxml](https://lxml.de/) python library

Usage
=====

- Navigate into the whatsapp contact page for the contact you want to call. (The page that has the `Call` button)
- Plug the phone into the computer and have ADB permissions set
- run `python call.py`
- to stop, press `Ctrl+C`

How it works
============

The code uses [`uiautomator`](https://stuff.mit.edu/afs/sipb/project/android/docs/tools/help/uiautomator/index.html) to dump an xml corresponding to the current view of the android device.

Then it reads the xml looking for the [Call button](call.py:28) (This can be changed to perform tasks other than calling in whatsapp) and sends a `tap` on the button's coordinates
