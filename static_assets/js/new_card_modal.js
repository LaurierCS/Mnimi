const modal = document.querySelector('.new_card_modal_wrapper');
const trigger = document.querySelector('.trigger');
const closeButton = document.querySelector('.modal_close_button');

function toggleModal() {
    modal.classList.toggle('show_modal');
}

function windowOnClick(event) {
    if (event.target === modal) {
        toggleModal();
    }
}

trigger.addEventListener('click', toggleModal);
closeButton.addEventListener('click', toggleModal);