$(document).ready(function() {
    main();
});

function main() {
    setInterval(function() {
        $.ajax({url: '/status/getImage/', success: function(data) {
            $('#imageContainer').html('<img src="data:image/png;base64,' + data + '" />');
        }
        });
    }, 330);
}
