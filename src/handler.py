# local
import utils

def Frame(data):
    if data.current_frame.pose:
        positionsOfFrame = data.current_frame.pose
        matrixOfFrame = utils.arrayOf16ToMatrix4by4(positionsOfFrame)
        # it seems the first 3 numbers in the array are x, y, z but cant figure out last value
        print(matrixOfFrame)

def LandMarks(data):
    for landmark in data.landmarks:
        if landmark.coords:
            [x, y, z] = landmark.coords
            # save to dataset and visualise ??