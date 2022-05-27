const newCardModal = document.querySelector('.new_card_modal_wrapper');
const newCardTrigger = document.querySelector('.trigger');
const newCardCloseButton = document.querySelector('.modal_close_button');

function newCardToggleModal() {
    newCardModal.classList.toggle('show_modal');
}

function newCardWindowOnClick(event) {
    if (event.target === newCardModal) {
        newCardToggleModal();
    }
}

newCardTrigger.addEventListener('click', newCardToggleModal);
newCardCloseButton.addEventListener('click', newCardToggleModal);