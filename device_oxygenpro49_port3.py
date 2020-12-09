# name=M-Audio Oxygen Pro 49 (MIDIIN3)
# url=https://github.com/PotcFdk/FLStudioOxygenPro49

import transport
import channels
import patterns
import mixer
import ui
import midi

VAL_OFF = 0
VAL_ON = 127

BUTTON_BANK_PREVIOUS = 46
BUTTON_BANK_NEXT = 47

BUTTON_LOOP = 86
BUTTON_LEFT = 91
BUTTON_RIGHT = 92
BUTTON_STOP = 93
BUTTON_PLAY = 94
BUTTON_RECORD = 95
BUTTON_TOP = 96
BUTOTN_BOTTOM = 97

KNOB_1 = 102
KNOB_2 = 103
KNOB_3 = 104
KNOB_4 = 105
KNOB_5 = 106
KNOB_6 = 107
KNOB_7 = 108
KNOB_8 = 109

SLIDER_1 = 224
SLIDER_2 = 225
SLIDER_3 = 226
SLIDER_4 = 227
SLIDER_5 = 228
SLIDER_6 = 229
SLIDER_7 = 230
SLIDER_8 = 231
SLIDER_9 = 232

MODE_BUTTON_REC_1 = 0
MODE_BUTTON_REC_2 = 1
MODE_BUTTON_REC_3 = 2
MODE_BUTTON_REC_4 = 3
MODE_BUTTON_REC_5 = 4
MODE_BUTTON_REC_6 = 5
MODE_BUTTON_REC_7 = 6
MODE_BUTTON_REC_8 = 7

MODE_BUTTON_SOLO_1 = 8
MODE_BUTTON_SOLO_2 = 9
MODE_BUTTON_SOLO_3 = 10
MODE_BUTTON_SOLO_4 = 11
MODE_BUTTON_SOLO_5 = 12
MODE_BUTTON_SOLO_6 = 13
MODE_BUTTON_SOLO_7 = 14
MODE_BUTTON_SOLO_8 = 15

MODE_BUTTON_MUTE_1 = 16
MODE_BUTTON_MUTE_2 = 17
MODE_BUTTON_MUTE_3 = 18
MODE_BUTTON_MUTE_4 = 19
MODE_BUTTON_MUTE_5 = 20
MODE_BUTTON_MUTE_6 = 21
MODE_BUTTON_MUTE_7 = 22
MODE_BUTTON_MUTE_8 = 23

MODE_BUTTON_SELECT_1 = 24
MODE_BUTTON_SELECT_2 = 25
MODE_BUTTON_SELECT_3 = 26
MODE_BUTTON_SELECT_4 = 27
MODE_BUTTON_SELECT_5 = 28
MODE_BUTTON_SELECT_6 = 29
MODE_BUTTON_SELECT_7 = 30
MODE_BUTTON_SELECT_8 = 31

class TOxygenPro49_P3():
	def OnMidiMsg(self, event):
		event.handled = True

		if event.midiId == midi.MIDI_NOTEON:
			if (event.pmeFlags & midi.PME_System != 0) and event.data2 == VAL_ON:
				print (event.data1, event.data2)
				if event.data1 == BUTTON_STOP:
					if transport.isPlaying():
						print ("STOP")
						transport.stop()
				elif event.data1 == BUTTON_PLAY:
					if not transport.isPlaying():
						print ("START")
						transport.start()
				elif event.data1 == BUTTON_RECORD:
					print ("RECORD")
					transport.record()
				elif event.data1 >= MODE_BUTTON_SELECT_1 and event.data1 <= MODE_BUTTON_SELECT_8:
					print ("MODE/SELECT {}".format (event.data1 - MODE_BUTTON_SELECT_1))
					channels.selectOneChannel (event.data1 - MODE_BUTTON_SELECT_1)
				elif event.data1 >= MODE_BUTTON_MUTE_1 and event.data1 <= MODE_BUTTON_MUTE_8:
					print ("MODE/MUTE {}".format (event.data1 - MODE_BUTTON_MUTE_1))
					mixer.muteTrack (event.data1 - MODE_BUTTON_MUTE_1 + 1)
				elif event.data1 >= MODE_BUTTON_SOLO_1 and event.data1 <= MODE_BUTTON_SOLO_8:
					print ("MODE/SOLO {}".format (event.data1 - MODE_BUTTON_SOLO_1))
					mixer.soloTrack (event.data1 - MODE_BUTTON_SOLO_1 + 1)
				elif event.data1 >= MODE_BUTTON_REC_1 and event.data1 <= MODE_BUTTON_REC_8:
					print ("MODE/REC {}".format (event.data1 - MODE_BUTTON_REC_1))
				elif event.data1 == BUTTON_LEFT:
					print ("PATTERN <<")
					patterns.jumpToPattern (patterns.patternNumber() - 1)
				elif event.data1 == BUTTON_RIGHT:
					print ("PATTERN >>")
					patterns.jumpToPattern (patterns.patternNumber() + 1)
				elif event.data1 == BUTTON_LOOP:
					print ("LOOP")
					transport.globalTransport (midi.FPT_LoopRecord, 1, event.pmeFlags)
				elif event.data1 == BUTTON_BANK_PREVIOUS or event.data1 == BUTTON_BANK_NEXT:
					print ("BANK <</>>")
				else:
					event.handled = False
			else:
				event.handled = False
		elif event.midiId == 224: # pitch wheel id
			if event.midiId + event.midiChan >= SLIDER_1 and event.midiId + event.midiChan <= SLIDER_9:
				mixer.setTrackVolume (event.midiChan + 1, event.data2 / 127)
			else:
				event.handled = False
		elif event.midiId == 176: # msb control change for knobs
			if event.data1 == KNOB_1:
				mixer.setTrackVolume (0, event.data2 / 127)
			elif event.data1 >= KNOB_2 and event.data1 <= KNOB_8:
				event.handled = True
			else:
				event.handled = False
		else:
			event.handled = False

OxygenPro49 = TOxygenPro49_P3()

def OnMidiMsg(event):
	print("OnMidiMsg")
	OxygenPro49.OnMidiMsg(event)

def OnMidiIn(event):
	print("OnMidiIn")

def OnControlChange(event):
	print("OnControlChange")

def OnProgramChange(event):
	print("OnProgramChange")
