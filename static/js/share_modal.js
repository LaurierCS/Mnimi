const shareModal = document.querySelector('.share_modal_wrapper');
const shareTrigger = document.querySelectorAll('.share_trigger');
const shareCloseButton = document.querySelectorAll('.share_modal_close_button');

function toggleShareModal() {
    shareModal.classList.toggle('show_modal');
}

function shareModalWindowOnClick(event) {
    if (event.target === shareModal) {
        toggleShareModal();
    }
}

shareTrigger.forEach(trigger => {
    trigger.addEventListener('click', toggleShareModal);
})

shareCloseButton.forEach(button => {
    button.addEventListener('click', toggleShareModal);
})
