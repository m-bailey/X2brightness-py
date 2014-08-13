steps = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 937]
brightness_path = '/sys/class/backlight/intel_backlight/brightness'
display = 'eDP1'

def set(increase):
	new_brightness = False
	with open(brightness_path, 'r') as f:
		read_brightness = int(f.read())
		if increase:
			for val in steps:
				if read_brightness < val:
					new_brightness = val
					break
		else:
			for val in reversed(steps):
				if read_brightness > val:
					new_brightness = val
					break

		if new_brightness is not False and new_brightness != read_brightness:
			from subprocess import call
			call(['xrandr', '--output',  display, '--set', 'BACKLIGHT', str(new_brightness)])
			call(['notify-send', ' ', '-i', 'display-brightness-symbolic', '-h', 'int:value:%d' % (new_brightness / 9.37), '-h', 'string:synchronous:brightness'])

	return new_brightness

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '-inc':
        set(True)
    elif len(sys.argv) > 1 and sys.argv[1] == '-dec':
    	set(False)
    else:
    	print 'Usage:\n\t-inc\tIncrease brightness\n\t-dec\tDecrease brightness'
