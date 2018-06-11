 window.onload=function () {

    function changeNum()
    {
    //购物车数量的点击
    //点击增加按钮
    //数量+1
    //控制数量不可以手动输入
    //计算总价(数量*单价)
        var  getAdd = document.getElementsByClassName("add");

        var getReduce = document.getElementsByClassName("reduce");

        var sumprice = 0 ;


        for(var i =0 ; i<getAdd.length; i++){
            getNum(i);

            }

        function getNum(i) {
            //数量增加

            getAdd[i].onclick = function () {
                //将该条记录的checkbox设置成 true
                getAdd[i].parentNode.parentNode.firstElementChild.firstElementChild.checked = "true";
               var num = parseInt(getAdd[i].previousElementSibling.value);
                num++;

               getAdd[i].previousElementSibling.value = num;
               //对应数量的变化
                //获取单价
                var price = getAdd[i].parentNode.previousElementSibling.innerHTML;
                //去掉单位
                var price = parseFloat(price.replace("$",""));

                //获取subtotal
                var sum = price * num;
                sumprice = sumprice + sum;

               getAdd[i].parentNode.nextElementSibling.innerHTML = sum.toFixed(2);
               document.getElementById("totalnum").innerHTML = sumprice.toFixed(2);




        var NextisCheck = 0;
         var checkbox = document.getElementsByClassName("checkbox");
      for(var j= 0; j<checkbox.length; j++){

            if (checkbox[j].firstElementChild.checked == true){

                 NextisCheck = NextisCheck +1;
                   document.getElementById("selectedTotal").innerHTML = NextisCheck;
            }
      };

            }


            //数量减少：
            getReduce[i].onclick = function () {

                getAdd[i].parentNode.parentNode.firstElementChild.firstElementChild.checked = "true";

             var num = getReduce[i].nextElementSibling.value;
                if (num>1){
                     num--;
                }
                else{
                   num = 1;
                }

                 getReduce[i].nextElementSibling.value = num;

                 //对应数量的变化
                var price = getAdd[i].parentNode.previousElementSibling.innerHTML;
                //去掉单位
                var price = parseFloat(price.replace("$",""));

                //获取subtotal
                var sum = price * num;

                    sumprice = sumprice - price;  //减去的数量有bug；如果连续点击-

               getAdd[i].parentNode.nextElementSibling.innerHTML = sum.toFixed(2);
                   document.getElementById("totalnum").innerHTML = sumprice.toFixed(2);

                           var NextisCheck = 0;
         var checkbox = document.getElementsByClassName("checkbox");
      for(var j= 0; j<checkbox.length; j++){

            if (checkbox[j].firstElementChild.checked == true){

                 NextisCheck = NextisCheck +1;
                   document.getElementById("selectedTotal").innerHTML = NextisCheck;
            }
      };


            }



        }






    }
    changeNum();




  //全选并计算商品总额
    var CheckAll = document.getElementsByClassName("CheckAll")[0].children[0];
     var checkbox = document.getElementsByClassName("checkbox");

    CheckAll.onclick = function(){
        var totalSum = 0;



        for(var i = 0 ;i<checkbox.length; i++){

            if(CheckAll.checked == true){

                 checkbox[i].firstElementChild.checked = true;
                 document.getElementById("selectedTotal").innerHTML = checkbox.length;
                totalSum = totalSum + parseFloat(checkbox[i].parentNode.children[4].innerHTML);
                 //合计商品总额
                    document.getElementById("totalnum").innerHTML = totalSum.toFixed(2);


                //     //在全选的情况下，点击取消了某一个选项
                // function ss(num,b) {
                //     var realtest = document.getElementById("selectedTotal").innerHTML;
                //     checkbox[num].addEventListener('click',function () {
                //        //判断是否处于选中状态
                //             b=5;
                //         console.log("为啥这个是5：：：：："+realtest);
                //             alert("realtest是"+realtest);
                //             alert("checkbox[num].firstElementChild.checked:::::::"+checkbox[num].firstElementChild.checked);
                //         if(checkbox[num].firstElementChild.checked == false){
                //
                //
                //             document.getElementById("selectedTotal").innerHTML = b -1;
                //              console.log("局部变量里的b是******"+b);
                //         }
                //         else if(checkbox[num].firstElementChild.checked == true){
                //              console.log("局部变量里的b22222是******"+b);
                //            document.getElementById("selectedTotal").innerHTML = b+1;
                //         }
                //     },false)
                //
                // }
                // ss(i,b);



            }
            else{
                checkbox[i].firstElementChild.checked = false;
                document.getElementById("selectedTotal").innerHTML = 0;
                document.getElementById("totalnum").innerHTML  = 0;

            }

        }
    }






//部分选择商品,并计算

    for(var j = 0; j<checkbox.length;j++){

        getClickTotal(j);

    }

  var isCheck = document.getElementById("selectedTotal").innerHTML;
      console.log("isCheck的值是~~~~~~~~~"+isCheck);
    function  getClickTotal(j){


        checkbox[j].onclick = function () {

            //先判断除了自己之外的，有没有checkbox = true;
            for(var k=0;k<checkbox.length;k++){

                if(checkbox[k].children[0].checked == true){
                    isCheck = isCheck-1+1;
                    // alert("for循环里的isCheck"+isCheck);
                }
            }

            //自己本身判断，被选中+1
              if(checkbox[j].children[0].checked == true){
                  isCheck = isCheck +1;

                  //已经选择了
                   document.getElementById("selectedTotal").innerHTML = isCheck;
                   if(isCheck == 5){
                       document.getElementsByClassName("CheckAll")[0].children[0].checked = true;
                   }
              }
              else {



                   isCheck = isCheck - 1
                   document.getElementById("selectedTotal").innerHTML = isCheck;
              }
        };

    }





}