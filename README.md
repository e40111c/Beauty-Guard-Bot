# TKU Beauty guard bot

美妝守門人，協助使用者選購適合自身膚質的美妝品。

Beauty guard bot providing best selection for user

> 選購保養/彩妝品總是擔心成分有問題嗎？不曉得這款產品是否適合自己的皮膚，會不會產生過敏等不良反應呢？

透過過去使用產品的成分，分析比對選購產品的成分，讓你能夠快速找到適合自己的商品，

提供Qr code / 產品條碼掃描等功能，結合財政部API讓你商品儲存更加便利。

## Main function

1. 儲存功能 - 儲存產品，儲存現在使用的美妝/保養商品，方便成分記錄於資料庫。

2. 比對功能 - 儲存產品成分比對選購商品成分，分析得出是否建議購入該商品。
 
3. 搜尋功能 - 想得知某項商品成分，使用搜尋功能即可。
 
4. 推薦功能 - 輸入膚質、預算、產品類型，推薦適合使用者膚質的商品。

## Demo Video

<div align=center>
<a href="https://www.youtube.com/watch?v=kjDUKZ1lwKM" target="_blank"><img src="https://github.com/e40111c/LinebotProject/blob/master/static/demo.png" 
alt="圖片 ALT 文字放在這裡" width="500" height="300" border="10" /></a>
</div>

## Documentaion

### 儲存產品

1.Qr code 掃描發票後進行儲存。

2.產品條碼 掃描商品外部條碼後儲存。

3.bot儲存 使用內部功能儲存。

### 比對功能

輸入想要比對的商品後，系統自動與資料庫產品成分進行比對並加以分析後給出是否建議購入的回饋。

## System

Machine：GCP Cloud VPS with Apache Server

Back-end：Django with Beautiful Soup 

Front-end：Linebot，html，css，js

API：Ministry of Finance E-invoice Platform、Linebot API

