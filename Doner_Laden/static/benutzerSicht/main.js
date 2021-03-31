$(document).ready(function(){
    
    // $('#orderModal').on('show.bs.modal', function(e){
        
    //     var productID = $(e.relatedTarget).data('product-id');
    //     // alert(productID);
    //     //$(e.currentTarget).find('input[name="counter"]').val(productID);
    //   });
    $('.building-link').click(function(){
        $('#building-name').html($(this).data('name'));
        var product_price = $(this).data('price');
        $("#product-price").val(product_price)
        var product_id = $(this).data('id');
        // $("#counter").val(ss);
        $("#pID").val(product_id);
        // hole from input $("#counter").val()
    });
   
}); 


