// When the html is drawn
$(document).ready(function () {
  // take markup element with id jq-notification for ajax notifications into a variable
  var successMessage = $("#jq-notification");

  // Catch the event of a click on the add to cart button
  $(document).on("click", ".add-to-cart", function (e) {
    // Blocking his base action
    e.preventDefault();

    // We take the counter element in the basket icon and take the value from there
    var goodsInCartCount = $("#goods-in-cart-count");
    var cartCount = parseInt(goodsInCartCount.text() || 0);

    // Get product id from data-product-id attribute
    var product_id = $(this).data("product-id");

    // From the href attribute we take the link to the django controller
    var add_to_cart_url = $(this).attr("href");

    // make post request via ajax without reloading the page
    $.ajax({
      type: "POST",
      url: add_to_cart_url,
      data: {
        product_id: product_id,
        csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
      },
      success: function (data) {
        // message
        successMessage.html(data.message);
        successMessage.fadeIn(400);
        // After 5sec, clear the message
        setTimeout(function () {
          successMessage.fadeOut(400);
        }, 5000);

        // Increase the number of items in the cart (rendering in the template)
        cartCount++;
        goodsInCartCount.text(cartCount);

        // Change the contents of the shopping cart to the django response (new rendered fragment of the cart markup)
        var cartItemsContainer = $("#cart-items-container");
        cartItemsContainer.html(data.cart_items_html);
      },

      error: function (data) {
        console.log("Ошибка при добавлении товара в корзину");
      },
    });
  });

  // Ловим собыитие клика по кнопке удалить товар из корзины
  $(document).on("click", ".remove-from-cart", function (e) {
      // Блокируем его базовое действие
      e.preventDefault();

      // Берем элемент счетчика в значке корзины и берем оттуда значение
      var goodsInCartCount = $("#goods-in-cart-count");
      var cartCount = parseInt(goodsInCartCount.text() || 0);

      // Получаем id корзины из атрибута data-cart-id
      var cart_id = $(this).data("cart-id");
      // Из атрибута href берем ссылку на контроллер django
      var remove_from_cart = $(this).attr("href");

      // делаем post запрос через ajax не перезагружая страницу
      $.ajax({

          type: "POST",
          url: remove_from_cart,
          data: {
              basket_id: cart_id,
              csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
          },
          success: function (data) {
              // Сообщение
              successMessage.html(data.message);
              successMessage.fadeIn(400);
              // Через 7сек убираем сообщение
              setTimeout(function () {
                  successMessage.fadeOut(400);
              }, 5000);

              // Уменьшаем количество товаров в корзине (отрисовка)
              cartCount -= data.quantity_deleted;
              goodsInCartCount.text(cartCount);

              // Меняем содержимое корзины на ответ от django (новый отрисованный фрагмент разметки корзины)
              var cartItemsContainer = $("#cart-items-container");
              cartItemsContainer.html(data.cart_items_html);

          },

          error: function (data) {
              console.log("Error durung deleting item from cart");
          },
      });
  });

  // Теперь + - количества товара
  // Обработчик события для уменьшения значения
  $(document).on("click", ".decrement", function () {
      // Берем ссылку на контроллер django из атрибута data-cart-change-url
      var url = $(this).data("cart-change-url");
      // Берем id корзины из атрибута data-cart-id
      var cartID = $(this).data("cart-id");
      // Ищем ближайшеий input с количеством
      var $input = $(this).closest('.input-group').find('.number');
      // Берем значение количества товара
      var currentValue = parseInt($input.val());
      // Если количества больше одного, то только тогда делаем -1
      if (currentValue > 1) {
          $input.val(currentValue - 1);
          // Запускаем функцию определенную ниже
          // с аргументами (id карты, новое количество, количество уменьшилось или прибавилось, url)
          updateCart(cartID, currentValue - 1, -1, url);
      }
  });

  // Обработчик события для увеличения значения
  $(document).on("click", ".increment", function () {
      // Берем ссылку на контроллер django из атрибута data-cart-change-url
      var url = $(this).data("cart-change-url");
      // Берем id корзины из атрибута data-cart-id
      var cartID = $(this).data("cart-id");
      // Ищем ближайшеий input с количеством
      var $input = $(this).closest('.input-group').find('.number');
      // Берем значение количества товара
      var currentValue = parseInt($input.val());

      $input.val(currentValue + 1);

      // Запускаем функцию определенную ниже
      // с аргументами (id карты, новое количество, количество уменьшилось или прибавилось, url)
      updateCart(cartID, currentValue + 1, 1, url);
  });

  function updateCart(cartID, quantity, change, url) {
      $.ajax({
          type: "POST",
          url: url,
          data: {
              basket_id: cartID,
              amount: quantity,
              csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
          },

          success: function (data) {
               // Сообщение
              successMessage.html(data.message);
              successMessage.fadeIn(400);
               // Через 7сек убираем сообщение
              setTimeout(function () {
                   successMessage.fadeOut(400);
              }, 7000);

              // Изменяем количество товаров в корзине
              var goodsInCartCount = $("#goods-in-cart-count");
              var cartCount = parseInt(goodsInCartCount.text() || 0);
              cartCount += change;
              goodsInCartCount.text(cartCount);

              // Меняем содержимое корзины
              var cartItemsContainer = $("#cart-items-container");
              cartItemsContainer.html(data.cart_items_html);

          },
          error: function (data) {
              console.log("Помилка при спробі додати товар до корзини");
          },
      });
  }

  var notification = $("#notification");
  if (notification.length > 0) {
    setTimeout(function () {
      notification.alert("close");
    }, 5000);
  }

  $("#modalButton").click(function () {
    $("#exampleModal").appendTo("body");

    $("#exampleModal").modal("show");
  });

  // Click on the button to close the cart windows
  $("#exampleModal .btn-close").click(function () {
    $("#exampleModal").modal("hide");
  });

  // Delivery method selection radio button event handler
  $("input[name='requires_delivery']").change(function () {
    var selectedValue = $(this).val();
    // Hide or show shipping address inputs
    if (selectedValue === "1") {
      $("#deliveryAddressField").show();
    } else {
      $("#deliveryAddressField").hide();
    }
  });
});
