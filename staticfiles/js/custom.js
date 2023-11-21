$(document).on('show.bs.collapse hide.bs.collapse', '.collapse', function(e) {
    e.stopPropagation();
    console.log('event triggered');
});