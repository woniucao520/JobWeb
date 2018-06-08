



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
        for(var i =0 ; i<getAdd.length; i++){
            getNum(i);

            }

        function getNum(i) {
            getAdd[i].onclick = function () {
               var num = getAdd[i].previousElementSibling.value;

               num++;
               getAdd[i].previousElementSibling.value = num;

            }

            getReduce[i].onclick = function () {

                 var num = getReduce[i].nextElementSibling.value;
                 num--;
                 getReduce[i].nextElementSibling.value = num;



            }



        }







    }
    changeNum()




}
