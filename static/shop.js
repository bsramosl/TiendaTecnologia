var $ = jQuery.noConflict();

function shop() {
  $.ajax({
    url: window.location.pathname,
    type: 'POST',
    data: {
      'action': 'cargar',
    },
    dataType: 'json',
  }).done(function (data) {
    document.getElementById('busca').style.display = 'block';
    let res = document.querySelector('#sho')
    res.innerHTML = '';
    for (let item of data) { 
        if (item.stock == 0 ){
            item.stock = '<span class="text-xs uppercase font-bold text-black ">outstock</span>';
        }
        else{
            item.stock = '<span class="text-xs uppercase font-bold text-white bg-green-300 py-1 px-2 rounded-md">instock</span>';
        }
 
      res.innerHTML += `
      <div class="mix mix-main col-span-12 sm:col-span-6 lg:col-span-4 h-auto">
      <div class="card-container h-full flex flex-col p-5 bg-white rounded-lg shadow-md hover:shadow-xl relative transition-all-300 hover:z-[2] translateY-2 overflow-hidden">
          <div class="absolute top-[10px] right-[10px]"> 
              <div class="p-[2px]">
                  <a onclick="view(${item.id})" class="tippy tippy-left-card-view btn-open-modal flex justify-center items-center h-9 w-9 bg-[rgba(0,0,0,.3)] hover:bg-primary-hover rounded-lg transition-all-300 cursor-pointer" href="javascript:void(0)" data-target=".quick-view-modal">
                      <i class="bi bi-eye text-xl text-white flex pointer-events-none"></i>
                  </a>
              </div>
          </div>
         
          


          <div class="h-[190px] overflow-hidden rounded-lg">
              <a href="/ProductDetail/${item.id}/">
                  <img class="card-object-fit w-full h-full" src="${item.image}" alt="product" />
              </a>
          </div>
          
          
          <div class="my-1">
              <a class="clamp font-medium break-all" href="#"> ${item.name} </a>
          </div>
          <div class="my-1">
              <p class="text-sm clamp-2 text-gray-400"> ${item.descripcion}</p>
          </div>
          <div class="flex gap-2 my-2">
              <span class="font-bold">Size:</span>
              <ul class="flex gap-3">
                  <li>S</li>
                  <li>M</li>
                  <li>L</li>
                  <li>XL</li>
              </ul>
          </div>
          <div class="flex gap-2 my-2">
              <div class="block h-3 w-3 bg-blue-600 rounded-full"></div>
              <div class="block h-3 w-3 bg-red-600 rounded-full"></div>
              <div class="block h-3 w-3 bg-yellow-600 rounded-full"></div>
              <div class="block h-3 w-3 bg-black rounded-full"></div>
          </div>
          <div class="my-1">
              <span class="text-lg font-bold">$${item.price}</span>
              <span class="text-sm text-primary-color line-through">  </span>
          </div>
          <div class="mt-auto">
              <a class="btn-effect flex justify-center items-center w-full p-2 bg-primary-color rounded-lg transition-all-300" href="/ProductDetail/${item.id}/">
                  <span class="font-bold uppercase text-white">View details</span>
              </a>
          </div>
      </div>
  </div> 
`}

  }).fail(function (jqXHR, textStatus, errorThrown) {
  }).always(function (data) {
  });
};



$("#submitButton").click(function () { 
  var ids = document.querySelectorAll("input[name='id[]']:checked");
  var consulta = $("#search").val();   
	var a=[]; 
	for (var i=0; i<ids.length; i++) { 
		a.push(ids[i].value);
	} 
  $.ajax({
    url: window.location.pathname,
    type: 'POST',
    data: {
      'action': 'filter',
      'category': a , 
      'search': consulta,
    },
    dataType: 'json',
  }).done(function (data) { 
    document.getElementById('busca').style.display = 'block';
    let res = document.querySelector('#sho')
    res.innerHTML = '';
    for (let item of data) {
      res.innerHTML += `
            <div class="mix mix-main col-span-12 sm:col-span-6 lg:col-span-4 h-auto">
            <div class="card-container h-full flex flex-col p-5 bg-white rounded-lg shadow-md hover:shadow-xl relative transition-all-300 hover:z-[2] translateY-2 overflow-hidden">
                <div class="absolute top-[10px] right-[10px]"> 
                    <div class="p-[2px]">
                        <a onclick="view(${item.id})" class="tippy tippy-left-card-view btn-open-modal flex justify-center items-center h-9 w-9 bg-[rgba(0,0,0,.3)] hover:bg-primary-hover rounded-lg transition-all-300 cursor-pointer" href="javascript:void(0)" data-target=".quick-view-modal">
                            <i class="bi bi-eye text-xl text-white flex pointer-events-none"></i>
                        </a>
                    </div>
                </div>
               
                


                <div class="h-[190px] overflow-hidden rounded-lg">
                    <a href="/ProductDetail/${item.id}/">
                        <img class="card-object-fit w-full h-full" src="${item.image}" alt="product" />
                    </a>
                </div>
                
                
                <div class="my-1">
                    <a class="clamp font-medium break-all" href="#"> ${item.name} </a>
                </div>
                <div class="my-1">
                    <p class="text-sm clamp-2 text-gray-400"> ${item.descripcion}</p>
                </div>
                <div class="flex gap-2 my-2">
                    <span class="font-bold">Size:</span>
                    <ul class="flex gap-3">
                        <li>S</li>
                        <li>M</li>
                        <li>L</li>
                        <li>XL</li>
                    </ul>
                </div>
                <div class="flex gap-2 my-2">
                    <div class="block h-3 w-3 bg-blue-600 rounded-full"></div>
                    <div class="block h-3 w-3 bg-red-600 rounded-full"></div>
                    <div class="block h-3 w-3 bg-yellow-600 rounded-full"></div>
                    <div class="block h-3 w-3 bg-black rounded-full"></div>
                </div>
                <div class="my-1">
                    <span class="text-lg font-bold">$${item.price}</span>
                    <span class="text-sm text-primary-color line-through">  </span>
                </div>
                <div class="mt-auto">
                    <a class="btn-effect flex justify-center items-center w-full p-2 bg-primary-color rounded-lg transition-all-300" href="/ProductDetail/${item.id}/">
                        <span class="font-bold uppercase text-white">View details</span>
                    </a>
                </div>
            </div>
        </div> 
 `}
   
  }).fail(function (jqXHR, textStatus, errorThrown) {
  }).always(function (data) {
  }); 
  return false;
});

 