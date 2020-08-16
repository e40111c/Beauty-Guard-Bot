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

def hello_view(request):
    return render(request, 'hello_django.html', {
        'data': "Hello Django"
    })




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
                                    label='手動輸入', text='紀錄產品'
                                ),
                                URITemplateAction(  # 這行要改
                                    label='掃描QRcode(限Android)', uri='https://liff.line.me/1654432888-3nAgx1WL'  # 這行要改
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
                                    label='手動輸入', text='搜尋產品'
                                ),
                                URITemplateAction(  # 這行要改
                                    label='掃描QRcode(限Android)', uri='https://liff.line.me/1654432888-3nAgx1WL'  # 這行要改
                                ),
                                MessageTemplateAction(
                                    label='掃描產品條碼', text='掃描產品條碼'
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
                                    label='手動輸入', text='分析產品'
                                ),
                                URITemplateAction(  # 這行要改
                                    label='掃描QRcode(限Android)', uri='https://liff.line.me/1654432888-3nAgx1WL'  # 這行要改
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
                            text = '對準發票上之QRCode，掃描後結果即顯示於聊天室',
                            actions=[
                                URITemplateAction(
                                    label='掃描QRCode(限Android)', uri='https://liff.line.me/1654432888-3nAgx1WL'  # 這行要改
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

                elif event.message.text == '紀錄產品':
                    updatestate(uid, 1, 0)
                    status = get_statusDB(uid)
                    message = message_continuous(status.continuous, uid, event.message.text)

                elif event.message.text == '搜尋產品':
                    updatestate(uid, 1, 0)
                    status = get_statusDB(uid)
                    message = message_continuous(status.continuous, uid, event.message.text)
                elif event.message.text == '圖片':
                    message = []
                    message.append(ImageSendMessage(original_content_url='https://5b76fcb485d9.ngrok.io/static/skincare_02.jpg',
                                               preview_image_url='https://5b76fcb485d9.ngrok.io/static/skincare_02.jpg'))
                    message.append(TextSendMessage(text='加個文字吧?'))
                    line_bot_api.reply_message(event.reply_token, message)

                elif event.message.text == '分析產品':
                    updatestate(uid, 1, 0)
                    status = get_statusDB(uid)
                    message = message_continuous(status.continuous, uid, event.message.text)


                elif event.message.text == '回報':
                    updatestate(uid, 1, 0)
                    status = get_statusDB(uid)
                    message = message_continuous(status.continuous, uid, event.message.text) 
                    
                else:
                    try:
                        status = get_statusDB(uid)
                        if(status.continuous == 0 and status.cnt==0):
                            message = ''
                        else:
                            message = message_continuous(status.continuous, uid, event.message.text)
                    except:
                        pass
                line_bot_api.reply_message(event.reply_token, message)
        return HttpResponse()
    else:
        return HttpResponseBadRequest()


def updatestate(userid, count, countin):
    states = CustomerState.objects.filter(uid=userid)
    if not states:
        states = CustomerState.objects.create(uid=userid, continuous=countin, cnt=count)
    else:
        states = CustomerState.objects.filter(uid=userid).update(continuous=countin, cnt=count)


def get_statusDB(userid):
    ans = CustomerState.objects.get(uid=userid)
    # db.close()
    return ans


def message_continuous(countin, uid, userMessage):
    if countin == 0 and userMessage == '紀錄產品':
        updatestate(uid, 1, 1)
        message = TextSendMessage(text='請輸入你想要紀錄的商品品牌')
    elif countin == 1:
        update_productDB(countin, uid, userMessage)
        updatestate(uid, 1, 2)
        message = TextSendMessage(text='請輸入你想要紀錄的商品名稱')

    elif countin == 0 and userMessage == '搜尋產品':
        updatestate(uid, 1, 4)
        message = TextSendMessage(text='請輸入你想要搜尋的產品品牌')
    elif countin == 4:
        updatestate(uid, 1, 5)
        message = TextSendMessage(text='請輸入你想要搜尋的商品名稱')
    elif countin == 5:
        res = ''
        result = search_productDB(userMessage)
        if type(result) == str:
            result = '查無此產品資訊'
        else:
            sp = result.ingredient.split(',')
            for i in sp:
                if i == '"':
                    pass
                else:
                    res += i + '\n'
            result = '已找到'+userMessage+'成分\n'+res
        updatestate(uid, 0, 0)
        message = TextSendMessage(text=result)
        
    elif countin == 0 and userMessage == '回報':
        message = TextSendMessage(text='請輸入想要回報的產品/問題')
        updatestate(uid, 1, 6)
    elif countin == 6:
        message = TextSendMessage(text='感謝你的回報，我們會盡速處理')
        updatestate(uid, 0, 0)
        
    elif countin == 0 and userMessage == '分析產品':
        message = TextSendMessage(text='請輸入想要分析的產品名稱')
        updatestate(uid, 1, 7)
    elif countin == 7:
        msg = Compare_All_Product(uid,userMessage)
        message = TextSendMessage(text=msg+'\n\n分析結束!!')
        updatestate(uid, 0, 0)

    else:
        update_productDB(countin, uid, userMessage)
        updatestate(uid, 0, 0)
        message = TemplateSendMessage(
            alt_text='資料庫商品有問題，請另尋產品',
            template=ButtonsTemplate(
                thumbnail_image_url='https://c4e69d26b7e1.ngrok.io/static/pic/carePic_1.jpg',
                title=userMessage,
                text='確認商品',
                actions=[
                    MessageTemplateAction(
                        label='確認儲存', text='儲存完成'
                    )
                ]
            )
        )

    return message


def update_productDB(count, uid, userMessage):
    if count == 1:
        product = Product.objects.create(uid=uid, pbrand=userMessage)
    else:
        product = Product.objects.create(uid=uid, pname=userMessage)


def get_productDB(userid):
    product = Product.objects.filter(uid=userid)
    return product


def search_productDB(productname):
    try:
        ingred = CosmeticIngredient.objects.get(pname=productname)
    except:
        ingred = '查無此產品資訊'
    return ingred

def Compare_All_Product(userid, qName):
    # 從資料庫取得資料
    msg = ''
    qIngre = []
    try:
        ingred = CosmeticIngredient.objects.get(pname=qName)
        qIngre = ingred.ingredient.split(',')
        msg += '成功找到\n' + qName + '\n'

        checkIngre = []
        # Start to compare suitable & nonsuitable
        cnt = 0
        if len(qIngre) > 0:
            data = UserProduct.objects.filter(uid=userid)
            for i in range(len(qIngre)):
                try:
                    for j in range(len(data)):
                        try:
                            unfitprod = data[j].unfit_prod
                            unfit_Ingre = CosmeticIngredient.objects.get(pname__icontains=unfitprod).ingredient.split(',')
                        except:
                            msg += 'unfitprod出錯\n'
                        for k in range(len(unfit_Ingre)):
                            if unfit_Ingre[k].find(qIngre[i]) != -1:
                                checkIngre.append(unfit_Ingre[k])
                                break
                except:
                    msg += '麻煩請先紀錄您曾經使用過的不適合產品，再利用分析功能喔！\n'
                    break
            for i in range(len(checkIngre)):
                try:
                    for j in range(len(data)):
                        try:
                            fitprod = data[j].fit_prod
                            fit_Ingre = CosmeticIngredient.objects.get(pname__icontains=fitprod).ingredient.split(',')
                        except:
                            msg += 'fit出錯'
                        for k in range(len(fit_Ingre)):
                            if fit_Ingre[k].find(checkIngre[i]) != -1:
                                checkIngre.remove(fit_Ingre[k])
                                break

                except:
                    msg += '麻煩請先紀錄您曾經使用過的適合產品，再利用分析功能喔！'
                    break

        try:
            if len(checkIngre) > 0:
                msg += '產品有過去讓您不適的成分，如有需要建議查詢醫生的專業意見喔！'
            else:
                msg += '產品並沒有過去讓您不適的成分，可以考慮購買喔！'
        except:
            msg += '錯誤發生，請重新點選分析！'

    except:
        msg += '非常抱歉！我們暫時沒有收錄這款產品，如果您願意的話可以回報給客服喔！\n'

    return msg


