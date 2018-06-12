window.onload = function () {


    //获取checkbox 复选框
    var selectInputs = document.getElementsByClassName("check");
    //获取全选按钮
    var checkall = document.getElementsByClassName("checkall");


    //获取表格的每一行
    var tr = document.getElementsByTagName("tbody")[0].children;

    var selectedTotal = document.getElementById("selectedTotal");//已经选择的数量
    var totalnum = document.getElementById("totalnum"); //总价



    //计算：选中后的数量 与 总价
    function getTotal() {
        //已经选择的商品数量
        var selectedTotal = 0 ;
        //商品总数
        var totalNum = 0 ;


        //循环表格
        for(var i = 0; i< tr.length ; i++){

            var isCheck = tr[i].getElementsByClassName("check-one");

            if(isCheck[0].checked == true){
                //获取单价
                var price = parseFloat(tr[i].cells[2].innerHTML.replace("$",""));

                //获取总计
                var subtotal = parseFloat(tr[i].cells[4].innerHTML);
                totalNum = totalNum + subtotal;


            }

        }


        totalnum.innerHTML = totalNum;//总价格


    }





    //前面的复选框点击事件
    for(var i = 0 ;i < selectInputs.length; i++){
            getselectInputs(i);  //解决循环总是最后一个i值的闭包问题。
    }

    function getselectInputs(i) {
        selectInputs[i].onclick = function () {


            //如果处于全选状态//使用indexof方法判断是否含有checkall 字符串
            if( selectInputs[i].className.indexOf("checkall")>=0){
                //将所有的状态改为check：true;
                for(var j = 0 ;j<selectInputs.length; j++){
                    selectInputs[j].checked = this.checked;

                }

                if(this.checked == true){
                    document.getElementById("selectedTotal").innerHTML = tr.length-1;
                }
                if(this.checked == false){
                    document.getElementById("selectedTotal").innerHTML = 1;
                }

            }

            if(this.checked == false){
                //如果有一个未选中，取消全选状态
                for(var k = 0; k < checkall.length; k++){
                    checkall[k].checked = false;
                }


                 var count = parseInt(document.getElementById("selectedTotal").innerHTML);
                if(count <=0){
                    document.getElementById("selectedTotal").innerHTML = 0;
                }
                document.getElementById("selectedTotal").innerHTML = count-1;
            }
            //
            if(this.checked == true ){
               var count = parseInt(document.getElementById("selectedTotal").innerHTML)+1;
               document.getElementById("selectedTotal").innerHTML = count;
            }


            //选择完毕后，开始计算
            getTotal();




        }
    }



    //数量增加，减少的点击事件的触发

    


}