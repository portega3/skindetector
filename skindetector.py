from pyimagesearch import imputils
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help = "path to the (optional)video file")
args = vars(ap.parse_args())





lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")



if not args.get("video", False):
	camera = cv2.VideoCaprture(0)


else:
	camera = cv2.VideoCapture(args["video"])

