from cemotion import Cemotion


def test(text):
    c = Cemotion()  # 实例化情感分析模型
    prediction = c.predict(text)  # 调用情感分析模型进行预测
    print(prediction)


def analyze_emotion(text):
    c = Cemotion()  # 实例化情感分析模型
    prediction = c.predict(text)  # 调用情感分析模型进行预测
    if prediction > 0.95:
        return 1
    else:
        return 0
