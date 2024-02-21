var $ = jQuery.noConflict();
var dat = [];
var tbldata;
var sale = {
    items: {
        cli: '',
        date_joined: '',
        subtotal: 0.00,
        iva: 0.00,
        total: 0.00,
        products: []
    }, calculate_invoice: function(){        
        var subtotal= 0.00;
        var iva= 0.12;        
        $.each(this.items.products,function(pos,dict){
            dict.subtotal = dict.cant * parseFloat(dict.products.price);
            subtotal+=dict.subtotal
        });
        this.items.subtotal= subtotal;
        this.items.iva = this.items.subtotal * iva;
        this.items.total = this.items.subtotal + this.items.iva;
        document.getElementById('subtotal').innerHTML = this.items.subtotal.toFixed(2);
        document.getElementById('iva').innerHTML = this.items.iva.toFixed(2);
        document.getElementById('total').innerHTML = this.items.total.toFixed(2);
        $('input[name="subtotal"]').val(this.items.subtotal.toFixed(2));
        $('input[name="iva"]').val(this.items.iva.toFixed(2));
        $('input[name="total"]').val(this.items.total.toFixed(2));
    },    
    list: function () {    
        this.calculate_invoice(); 
        tbldata = $('#data').DataTable({
            searching: false, 
            paging: false,
            info: false,  
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.products,                                   
            columns: [
                {"data": "producto_id"},
                {"data": "nombre"},
                {"data": "cantidad"},
                {"data": "price"}, 
                {"data": "acumulado"},  
            ], 
            columnDefs: [ 
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<img src="'+ row.products.image +'" alt="" height="40" width="40"/>';
                    }
                }, 
                {targets: [1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<td>'+row.products.nombre+'</td>';
                    }
                }, 
                {targets: [2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<td>'+row.products.price+'</td>';
                    }
                }, 
                {
                    targets: [3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<div class="quantity inline-flex bg-white rounded-lg shadow"><input type="number" name="cant" id="cant" class="quantity-value input-number w-12 text-center text-lg p-1 bg-transparent text-gray-400 border-none focus:ring-0 focus:border-none" autocomplete="off" value="'+row.cant+'"></div>';
                    }
                },
                {targets: [4],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<td>'+row.subtotal+'</td>';
                    }
                }, {
                    targets: [5],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a onclick="delete_cart('+row.products.producto_id+')" rel="remove" class="tippy tippy-remove btn-delete text-slate-400 hover:text-primary-color transition-all-300"><i class="bi bi-trash-fill inline pointer-events-none text-xl"></i></a>';
                    }
                }
            ],
            rowCallback(row, data,){ 
                $(row).find('input[name="cant"]').TouchSpin({
                    min: 1,
                    max:50,
                    step: 1, 
                    buttondown_class: "quantity-btn decrement text-primary-color",
                    buttonup_class: "quantity-btn increment text-primary-color",
                    buttonup_txt:   '<i onclick="add_cart('+data.products.producto_id+')" class="bi bi-caret-up-fill"></i>',
                    buttondown_txt:'<i onclick="restar_cart('+data.products.producto_id+')" class="bi bi-caret-down-fill"></i>',
                }); 
            },             
            initComplete: function (settings, json) {

            }
        });
    },
    
};


function add(){  
    for (const rec of dat) { 
        var item=[];        
        item.cant = rec.cantidad ;
        item.subtotal = rec.acumulado ;  
        item.products = rec;
        sale.items.products.push(item)      
      }
    sale.list();  
}
 

function cart() {  
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': 'cargar',             
        },
        dataType: 'json',  
    }).done(function(data){    
        dat.push(data);  
        dat = dat.shift();
        add();  
    }).fail(function (jqXHR, textStatus, errorThrown) {
    }).always(function (data) {
    });   
};




$('#data tbody')
.on('click','a[rel="remove"]',function(){
    var tr = tbldata.cell($(this).closest('td, li')).index();
    sale.items.products.splice(tr.row,1);
    sale.list();
}) 
.on('change','input[name="cant"]',function(){ 
    var cant = parseInt($(this).val());
    var tr = tbldata.cell($(this).closest('td, li')).index();
    sale.items.products[tr.row].cant = cant; 
    sale.calculate_invoice();
    $('td:eq(4)',tbldata.row(tr.row).node()).html('$'+ sale.items.products[tr.row].subtotal.toFixed(2));  
});




 