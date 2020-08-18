//從資料庫撈出使用者儲存的適合產品

//**連結資料庫後解開-開始**
//data = UserProduct.objects.filter(uid=userid);
//var unsuit_prod = data[j].unfit_prod;
//**連結資料庫後解開-結束**

//結束撈資料
document.open();
var unsuit_prod = ["SUNPLAY水凝清爽防曬露SPF25 PA++","純淨輕透防禦乳 spf50+ pa+++","C","D","E","F"]; //**需刪除** this is for testing

var html_card = "<div class=\"owl-carousel owl-theme\" style = \"padding-top: 50px; padding-left: 33px;\">";
for(var i = 0; i < unsuit_prod.length; i++){
    //var pType = CosmeticIngredient.objects.get(pname=unsuit_prod[i]).type
    var pType = "Cosmetics"; //**需刪除** this is for testing
    if(pType == "Cosmetics"){
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
        var img_link = 'https://drive.google.com/uc?export=download&id=1OVNiLh90lHWS60WLL1fyNf8-6n5w0WJ3'; //**需刪除** this is for testing
        
        html_card +="<!--Card image-->";
        html_card +="<div class=\"view overlay\" style=\"margin-top: 30%;margin-bottom: 10%;\">";
        html_card +="<img src=\""+img_link+"\" class=\"img-fluid\" alt=\"\">"; //img_link is the value to be changed
        html_card +="</div><h5 class=\"card-title\" style=\"text-align: center; margin:10px;\">"+unsuit_prod[i]+"</h5>"; //suit_prod[i] is the value to be changed
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
        var ingre = ["Iron Oxides","Prunus Speciosa Leaf Extract","Alpha-isomethyl ionone","Isopropyl Myristate","Camellia Sinensis Leaf Extract","Polyquaternium-51","Limonene","Alumina"];
        var ewg = ['2分 (安全)', '1分 (安全)', '1分 (安全)', '1分 (安全)', '1分 (安全)', '1分 (安全)', '5分 (普通)', '2分 (安全)'];
        var acne = ['0', '0', '0', '5', '0', '0', '0', '0'];
        var dalton = ['159.69', 'None', 'None', '270.5', 'None', '437.5', '136.23', '101.961'];
        var stimulation = ['0', '0', '0', '3', '0', '0', '0', '0'];
        var safe = ['2', '1', '3', '1', '1-2', '1', '4-5','2'];
        //以上測試用,連資料庫後,需刪除

        for(var j = 0; j < ingre.length; j++){
            //need loop for ingredient start from here
            html_card += "<tbody class = \"table_row\"><tr>";
            html_card += "<th scope=\"row\">"+ingre[j]+"</th><td>"+ewg[j]+"</td><td>"+acne[j]+"</td><td>"+dalton[j]+"</td><td>"+stimulation[j]+"</td><td>"+safe[j]+"</td></tr>";
            //end loop
        }
        html_card += "</tbody></table></div></div>";
        html_card +="<button class=\"btn btn-primary\" id=\"btnflip2\" style=\"display:inline-block; margin-left:75%;margin-top:10px;background-color: black;border-color: transparent;box-shadow: 0px 2px grey;\">Back</button>";
        html_card +="</div></div></div></div></div>";
    }
}
html_card += "</div></div>";
document.write(html_card)
