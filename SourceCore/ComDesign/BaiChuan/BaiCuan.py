# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html
from http import HTTPStatus
import dashscope

dashscope.api_key = ""


def sample_sync_call(prompt_text):
    resp = dashscope.Generation.call(
        model='qwen-turbo',
        prompt='你现在需要扮演一位心理咨询师，通过简短的聊天回答患者的话,回答控制在200字以内：' + prompt_text
    )
    # The response status_code is HTTPStatus.OK indicate success,
    # otherwise indicate request is failed, you can get error code
    # and message from code and message.
    if resp.status_code == HTTPStatus.OK:
        r = {'text': resp.output['text'], 'type': 'text'}
        return r
    else:
        print(resp.message)  # The error message.
        return resp.code
