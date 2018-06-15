window.onload = function () {


    //获取checkbox 复选框
    var selectInputs = document.getElementsByClassName("check");
    //获取全选按钮
    var checkall = document.getElementsByClassName("checkall");
    //增加按钮
    var  getAdd = document.getElementsByClassName("add");
    //减少按钮
    var getReduce = document.getElementsByClassName("reduce");
    //删除按钮
    var  del =  document.getElementsByClassName("delete");

    var deleteall = document.getElementById("deleteAll");




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

        //已经选择的商品个数

        //循环表格
        for(var i = 0; i< tr.length ; i++){

            var isCheck = tr[i].getElementsByClassName("check-one");

            if(isCheck[0].checked == true){
                //获取单价
                var price = parseFloat(tr[i].cells[2].innerHTML.replace("$",""));

                //获取个数
                var num = parseInt(tr[i].cells[3].getElementsByClassName("count_input")[0].value);



                selectedTotal = selectedTotal + num;



                //获取总计
                var subtotal = parseFloat(tr[i].cells[4].innerHTML);
                totalNum = totalNum + subtotal;




            }

        }


        totalnum.innerHTML = totalNum;//总价格
        document.getElementById("selectedTotal").innerHTML = selectedTotal;//总个数


    }


            //每行，数量*金额 小计
        function  subTotal(i) {

                //获取单价
                var price = parseFloat(tr[i].cells[2].innerHTML.replace("$",""));


                //获取个数
                var num = parseInt(tr[i].cells[3].getElementsByClassName("count_input")[0].value);



                var sumprice = price * num

                tr[i].cells[4].innerHTML = sumprice.toFixed(2);

        }







    for(var j = 0; j< tr.length ; j++){

        getsubInputs(j);
    }



    function  getsubInputs(j) {

        //数量增加，减少的点击事件的触发
        getAdd[j].onclick = function () {
            alert("增加按钮的j是"+j);

            getAdd[j].parentNode.parentNode.firstElementChild.firstElementChild.checked = "true";
            var num = parseInt(getAdd[j].previousElementSibling.value);

                num++;
                getAdd[j].previousElementSibling.value = num;
                subTotal(j);
                 getTotal();

        }


        //数量减少，事件触发
        getReduce[j].onclick = function () {
            alert("这是减少的第*****个:"+j);
              getReduce[j].parentNode.parentNode.firstElementChild.firstElementChild.checked = "true";

             var num = getReduce[j].nextElementSibling.value;
                if (num>1){
                     num--;
                }
                else{
                   num = 1;
                }

                 getReduce[j].nextElementSibling.value = num;
                 subTotal(j);
                 getTotal();

        }

                    //单条记录的删除
                   del[j].onclick = function () {

                            alert("这是减少的第*****个:"+j);
                    //给个提示框
                    var conf = confirm("确定要删除吗？");
                    if(conf){

                    this.parentNode.parentNode.parentNode.removeChild(this.parentNode.parentNode);

                    }
                  //删除后重新计算

                    for(var i = 0 ;i < selectInputs.length; i++){
                            console.log("目前还有checkbox按钮的个数"+selectInputs.length);
                                getselectInputs(i);  //解决循环总是最后一个i值的闭包问题。

                        }


                    for(var j = 0; j< tr.length ; j++){

                            getsubInputs(j);
                        }

                    getTotal()

                        }


    }


        //全选删除
        deleteall.onclick = function () {
            //如果全选按钮没有选择，提示:请选择商品
            if(selectedTotal.innerHTML != 0){
                var con = confirm("确定要删除所选商品吗？");
                if(con){
                    for(var j = 0 ;j < tr.length ; j++){
                            console.log("循环了几个j"+j);
                        //如果处于选中状态
                        if(tr[j].getElementsByClassName("check")[0].checked){

                            console.log("删除选中的第："+ j +"***********"+ tr[j].innerHTML);
                            //删除选中的这个状态
                            tr[j].parentNode.removeChild(tr[j]);
                            j--; //为了解决索引提前，导致删除遗漏掉删除元素;
                        }
                    }
                }


            }else{
                alert("请选择商品！");
            }

        getTotal();
        }




    for(var i = 0 ;i < selectInputs.length; i++){
        console.log("目前还有checkbox按钮的个数"+selectInputs.length);
            getselectInputs(i);  //解决循环总是最后一个i值的闭包问题。

    }


    function getselectInputs(i) {

        selectInputs[i].onclick = function () {

            //如果处于全选状态//使用indexof方法判断是否含有checkall 字符串
            if( selectInputs[i].className === "checkall check"){

                //将所有的状态改为check：true;
                for(var j = 0 ;j<selectInputs.length; j++){
                    console.log("删除后的selectInputs个数是"+selectInputs.length);
                    selectInputs[j].checked = this.checked;

                }


            }

            if(!this.checked ){
                //如果有一个未选中，取消全选状态
                for(var k = 0; k < checkall.length; k++){
                    checkall[k].checked = false;
                }

            }

            //选择完毕后，开始计算
            getTotal();

        }



    }








    


}