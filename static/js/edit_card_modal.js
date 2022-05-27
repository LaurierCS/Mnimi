const editModal = document.querySelector('.edit_card_modal_wrapper');
const editTrigger = document.querySelectorAll('.edit_trigger');
const editCloseButton = document.querySelectorAll('.edit_card_modal_close_button');

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

