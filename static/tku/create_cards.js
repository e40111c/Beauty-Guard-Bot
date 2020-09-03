//從資料庫撈出使用者儲存的適合產品
//**連結資料庫後解開-開始**
//data = UserProduct.objects.filter(uid=userid);
//var unsuit_prod = data[j].unfit_prod;
//**連結資料庫後解開-結束**

//結束撈資料
document.open();

//var unsuit_prod = [pname,'專科美人專用畫眉筆']; //**需刪除** this is for testingl

var html_card = "<div class=\"owl-carousel owl-theme\" style = \"padding-top: 50px; padding-left: 33px;\">";
for(var i = 0; i < products.length; i++) {

        //Part1: create card
        html_card += "<div class=\"item\">";
        html_card += "<div class=\"card\" id = \"card_style\">";
        html_card +="<div class=\"flip-card\">";
        html_card +="<div class=\"flip-card-inner\">";
        html_card +="<div class=\"flip-card-front\">";
        html_card +="<div class=\"card-body\" style= \"padding: 0px; align-items: center;\">";

        //Part2: set card image and product name
        //**連結資料庫後解開**
        //var img_link = CosmeticIngredient.objects.get(pname=unsuit_prod[i]).imgLink

        var img_link = products[i].fields.picurl;

        //**需刪除** this is for testing
        
        html_card +="<!--Card image-->";
        html_card +="<div class=\"view overlay\" style=\"margin-top: 30%;margin-bottom: 10%;\">";
        html_card +="<img src=\""+img_link+"\" class=\"img-fluid\" alt=\"\">"; //img_link is the value to be changed
        html_card +="</div><h5 class=\"card-title\" style=\"text-align: center; margin:10px;\">"+products[i].fields.unfit_prod+"</h5>"; //suit_prod[i] is the value to be changed
        html_card +="<button class=\"btn btn-primary\" id=\"btnflip1\" style=\"display:inline-block;margin-left:35%;margin-top:10px;background-color: black;border-color: transparent;box-shadow: 0px 2px grey;\"\">產品成分</button></a></div></div>";
        
        //Part3: set card content(成分,EWG評分,4個指標)
        //(1) create table
        html_card +="<div class=\"flip-card-back\">";
        html_card += "<div class=\"card-body scroll\" style= \"padding: 0px;height:100%;\">";
        html_card += "<!--Card content--><div>";
        html_card += "<table class=\"table table-hover\">";
        html_card += "<thead class=\"table_head\"><tr>";
        html_card += "<th scope=\"col\">成分</th><th scope=\"col\">EWG評分</th><th scope=\"col\">致痘度</th><th scope=\"col\">滲透度</th><th scope=\"col\">刺激度</th><th scope=\"col\">安全度</th></tr></thead>";

        //(2) get data from databas
        //**連結資料庫後解開**
        //var ingre = CosmeticIngredient.objects.get(pname=unsuit_prod[i]).ingredient.split(',');
        //var ewg = CosmeticIngredient.objects.get(pname=unsuit_prod[i]).ewgscore.split(',');
        //var acne = CosmeticIngredient.objects.get(pname=unsuit_prod[i]).acne.split(',');
        //var dalton = CosmeticIngredient.objects.get(pname=unsuit_prod[i]).dalton.split(',');
        //var stimulation = CosmeticIngredient.objects.get(pname=unsuit_prod[i]).stimulation.split(',');
        //var safe = CosmeticIngredient.objects.get(pname=unsuit_prod[i]).safeness.split(',');

        //以下測試用,連資料庫後需刪除
        var ingre = products[i].fields.ingredient.split(',');
        var ewg = products[i].fields.score.split(',');
        var ace = products[i].fields.acne.split(',');
        var dal = products[i].fields.dalton.split(',');
        var stimulation = products[i].fields.stimulation.split(',')
        var saf = products[i].fields.safeness.split(',');
        
        //以上測試用,連資料庫後,需刪除
        
        for(var j = 0; j < ingre.length; j++){
            //need loop for ingredient start from here
            ingre[j] = String(ingre[j])
            ewg[j] = String(ewg[j])
            ace[j] = String(ace[j])
            dal[j] = String(dal[j])
            stimulation[j] = String(stimulation[j])
            saf[j] = String(saf[j])

            ewg[j] = ewg[j].replace('[','');
            ewg[j] = ewg[j].replace(']','');
                
            ingre[j] = ingre[j].replace('[','');
            ingre[j] = ingre[j].replace(']','');
            ingre[j] = ingre[j].replaceAll(`'`,'')
                
            ace[j] = ace[j].replace('[','');
            ace[j] = ace[j].replace(']','');

            dal[j] = dal[j].replace('[','');
            dal[j] = dal[j].replace(']','');

            stimulation[j] = stimulation[j].replace('[','');
            stimulation[j] = stimulation[j].replace(']','');

            saf[j] = saf[j].replace('[','');
            saf[j] = saf[j].replace(']','');


            html_card += "<tbody class = \"table_row\"><tr>";
            html_card += "<th scope=\"row\">"+ingre[j]+"</th><td>"+ewg[j]+"</td><td>"+ace[j]+"</td><td>"+dal[j]+"</td><td>"+stimulation[j]+"</td><td>"+saf[j]+"</td></tr>";
            //end loop
        }
        html_card += "</tbody></table></div></div>";
        html_card +="<button class=\"btn btn-primary\" id=\"btnflip2\" style=\"display:inline-block; margin-left:75%;margin-top:10px;background-color: black;border-color: transparent;box-shadow: 0px 2px grey;\">Back</button>";
        html_card +="</div></div></div></div></div>";

}
html_card += "</div></div>";
document.write(html_card)
