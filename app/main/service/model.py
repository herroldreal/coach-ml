from deepface import DeepFace


def verify(image_path1, image_path2):
    result = DeepFace.verify(
        image_path1,
        image_path2,
        enforce_detection=False,
        detector_backend='mtcnn'
    )
    #  df = DeepFace.find(image_path1, './', enforce_detection=False)
    # analyze = DeepFace.analyze(
    #     image_path1,
    #     enforce_detection=True,
    #     detector_backend='mtcnn',
    #     actions=('age', 'gender', 'race', 'emotion')
    # )

    #  print('Face Recognition result -> {}'.format(df))
    #  print('Face result -> {}'.format(result))
    analyze = result
    print(analyze)
    # print('Face emotion result -> Gender: {} - Age: {} - Race: {} - Emotion: {}'.format(analyze["dominant_gender"],
    # analyze["age"], analyze["dominant_race"], analyze["dominant_emotion"]))
