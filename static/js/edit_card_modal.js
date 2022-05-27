const editModal = document.querySelector('.edit_card_modal_wrapper');
const editTrigger = document.querySelector('.edit_trigger');
const editCloseButton = document.querySelector('.edit_card_modal_close_button');

function toggleEditModal() {
    editModal.classList.toggle('show_modal');
}

function windowOnClick(event) {
    if (event.target === editModal) {
        toggleEditModal();
    }
}

editTrigger.addEventListener('click', toggleEditModal);
editCloseButton.addEventListener('click', toggleEditModal);