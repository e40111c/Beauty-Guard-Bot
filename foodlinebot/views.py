from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot.models import *
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

from .models import *
 
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
 
 
@csrf_exempt
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                uid = event.source.user_id
                if event.message.text == '分析':
                    message = TemplateSendMessage(
                        alt_text='分析Template無法顯示',
                        template=ButtonsTemplate(
                            thumbnail_image_url='https://cheeek.me/wp-content/uploads/2018/09/117244283.jpg',
                            title='分析',
                            text='分析與已紀錄之產品成分是否適合',
                            actions=[
                                MessageTemplateAction(
                                    label='手動輸入', text='手動輸入'
                                ),
                                MessageTemplateAction(
                                    label='掃描QRcode', text='掃描QRcode'
                                ),
                                MessageTemplateAction(
                                    label='掃描產品條碼', text='掃描產品條碼'
                                )
                            ]
                        )
                    )
                elif event.message.text == '手動輸入':
                    updatestate(userid,1,0)
                    message = '成功儲存'
                else:
                    message = event.message.text
                line_bot_api.reply_message(event.reply_token, message)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()




def updatestate(userid,count,countin):
    states = CustomerStatus.objects.filter(uid=userid)
    if not states:
        states = CustomerStatus.objects.create(uid=userid, continuous=countin, cnt=count)
    else:
        states = CustomerStatus.objects.filter(uid=userid).update(continuous=countin,cnt=count)
# Create your views here.
