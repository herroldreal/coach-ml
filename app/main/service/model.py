from deepface import DeepFace


def verify(image_path1, image_path2):
    result = DeepFace.verify(
        image_path1,
        image_path2,
        enforce_detection=False,
        detector_backend='mtcnn'
    )

    print('Face emotion result -> Gender: {} - Age: {} - Race: {} - Emotion: {}'.format(
        result[0]["dominant_gender"],
        result[0]["age"],
        result[0]["dominant_race"],
        result[0]["dominant_emotion"]
    ))


def find(image_path):
    df = DeepFace.find(image_path, './', enforce_detection=False)
    print('Face Recognition result -> {}'.format(df))


def analyze(image_path):
    analyze = DeepFace.analyze(
         image_path,
         enforce_detection=True,
         detector_backend='mtcnn',
         actions=('age', 'gender', 'race', 'emotion')
    )

    print('Face result -> {}'.format(analyze))

