""" config file containing some global variables and paths """

# paths for landmarks and cascades
PREDICTOR_PATH = "/Users/nbettache/Desktop/face_recognition/shape_predictor_68_face_landmarks.dat"
CASCADE_PATH = "/Users/nbettache/Desktop/face_recognition/haarcascade_frontalface_default.xml"

# constants for face alignment
LEFT_EYE_POS = (6, 6)
EYES_SPACE = 18
FACE_HEIGHT = 32  # from eyes to chin
EYE_MOUTH = 16
HEIGHT = 30
WIDTH = 30

# reference face image
IMREF_PATH = "/Users/nbettache/Desktop/face_recognition/data/yalefaces/subject03/subject03_noglasses.png"

# database paths
DATABASE_PATH = "/Users/nbettache/Desktop/face_recognition/data/yalefaces"

# print stuff during dictionaries creation
VERBOSE = True

# parameters
TRAINING_FACES = 4
TEST_FACES = 3
DIM_REDUCTION = False
NB_DIM = 15

# RSC algorithm params
NB_ITER = 2
PARAM_C = 8.0
PARAM_TAU = 0.8
LAMBDA = 0.001

REG_METHOD = 'l1'  # default (other possible value: l1)