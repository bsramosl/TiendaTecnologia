var $ = jQuery.noConflict(); 
  
window.onload = function() {  
  $.ajax({
      url:  "/inicio_major/",
      type: 'POST',
      data: {
          'action': 'cargar',             
      },
      dataType: 'json', 
  }).done(function(data){     
    document.getElementById('loader').innerHTML = data[0].name;
    document.getElementById('email').innerHTML = data[0].email;
    document.getElementById('phone').innerHTML = data[0].phone;
    document.getElementById('email-footer').innerHTML = data[0].email;
    document.getElementById('phone-footer').innerHTML = data[0].phone;
    document.getElementById('address').innerHTML = data[0].address;
    document.getElementById('logo').innerHTML = 
    ' <img class= "inline" style="max-width:190px; max-height:50px;" src=' + data[0].logo + '/>';
     
    refresh_cart();
 
  }).fail(function (jqXHR, textStatus, errorThrown) {
  }).always(function (data) {
  });   
};


function refresh_cart(){  
  $.ajax({
      url: "/refresh_cart/",
      type: 'POST',
      data: {
        'action': 'refresh', 
      },
      dataType: 'json',
    }).done(function (data) { 
      total = 0;
      let res = document.querySelector('#res')
      res.innerHTML = '';
      for (let item of data) { 
        total+= item.acumulado ;
        res.innerHTML += `
        <div class="hidden flex-col justify-center items-center p-5 gap-4">
        <i class="bi bi-cart-x text-8xl text-gray-200"></i>
        <p class="font-semibold">There are no products in the cart.</p>
        <a class="btn-effect flex justify-center items-center p-2 bg-primary-color rounded-lg gap-2 transition-all-300" href="#">
          <span class="font-bold uppercase text-white">Go to the store</span>
        </a>
      </div>
      <!-- -->
      <a  onclick="delete_cart(${item.producto_id})" class="bg-white hover:bg-gray-100 flex justify-between items-center gap-5 h-[100px] w-full p-2 transition-all-300" href="#">
        <div class="border rounded-lg h-[80px] w-[80px] min-w-[80px] overflow-hidden">
          <img class="w-full h-full object-cover" src="${item.image}" alt="product" />
        </div> 
        <div class="flex flex-col w-full">
          <h6 class="font-semibold text-lg clamp-2 break-all">${item.nombre}</h6>
          <div class="flex gap-2">
            <div class="flex gap-1 leading-7 text-gray-400">
              <span>${item.cantidad}</span>
              <span>X</span>
            </div>
            <div class="flex gap-2 items-center">
              <span class="font-bold text-primary-color">${item.acumulado}</span>
            </div>
          </div>
        </div>

        <div class="flex text-slate-400 hover:text-primary-color transition-all-300">
          <i  class="bi bi-trash-fill text-2xl pointer-events-none"></i>
        </div>
      </a>
      
   `} 
    document.getElementById('sub').innerHTML =  '$'+total;
    document.getElementById('totalitems').innerHTML =  data.length;
    
    
    }).fail(function (jqXHR, textStatus, errorThrown) {
    }).always(function (data) {
    });  
}


function add_cart(id){ 
    $.ajax({
        url: "/cart/",
        type: 'POST',
        data: {
          'action': 'add',
          'id':id , 
        },
        dataType: 'json',
      }).done(function (data) {  
        refresh_cart(); 
      }).fail(function (jqXHR, textStatus, errorThrown) {
      }).always(function (data) {
      });  
}


function delete_cart(id){ 
    $.ajax({
        url: "/cart/",
        type: 'POST',
        data: {
          'action': 'delete',
          'id':id , 
        },
        dataType: 'json',
      }).done(function (data) {   
        refresh_cart();
      }).fail(function (jqXHR, textStatus, errorThrown) {
      }).always(function (data) {
      });  
}

function restar_cart(id){ 
  $.ajax({
      url: "/cart/",
      type: 'POST',
      data: {
        'action': 'restar',
        'id':id , 
      },
      dataType: 'json',
    }).done(function (data) {  
      refresh_cart();
    }).fail(function (jqXHR, textStatus, errorThrown) {
    }).always(function (data) {
    });  
} 

  