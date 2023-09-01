import os, cv2

frameNumberSize = 6  # six digits
outputFileExt = '.png'
showFrameTime = 120  # 120 ms for showing each frame


# Extracts the frames of the given video and saves them on the given output folder, up to point of having <frameCount>
# samples. Give ZERO, if all the frames must be extracted. Returns a list with the filepaths of the saved frames.
# If <showFrames> is true, it shows the extracted frames.
def extract_frames(videoFilePath, outputFolder, frameCount=0, showFrames=False):
    frameFilePaths = []
    videoLabel = videoFilePath.split(os.sep)[-1]

    reader = cv2.VideoCapture(videoFilePath)
    while (frameCount == 0 or len(frameFilePaths) < frameCount) and reader.isOpened():
        frameFilePath = outputFolder + os.sep + videoLabel + '_' + str(len(frameFilePaths)).zfill(
            frameNumberSize) + outputFileExt

        ret, frame = reader.read()
        if ret:
            cv2.imwrite(frameFilePath, frame)
            frameFilePaths.append(frameFilePath)

            if showFrames:
                cv2.imshow(videoLabel, frame)
                cv2.waitKey(showFrameTime)
        else:
            break

    reader.release()
    cv2.destroyAllWindows()

    return frameFilePaths

