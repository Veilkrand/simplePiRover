import pantilthat as pt

class PanTiltController:

    def __init__(self, pan_offset=0, tilt_offset=0):
        self.pan_offset = pan_offset
        self.tilt_offset = tilt_offset

        self.center()

    def _clamp(self, minimum, x, maximum):
        return max(minimum, min(x, maximum))

    def center(self):
        self.pan = self.pan_offset
        self.tilt = self.tilt_offset
        pt.pan(self.pan)
        pt.tilt(self.tilt)

    def look(self, pan, tilt):
        pt.pan(self._clamp(-90, int(pan * 90) + self.pan, 90))
        pt.tilt(self._clamp(-90, int(tilt * 90) + self.tilt, 90))

    def update_center(self, pan, tilt):


        # if pan > 0.5:
        #     self.pan = self._clamp(-90, self.pan + 1, 90)
        # elif pan < 0.5:

        self.pan = self._clamp(-90, pan + self.pan, 90)
        self.tilt = self._clamp(-90, tilt + self.tilt, 90)

        # pt.pan(self.pan)
        # pt.tilt(self.tilt)
