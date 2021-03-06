default: gui test

UItest:
	@py UItest.py

test:
	@py main.py

gui:
	@pyuic5 ui/mainwindow.ui -o ui_mainwindow.py
	@pyuic5 ui/hmi.ui -o ui_hmi.py
	@pyuic5 ui/avrdude.ui -o ui_avrdude.py
	@pyuic5 ui/asa_prog.ui -o ui_asa_prog.py
	@pyuic5 ui/bit_selector.ui -o ui_bit_selector.py
	@pyuic5 ui/hmi_save_dialog.ui -o ui_hmi_save_dialog.py
	@pyuic5 ui/hmi_load_dialog.ui -o ui_hmi_load_dialog.py
