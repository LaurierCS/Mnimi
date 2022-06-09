const deleteModal = document.querySelector('.delete_card_modal_wrapper');
const deleteTrigger = document.querySelectorAll('.delete_trigger');
const deleteCloseButton = document.querySelectorAll('.delete_card_modal_close_button');

function toggledeleteModal() {
    deleteModal.classList.toggle('show_modal');
}

function windowOnClick(event) {
    if (event.target === deleteModal) {
        toggledeleteModal();
    }
}

deleteTrigger.forEach(trigger => {
    trigger.addEventListener('click', toggledeleteModal);
})

deleteCloseButton.forEach(button => {
    button.addEventListener('click', toggledeleteModal);
})

