$(document).ready(function(){
    $('#clear').click(function() {
        $('#template').val('');
        $('#render').val('');
        $('#values').val('');
        $('#optiontype').val('');
        $('#render').html('');
    });

    $('#convert').click(function() {
        var is_checked_showwhitespaces = $('input[name="showwhitespaces"]').is(':checked') ? 1:0;
        var is_checked_dummyvalues = $('input[name="dummyvalues"]').is(':checked') ? 1:0;
        var is_selected_optiontype = $('input[name="optiontype"]:checked').val();

        // Push the input to the Jinja2 api (Python)
        $.post('/convert', {
            template: $('#template').val(),
            values: $('#values').val(),
            optiontype: is_selected_optiontype,
            showwhitespaces: is_checked_showwhitespaces,
            dummyvalues: is_checked_dummyvalues
        }).done(function(response) {
            // Grey out the white spaces chars if any
            response = response.replace(/•/g, '<span class="whitespace">•</span>');

            // Display the answer
            $('#render').html(response);
        });
    });
});
