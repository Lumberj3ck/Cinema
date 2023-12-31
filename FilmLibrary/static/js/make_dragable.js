$(function () {
    // Set the initial position of the ".theater_wrapper" element
    $(".theater_wrapper").css({top: 40, left: 0});

    $(".theater_wrapper").draggable({
        containment: [-300, 40, 300, 280],
        revert: function (dropped) {
            // Получаем элемент .cinema-hall
            var cinemaHall = $(".theater_wrapper");

            // Получаем текущий масштаб элемента .cinema-hall
            var scale = parseFloat(cinemaHall.css("transform").split(',')[3]);

            // Если масштаб меньше 1, возвращаем true (на стартовую позицию),
            // в противном случае, возвращаем false (в оригинальное положение)
            return scale <= 1;
        }
    });
});