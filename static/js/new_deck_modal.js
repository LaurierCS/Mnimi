const editModal = document.querySelector('.new_deck_modal_wrapper');
const editTrigger = document.querySelectorAll('.new_deck_trigger');
const editCloseButton = document.querySelectorAll('.modal_close_button');

function toggleEditModal() {
    editModal.classList.toggle('show_modal');
}

function windowOnClick(event) {
    if (event.target === editModal) {
        toggleEditModal();
    }
}

editTrigger.forEach(trigger => {
    trigger.addEventListener('click', toggleEditModal);
})

editCloseButton.forEach(button => {
    button.addEventListener('click', toggleEditModal);
})

