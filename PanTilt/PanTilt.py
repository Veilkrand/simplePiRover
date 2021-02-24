import pantilthat as pt


class PanTiltController:
    pan = 0
    tilt = 0

    ANGLE_STEP_CENTERING = 2

    def __init__(self,
                 pan_offset=0, tilt_offset=0,
                 pan_max=90, pan_min=-90,
                 tilt_max=90, tilt_min=-90):

        self.pan_offset = pan_offset
        self.tilt_offset = tilt_offset

        self.pan_max = pan_max
        self.pan_min = pan_min
        self.tilt_max = tilt_max
        self.tilt_min = tilt_min

        self.center()

    @staticmethod
    def _clamp(minimum, x, maximum):
        return max(minimum, min(x, maximum))

    def center(self):
        self.pan = self.pan_offset
        self.tilt = self.tilt_offset
        pt.pan(self.pan)
        pt.tilt(self.tilt)

    def look(self, pan, tilt):
        pt.pan(self._clamp(self.pan_min, int(pan * self.pan_max) + self.pan, self.pan_max))
        pt.tilt(self._clamp(self.tilt_min, int(tilt * self.tilt_max) + self.tilt, self.tilt_max))

    def update_center(self, pan, tilt):

        pan = pan * self.ANGLE_STEP_CENTERING
        tilt = tilt * self.ANGLE_STEP_CENTERING

        self.pan = self._clamp(self.pan_min, pan + self.pan, self.pan_max)
        self.tilt = self._clamp(self.tilt_min, tilt + self.tilt, self.tilt_max)
