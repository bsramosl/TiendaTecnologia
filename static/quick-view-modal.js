var $ = jQuery.noConflict();

function view(id){
    $.ajax({
        url: "/modales/",
        type: 'POST',
        data: {
          'action': 'view',
          'id':id , 
        },
        dataType: 'json',
      }).done(function (data) { 
        //document.getElementById('wid').innerHTML = data[0].id;
        document.getElementById('wname').innerHTML = data[0].name;
        //document.getElementById('wcategory').innerHTML = data[0].category;
        document.getElementById('wdescripcion').innerHTML = data[0].descripcion;
        document.getElementById('wimage').innerHTML = 
        ' <img   src=' + data[0].image + '/>';
        document.getElementById('wimage2').innerHTML = 
        ' <img  src=' + data[0].image2 + '/>';
        document.getElementById('wimage3').innerHTML = 
        ' <img  src=' + data[0].image3 + '/>';
        document.getElementById('wimage4').innerHTML = 
        ' <img   src=' + data[0].image + '/>';
        document.getElementById('wimage5').innerHTML = 
        ' <img  src=' + data[0].image2 + '/>';
        document.getElementById('wimage6').innerHTML = 
        ' <img  src=' + data[0].image3 + '/>';      
        document.getElementById('wprice').innerHTML = data[0].price;
        document.getElementById('add').innerHTML = '<a onclick="add_cart('+data[0].id+');" class="btn-effect flex justify-center items-center h-full w-full p-2 bg-primary-color rounded-lg gap-2 transition-all-300" type="submit"><i class="bi bi-cart-fill text-xl text-white flex"></i><span class="font-bold uppercase text-white">Add to cart</span></a>';

        if (data[0].stock == 0 ){
            document.getElementById('wstock').innerHTML = '<span class="text-xs uppercase font-bold text-black ">outstock</span>';
        }
        else{
            document.getElementById('wstock').innerHTML = '<span class="text-xs uppercase font-bold text-white bg-green-300 py-1 px-2 rounded-md">instock</span>';
        }

 
      }).fail(function (jqXHR, textStatus, errorThrown) {
      }).always(function (data) {
      }); 

}

 