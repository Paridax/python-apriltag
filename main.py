import apriltag
import cv2

def main():
	# Load the image
	image = cv2.imread("apriltag_target.png")
	# Convert to grayscale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# Create the detector
	detector = apriltag.Detector()
	# Detect the tags
	tags = detector.detect(gray)
	# Print the tags
	print(tags)

if __name__ == '__main__':
	main()