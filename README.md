# FLStudioOxygenPro49
FL Studio 20 script for the M-Audio Oxygen Pro 49 controller.

Note: I have no previous experience with MIDI controllers so this might be a bit different from other integrations, but I intend this script to work well for at least my personal case. ;-)

The M-Audio Oxygen Pro 49 seems to provide four MIDI input devices.  
According to some tests I made:
- Normal keys/notes can be received via device 1 
- I have no idea what device 2 is for, yet
- Device 3 handles most of the sliders, knobs and buttons when the controller is set to DAW mode
- Device 4 I'm unsure about, but it seems like the M-Audio editor uses that one to transfer presets from and to the controller (?)

## Features
- Sliders: mapped to mixer sliders, first slider is the first mixer slider (slider #1, not the master channel!)  
- Knobs: first knob mapped to the master channel, the rest is currently unmapped  
- Buttons below sliders:  
This one actually depends on which mode is selected:  
REC: currently unmapped
SELECT: selects an instrument in the pattern window
MUTE: mutes a channel in the mixer
SOLO: sets a channel to solo mode in the mixer
- Left/Right button: previous/next pattern
- Loop button: toggles loop recording mode

## Getting started

To get up and running:  
``// TODO: improve these instructions``

1. Go to `%userprofile%\Documents\Image-Line\FL Studio\Settings\Hardware`
2. Clone this repository into that directory so that you end up with something like `%userprofile%\Documents\Image-Line\FL Studio\Settings\Hardware\oxygenpro49\device_oxygenpro49_port3.py`. The name of the directory is not important.
3. Import the DAW preset into the M-Audio Editor and send it to the controller. I don't think the user preset is required, but I included a working one, in case it's needed. [1]
4. Restart FL Studio and go to the midi configuration. Make sure to set up the controller so that the first MIDI device is set to `(generic controller)` and the third device (MIDIIN3) is set to this script.
5. Ideally, in the output section select the first device and enable the option to send the master sync to that device. On the controller, you can set the clock sync setting to EXTERNAL.
6. Now you should be ready. A quick test would be to see if the Play/Stop/Record buttons work.


## Notes
- **[1]** This preset is based on the official FL Studio preset, but the knobs have been adjusted to emit CC messages beginning at 102 for the first knob, 103 for the second etc.  
The reason for this is that by default, the FL Studio profile seems to trigger the same Mackie controls as the sliders, which I am not quite sure why that is. I am not sure if this is the best way to deal with this, but it works for now.
