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
                
                if event.message.text == '紀錄':
                    message = TemplateSendMessage(
                        alt_text='記錄Template無法顯示',
                        template=ButtonsTemplate(
                            thumbnail_image_url='https://cheeek.me/wp-content/uploads/2018/09/117244283.jpg',
                            title='紀錄',
                            text='紀錄之產品將存於已記錄',
                            actions=[
                                MessageTemplateAction(
                                    label='手動輸入', text='手動輸入'
                                ),
                                MessageTemplateAction(
                                    label='掃描QRcode', text='掃描QRcode'
                                ),
                                MessageTemplateAction(
                                    label='掃描產品條碼', text='掃描產品條碼'
                                ),
                                MessageTemplateAction(
                                    label='查看已記錄', text='查看已記錄'
                                )
                            ]
                        )
                    )

                elif event.message.text == '搜尋':
                    message = TemplateSendMessage(
                        alt_text='搜尋Template無法顯示',
                        template=ButtonsTemplate(
                            thumbnail_image_url='https://cheeek.me/wp-content/uploads/2018/09/117244283.jpg',
                            title='搜尋',
                            text='僅搜尋產品成分',
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

                elif event.message.text == '掃描QRcode':
                    message = TemplateSendMessage(
                        alt_text='掃描QRCode Template無法顯示',
                        template=ButtonsTemplate(
                            title='掃描QRCode',
                            text='進入後點選下方的掃描行動條碼並將發票掃描後之文字檔傳回對話訊息',
                            actions=[
                                URITemplateAction(
                                    label='掃描QRCode', uri='https://line.me/R/nv/QRCode'
                                )
                            ]
                        )
                    )
                elif event.message.text == '掃描產品條碼':
                    message = TemplateSendMessage(
                        alt_text='掃描產品條碼Template無法顯示',
                        template=ButtonsTemplate(
                            title='掃描產品條碼',
                            text='進入後將產品條碼拍照後轉為文字並將條碼之對應數字傳回對話訊息',
                            actions=[
                                URITemplateAction(
                                    label='掃描產品條碼', uri='https://line.me/R/nv/camera/ocr'
                                )
                            ]
                        )
                    )

                elif event.message.text == '分析':
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
                    updatestate(uid,1,0)
                    status = get_statusDB(uid)
                    message = message_continuous(status.continuous, uid, event.message.text)
                    line_bot_api.reply_message(event.reply_token, message)
                
                elif event.message.text == '分析產品':
                    prc = get_productDB(uid)
                    pn = Compare_All_Product(uid,prc[1].pname)
                    pn += '分析結束!!!!'
                    message = TextSendMessage(text=pn)
                
                
                else:
                    status = get_statusDB(uid)
                    message = message_continuous(status.continuous, uid, event.message.text)
                line_bot_api.reply_message(event.reply_token, message)
        return HttpResponse()
    else:
        return HttpResponseBadRequest()


def updatestate(userid,count,countin):
    states = CustomerState.objects.filter(uid=userid)
    if not states:
        states = CustomerState.objects.create(uid=userid, continuous=countin, cnt=count)
    else:
        states = CustomerState.objects.filter(uid=userid).update(continuous=countin,cnt=count)




def get_statusDB(userid):
    ans = CustomerState.objects.get(uid = userid)
    # db.close()
    return ans

def message_continuous(countin,uid,userMessage):
    if countin == 0:
        updatestate(uid,1,1)
        message = TextSendMessage(text = '請輸入你想要紀錄的商品的品牌')
    elif countin == 1:
        update_productDB(countin,uid,userMessage)
        updatestate(uid,1,2)
        message = TextSendMessage(text = '請輸入你想要紀錄的商品名稱')
    else:
        update_productDB(countin,uid,userMessage)
        product = get_productDB(uid)
        msg = ''
        if(len(product)>1):
            msg += '品牌' + product[len(product)-1].pbrand + '\n'
            msg += '商品名稱' + product[len(product)-1].pname + '\n'
        else:
            msg += '品牌' + product[0].pbrand + '\n'
            msg += '商品名稱' + product[0].pname + '\n'
        updatestate(uid, 0, 0)
        message = TextSendMessage(text = '已儲存' + str(msg))
    return message



def update_productDB(count,uid,userMessage):

    if count == 1:
        product = Product.objects.create(uid=uid,pbrand=userMessage)
    else:
        product = Product.objects.create(uid=uid,pname=userMessage)


def get_productDB(userid):
    product = Product.objects.filter(uid=userid)
    return product



def Compare_All_Product(userid,qName):
    #從資料庫取得資料
    msg = ''
    cbt = 0
    try:
        allProd = Product.objects.filter(uid=userid)
    except:
        msg = '使用者找產品有問題\n'
    found = -1
    for i in range(1,len(allProd)):
        if qName == allProd[i].pname :
            cbt += 1
            try:
                ingred = CosmeticIngredient.objects.get(pname=qName)
            except:
                msg += '資料庫找名字有問題\n'
            try:
                qIngre = ingred.ingredient.split(',')
                #if qIngre.index('') != -1: qIngre.remove('')
            except:
                msg += '拆解有問題\n'
            found = i
            break
        else:
            msg += '非常抱歉！我們暫時沒有收錄這款產品，如果您願意的話可以回報給客服喔！\n'
    msg += '成功找到\n'+qName+'\n'
    
    data = User_Product.objects.filter(uid = userid)
 
        
    return msg
