$(document).ready(function () {
    var notification = $('#notification');
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        },
            5000);
    }

    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');

        $('#exampleModal').modal('show');
    });

    // Click on the button to close the cart windows
    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    // Delivery method selection radio button event handler
    $("input[name='requires_delivery']").change(function() {
        var selectedValue = $(this).val();
        // Hide or show shipping address inputs
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });

});