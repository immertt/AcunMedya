import cv2
import mediapipe as mp



class FaceMeshDetector:
    def __init__(self,max_faces=2,refine_landmarks=True,detection_confidence=0.5, tracking_confidence=0.5):
        self.max_faces = max_faces
        self.refine_landmarks = refine_landmarks
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces = self.max_faces,
            refine_landmarks = self.refine_landmarks,
            min_detection_confidence = self.detection_confidence,
            min_tracking_confidence = self.tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.drawing_spec = self.mp_draw.DrawingSpec(thickness=1,circle_radius=1)

    def detect_faces(self,frame):
        rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)
        return results
    
    def draw_landmarks(self,frame,landmarks):
        self.mp_draw.draw_landmarks(
            image = frame,
            landmark_list = landmarks,
            connections = self.mp_face_mesh.FACEMESH_IRISES,
            landmark_drawing_spec = self.drawing_spec,
            connection_drawing_spec = self.drawing_spec
        )
