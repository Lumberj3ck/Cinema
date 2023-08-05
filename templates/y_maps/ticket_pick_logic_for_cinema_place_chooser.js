function unselect(seat) {
    seat.innerHTML = "<img src='https://ticket.kino.kz/static/media/empty_light.f550f048.svg' alt=''>"
    seat.className = 'seat'
}

function close_all_selected() {
    document.querySelectorAll('.choice').forEach(item => item.classList.toggle('choice'))
}

function close_last_selected() {
    // last_selected = document.querySelectorAll('.choice')
    // last_selected_elem1 = last_selected[last_selected.length - 1]
    if (last_selected && !selected_tickets.includes(last_selected)) {
        unselect(last_selected)
    }
}

function canvas_is_open() {
    offcanvas = document.getElementById('offcanvasBottom')
    return offcanvas.classList.contains('show')

}

function open_offcanvas() {
    offcanvas = document.getElementById('offcanvasBottom')
    if (!offcanvas.classList.contains('show')) {
        offcanvas.classList.toggle('show')
    }
}

function open_permcanvas() {
    offcanvas = document.getElementById('places_choosen')
    if (!offcanvas.classList.contains('show')) {
        offcanvas.classList.toggle('show')
    }
}

function close_off_canvas() {
    offcanvas = document.getElementById('offcanvasBottom')
    if (offcanvas.classList.contains('show')) {
        offcanvas.classList.toggle('show')
    }
}

function btn_close() {
    close_last_selected()
    offcanvas = document.getElementById('offcanvasBottom')
    if (offcanvas.classList.contains('show')) {
        offcanvas.classList.toggle('show')
    }
}

function permanent_close() {
    close_last_selected()
    offcanvas = document.getElementById('places_choosen')
    if (offcanvas.classList.contains('show')) {
        offcanvas.classList.toggle('show')
    }
}


const adult_but = document.getElementById('adult')
const student_but = document.getElementById('student')
const permanent_off = document.getElementById('places_choosen')
var selected_tickets = []

function onDeleteButtonClick(event) {
    const ticketItem = event.target.closest(".ticket_item");
    if (ticketItem) {
        const rowAndSeat = ticketItem.querySelector(".ticket_label").textContent;
        const regex = /\d+/g;
        const numbers = rowAndSeat.match(regex);
        removeElementFromSavedList(numbers[0], numbers[1]);
        ticketItem.remove();
    }
    if (selected_tickets.length === 0) {
        permanent_close()
    }
}

function on_click_for_delete_button() {
    const deleteButtons = document.querySelectorAll(".delete_btn");
    deleteButtons.forEach((button) => {
        button.addEventListener("click", onDeleteButtonClick);
    });
}

function removeElementFromSavedList(row, seat) {
    const index = selected_tickets.findIndex((element) => element.element.querySelector('.picked_seat').textContent === seat && element.element.parentElement.title === row);
    ticket_object = selected_tickets[index]
    unselect(ticket_object.element)
    type = ticket_object.type
    var delete_ticket_price = type === "adult" ? 2000 : 1300;
    price -= delete_ticket_price
    if (index !== -1) {
        selected_tickets.splice(index, 1);
        update_permanent_offcanvas_header()
    }
}

function pluralize(number) {
    var word = "билет";
    var forms = ["билет", "билета", "билетов"];
    if (number % 100 >= 11 && number % 100 <= 14) {
        return word + "ов";
    }
    var lastDigit = number % 10;
    if (lastDigit === 1) {
        return word;
    } else if (lastDigit >= 2 && lastDigit <= 4) {
        return forms[1];
    } else {
        return forms[2];
    }
}

price = 0

function update_permanent_offcanvas_header() {
    quontity = selected_tickets.length
    pluralized = pluralize(quontity)
    label.textContent = `${quontity} ${pluralized}: ${price}₸`
}

class TicketData {
    constructor(element, type) {
        this.element = element;
        this.type = type;
    }
}

function

append_ticket(event) {
    close_off_canvas()
    which = event.target.closest('.type_button').id
    price += which === 'adult' ? 2000 : 1300;
    open_permcanvas()
    new_ticket = new TicketData(last_selected, which)
    selected_tickets.push(new_ticket)
    last_selected_content = get_info_about_seat(last_selected)
    const newDiv = document.createElement("div");
    newDiv.className = "ticket_item";
    newDiv.innerHTML = `<span class='ticket_label'>${last_selected_content}</span><img src='https://ticket.kino.kz/static/media/gray-close.f3663d50.svg' alt='' class='delete_btn'>`
    div = document.querySelector('.ticket_items_wrapper')
    label = document.querySelector('#offcanvasBottomLabel')
    update_permanent_offcanvas_header()
    div.appendChild(newDiv)
    on_click_for_delete_button()
}

adult_but
    .addEventListener('click',append_ticket)
student_but
    .addEventListener('click', append_ticket)
function

izoomIn() {
    const element = document.getElementById('theater_wrapper');
    const currentScale = window.getComputedStyle(element).transform;
    const currentScaleValue = currentScale === 'none' ? 1 : parseFloat(currentScale.split(',')[0].split('(')[1]);
    if (currentScaleValue >= 3) {
        element.style.transform = 'scale(1)'
    } else {
        element.style.transform = `scale(${currentScaleValue + 0.3})`;
    }
}

function

izoomOut() {
    const element = document.getElementById('theater_wrapper');
    const currentScale = window.getComputedStyle(element).transform;
    const currentScaleValue = currentScale === 'none' ? 1 : parseFloat(currentScale.split(',')[0].split('(')[1]);
    if ((currentScaleValue - 0.3) === 1) {
        element.style.top = '100px'
        element.style.left = '0px'
    }
    if (currentScaleValue <= 0.5) {
        element.style.transform = 'scale(1)'
    } else {
        element.style.transform = `scale(${currentScaleValue - 0.3})`;
    }
}

const
    cinemaHall = document.querySelector('.cinema-hall');

for (let row = 1; row <= 8; row++) {
    row_name = document.createElement('div')
    row_name.innerHTML = `<span class="row_num">${row}</span>`
    row_name.title = row
    row_name.className = 'seat_row'
    cinemaHall.appendChild(row_name)
    seat_numbers = {7: 17, 8: 18}
    n = 14
    if (row in seat_numbers
    ) {
        n = seat_numbers[row]
    }
    for (let seat = 1; seat <= n; seat++) {
        const seatDiv = document.createElement('div');
        seatDiv.className = 'seat';
        seatDiv.title = seat
        row_name.appendChild(seatDiv);
        seat_img = document.createElement('img');
        seat_img.src = 'https://ticket.kino.kz/static/media/empty_light.f550f048.svg'
        seatDiv.appendChild(seat_img)
    }
}
const seats = document.querySelectorAll('.seat');

function get_info_about_seat(seat) {
    row = seat.parentElement.title
    clean_text = `${row} ряд ${seat.title} место`
    return clean_text;
}

seats.forEach(seat => {
    seat.addEventListener('click', () => {
        if (seat.classList.contains('reserved')) {
            alert('Место уже занято!');
        } else if (seat.classList.contains('choice')) {
            btn_close()
        } else {
            if (!canvas_is_open()) {
                open_offcanvas()
                offcanvas_text = document.getElementById('offcanvasBottomLabel1')
                last_selected = seat
                offcanvas_text.innerText = get_info_about_seat(seat)
                seat.innerHTML = `<img src='https://ticket.kino.kz/static/media/picked.da337db8.svg' alt=''><span class='picked_seat' >${seat.title}</span>`
                seat.className = 'seat choice'
            } else {
                btn_close()
            }
        }
    });
});
