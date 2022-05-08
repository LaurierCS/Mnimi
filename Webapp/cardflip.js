JAVASCRIPT:


$(".study_card-grid").flip({
  trigger: "manual"
});

$(".flip").click(function() {
  $(this)
    .closest(".study_card-grid")
    .flip(true);
});

$(".unflip").click(function() {
  $(this)
    .closest(".study_card-grid")
    .flip(false);
});
